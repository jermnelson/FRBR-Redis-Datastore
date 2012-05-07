"""
 :mod:`commands` Budget Redis Commands
"""
__author__ = 'Jeremy Nelson'
import re,redis,pymarc
import datetime,sys

redis_server = redis.StrictRedis(host='tuttlibsys',port=7300)

def get_invoice(**kwargs):
    """
    Function takes either an invoice number or the redis key for the
    invoice and returns a dictionary with the invoice information and
    all associated transactions.

    :param number: Invoice number, optional
    :param redis_key: Invoice redis_key, optional
    :rtype: dictionary
    """
    # redis_key variable scoped to function, starts with None
    redis_key = None
    # If an invoice number parameter, try to retrieve redis_key
    # from the invoice:numbers Redis hash
    if kwargs.has_key('number'):
        redis_key = redis_server.hget('invoice:numbers',
                                      kwargs.get('number'))
    # If an invoice redis_key paramter, first checks consistency
    # and then set func redis_key variable to passed
    if kwargs.has_key('redis_key'):
        direct_redis_key = kwargs.get('redis_key')
        # Checks to see if redis_key param exists in current datastore,
        # raises error if it doesn't
        if not redis_server.exists(direct_redis_key):
            raise ValueError('%s redis key does not exist in datastore' %\
                             direct_redis_key)
        # Should only be set if the code calling this func passes in both
        # an invoice number and a redis_key
        if redis_key is not None:
            # Raise error if the invoice number redis_key differs from
            # passed in redis_key
            if redis_key != direct_redis_key:
                error_msg = 'redis_key of %s not equal to passed in redis_key of %s' %\
                            (redis_key,
                             direct_redis_key)
                raise ValueError(error_msg)
        else:
            # Finally, sets the func redis_key variable to passed in redis_key
            redis_key = direct_redis_key
    invoice_redis_info = redis_server.hgetall(redis_key)
    invoice_redis_info['redis_key'] = redis_key
    # Extracts all transactions associated with this invoice
    redis_transactions = redis_server.zrange('%s:transactions' % redis_key,
                                             0,
                                             -1)
    # Add a list of transaction dicts to invoice_redis_info dict
    # also computes and returns total amount for the invoice
    invoice_redis_info['transactions'] = []
    total_amt = 0
    for transaction_key in redis_transactions:
        transaction = redis_server.hgetall(transaction_key)
        clean_transaction = dict()
        # Add transaction amount to invoice total
        total_amt += float(transaction.get('amount'))
        # Remove invoice from transaction and check to confirm that
        # transaction is for the correct invoice
        if transaction.pop('invoice') != redis_key:
            raise ValueError("Wrong invoice for %s" % transaction_key)
        clean_transaction['redis_key'] = transaction_key
        for k,v in transaction.iteritems():
           template_key = k.replace(" ","_")
           if template_key in ["date","paid_on"]:
               clean_transaction[template_key] = datetime.datetime.strptime(v,
                                                                            '%Y-%m-%d 00:00:00')
           else:
               clean_transaction[template_key] = v
        invoice_redis_info['transactions'].append(clean_transaction)
    invoice_redis_info['total_amount'] = total_amt
    # Return invoice_redis_info to call code
    return invoice_redis_info

invoice_re = re.compile(r"^Inv#\s(?P<number>\d+\w+)\sDated:(?P<date>\d+-\d+-\d+)\sAmt:\$(?P<amount>\d+[,|.]*\d*)\sOn:(?P<paid>\d+-\d+-\d+)\sVoucher#(?P<voucher>\d+)$")
def ingest_invoice(marc_record):
    """
    Function ingests a III Order MARC Record into Redis datastore.

    :param marc_record: MARC record
    :rtype: dictionary
    """
    if marc_record['035']:
        raw_bib = marc_record['035']['a']
        bib_number = raw_bib[1:-1]
    if marc_record['995']:
        invoice_regex = invoice_re.search(marc_record['995']['a'])
    else:
        print("ERROR cannot extract invoice number from %s" % marc_record.leader)
        invoice_regex = None
    if invoice_regex is not None:
        invoice_result = invoice_regex.groupdict()
        
        # Checks to see if invoice exists, add otherwise
        invoice_key = redis_server.hget('invoice:numbers',
                                        invoice_result['number'])
        if invoice_key is None:
            invoice_key = 'invoice:%s' % redis_server.incr('global:invoice')
            redis_server.hset('invoice:numbers',
                              invoice_result.get('number'),
                              invoice_key)
        # Checks if invoice number is present, add otherwise to invoice
        if not redis_server.exists(invoice_key):
            redis_server.hset(invoice_key,
                              'number',
                              invoice_result.get('number'))
            redis_server.hset(invoice_key,
                              'created',
                              datetime.datetime.today())
        # Creates a transaction to associate with invoice
        transaction_key = 'transaction:%s' % redis_server.incr('global:transaction')
        # Converts dates to python datetimes and set in redis
        transaction_date = datetime.datetime.strptime(invoice_result.get('date'),
                                                      '%m-%d-%y')
        if redis_server.hexists(invoice_key,'transaction date'):
            invoice_date = datetime.datetime.strptime(redis_server.hget(invoice_key,
                                                                        'transaction date'),
                                                      '%Y-%m-%d 00:00:00')
            if transaction_date > invoice_date:
                redis_server.hset(invoice_key,
                                  'transaction date',
                                  transaction_date)
        else:
            redis_server.hset(invoice_key,
                              'transaction date',
                              transaction_date)

        redis_server.hset(transaction_key,'date',transaction_date)
        paid_on_date = datetime.datetime.strptime(invoice_result.get('paid'),
                                                  '%m-%d-%y')
        redis_server.hset(transaction_key,'paid on',paid_on_date)
        # Set invoice key and amount to transaction hash
        redis_server.hset(transaction_key,'bib number',bib_number)
        redis_server.hset(transaction_key,'invoice',invoice_key)
        redis_server.hset(transaction_key,'amount',invoice_result.get('amount'))
        # Add to invoice:transactions sorted set by date
        redis_server.zadd('%s:transactions' % invoice_key,
                          transaction_date.toordinal(),
                          transaction_key)
        # Checks exists or adds voucher
        voucher_key = redis_server.hget('invoice:vouchers',
                                        invoice_result.get('voucher'))
        if voucher_key is None:
            voucher_key = 'voucher:%s' % redis_server.incr('global:voucher')
            redis_server.hset('invoice:vouchers',
                              invoice_result.get('voucher'),
                              voucher_key)
            redis_server.hset(voucher_key,
                              'name',
                              invoice_result.get("voucher"))
        redis_server.hset(transaction_key,'voucher',voucher_key)
        
        
def load_order_records(pathname):
    """
    Function takes a path to a MARC file location, creates an iterator,
    and attempts to ingest invoice from each record

    :param pathname: Path to MARC file
    """
    marc_reader = pymarc.MARCReader(open(pathname),
                                    utf8_handling='ignore')
    for counter,record in enumerate(marc_reader):
        if counter%1000:
            sys.stderr.write(".")
        else:
            sys.stderr.write("%s" % counter)
        ingest_invoice(record)
        
        
        
                          
            
            
        
        

    
                             
    
    
