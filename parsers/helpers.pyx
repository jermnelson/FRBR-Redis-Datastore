"""
 :mod:`helpers` - Cython speedup functions for parsing MARC records into FRBR
                   entities stored in Redis
"""

def parse_record(record):
    print("In MARC to Python %s" % record)
