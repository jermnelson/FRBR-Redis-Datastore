"""
 :mod:`commands` Budget Redis Commands
"""
__author__ = 'Jeremy Nelson'
import re,redis,pymarc
import datetime,sys
from invoice.redis_helper import ingest_invoice

redis_server = redis.StrictRedis(host='tuttlibsys',port=7300)

def load_all_records(pathname):
    """
    Function takes a path to a MARC file location, creates an iterator,
    and attempts to ingest order and/or pcard info from each record

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
        
        
        
                          
            
            
        
        

    
                             
    
    
