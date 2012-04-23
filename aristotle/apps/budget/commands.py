import re,redis,pymarc
import datetime

redis_server = redis.StrictRedis(host='tuttdemo')

invoice_re = re.compile(r"^Inv#\s(?P<number>\d+\w+)\sDated:(?P<date>\d+-\d+-\d+)\sAmt:\$(?P<amount>\d+[,|.]*\d*)\sOn:(?P<paid>\d+-\d+-\d+)\sVoucher#(?P<voucher>\d+)$")
def ingest_invoice(marc_record):
    """
    Function checks 

    :param field995s: MARC 995 field subfield a value
    :rtype: dictionary
    """
    if marc_record['035']['a']:
        raw_bib = marc_record['035']['a']
        bib_number = raw_bib[1:-1]
    if marc_record['994']['a']:
        invoice_result = invoice_re.search(marc_record['994']['a'])
    if invoice_result is not None:
        
        # Checks to see if invoice exists, add otherwise
        invoice_key = redis_server.hget('invoice:numbers',
                                        invoice_result['number'])
        if invoice_key is None:
            invoice_key = 'invoice:%s' % redis_server.incr('global:invoice')
            redis_server.hset('invoice:numbers',
                              invoice_result.get('number'),
                              invoice_key)
        # Creates a transaction to associate with invoice
        transaction_key = 'transaction:%s' % redis_server.incr('global:transaction')
        # Converts dates to python datetimes and set in redis
        transaction_date = datetime.datetime.strptime(invoice_result.get('date'),
                                                      '%d-%m-%y')
        redis_server.hset(transaction_key,'date',transaction_date)
        paid_on_date = datetime.datetime.strptime(invoice_result.get('paid'),
                                                  '%d-%m-%y')
        redis_server.hset(transaction_key,'paid on',paid_on_date)
        # Set invoice key and amount to transaction hash
        redis_server.hset(transaction_key,'bib number',bib_number)
        redis_server.hset(transaction_key,'invoice',invoice_key)
        redis_server.hset(transaction_key,'amount',invoice_result.get('amount'))
        # Add to invoice:transactions sorted set by date
        redis_server.zadd('%s:transactions' % invoice_key,
                          transaction_date,
                          transaction_key)
        # Checks exists or adds voucher
        voucher_key = redis_server.hget('invoice:vouchers',
                                        invoice_result.get('voucher'))
        if voucher_key is None:
            voucher_key = 'voucher:%s' % redis_server.incr('global:voucher')
            redis_server.hset('invoice:vouchers',
                              invoice_result.get('voucher'),
                              voucher_key)
        redis_server.hset(transaction_key,'voucher',voucher_key)
        
        
        
        
        
        
                          
            
            
        
        

    
                             
    
    
