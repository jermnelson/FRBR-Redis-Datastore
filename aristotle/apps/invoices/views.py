"""
 :mod:`views` Invoices App Views
"""
__author__ = "Jeremy Nelson"

import datetime
from django.views.generic.simple import direct_to_template
from app_settings import APP
from settings import INSTITUTION
import budget.commands as commands

def browse(request):
    """
    browse displays a browsable listing of invoices by year, month, day

    :param request: Web request
    """
    invoice_keys = commands.redis_server.keys("invoice:*")
    invoices = {}
    for key in invoice_keys:
        raw_date = commands.redis_server.hget(key,'transaction date')
        transaction_date = datetime.datetime.strptime(raw_date,
                                                       '%Y-%m-%d 00:00:00')
        if invoices.has_key(transaction_date.year):
            year_transactions = invoices[transaction_date.year]
            if year_transactions.has_key(transaction_date.month):
                month_transactions = year_transactions[transaction_date.month]
                if not month_transactions.has_key(key):
                    month_transactions[key] = transaction_date
            else:
                year_transactions[transaction_date.month] = {key:transaction_date}
        else:
            invoices[transaction_date.year] = {transaction_date.month:{key:transaction_date}}
        
    return direct_to_template(request,
                              'invoices/browse.html',
                              {'app':APP,
                               'institution':INSTITUTION,
                               'invoices':invoices})


def default(request):
    """
    default is the standard view for the invoice app
 
    :param request: Web request
    """
    if request.GET.has_key('invoice_key'):
        invoice_key = request.GET.get('invoice_key')
    elif request.POST.has_key('invoice_key'):
        invoice_key = request.POST.get('invoice_key')
    else:
        invoice_key = commands.redis_server.keys("invoice:*")[-1]
    previous_five = []
    incr_num = int(invoice_key.split(":")[1])
    for i in range(incr_num,incr_num-5,-1):
        redis_key = 'invoice:%s' % i
        if commands.redis_server.exists(redis_key) is True:
            invoice = {'invoice_key':redis_key}
            invoice['number'] = commands.redis_server.hget(redis_key,'number')
            last_transaction = commands.redis_server.zrange('%s:transactions' % redis_key,
                                                            -1,
                                                            -1)
            if len(last_transaction) > 0:
                last_transaction = last_transaction[0]
                raw_date = commands.redis_server.hget(last_transaction,
                                                     'date')
                invoice['date'] = datetime.datetime.strptime(raw_date,
                                                             '%Y-%m-%d 00:00:00')
            previous_five.append(invoice)
    invoice = commands.get_invoice(redis_key=invoice_key)
    return direct_to_template(request,
                              'invoices/app.html',
                              {'app':APP,
                               'institution':INSTITUTION,
                               'invoice':invoice,
                               'previous_invoices':previous_five})
