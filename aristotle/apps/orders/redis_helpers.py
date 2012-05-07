"""
 :mod:`commands` Order Redis Commands
"""
__author__ = 'Jeremy Nelson'
import re,redis,pymarc
import datetime,sys
from invoice.redis_helper import ingest_invoice

redis_server = redis.StrictRedis(host='tuttlibsys',port=7300)

PCARD_RE = re.compile(r"^Inv#\sPCARD\s(?P<number>\d+\w+)\sDated:(?P<date>\d+-\d+-\d+)\sAmt:\$(?P<amount>\d+[,|.]*\d*)\sOn:(?P<paid>\d+-\d+-\d+)\sVoucher#(?P<voucher>\d+)")
        
        
                          
            
            
        
        

    
                             
    
    
