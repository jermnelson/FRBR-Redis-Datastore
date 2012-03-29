"""
 :mod:`commands` Call Number Helper Utilities
"""
import pymarc,redis,re
import logging,sys
try:
    import settings 
    REDIS_HOST = settings.REDIS_HOST
    REDIS_PORT = settings.REDIS_PORT
    CALL_NUMBER_DB = settings.CALL_NUMBER_DB
except ImportError:
    # Setup for local development
    REDIS_HOST = '172.25.1.108'
#    REDIS_HOST = '0.0.0.0'
    REDIS_PORT = 6379
    CALL_NUMBER_DB = 4
    

redis_server = redis.StrictRedis(host=REDIS_HOST,
                                 port=REDIS_PORT,
                                 db=CALL_NUMBER_DB)

english_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
                    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
                    'Y', 'Z']

lccn_first_cutter_re = re.compile(r"^(\D+)(\d+)")

def generate_search_set(call_number):
    sections = call_number.split(".")
    first_cutter = sections[0].strip()
    for i in range(0,len(first_cutter)):
        redis_server.zadd('call-number-sorted-search-set',0,first_cutter[0:i])
    redis_server.zadd('call-number-sorted-search-set',0,first_cutter)
    redis_server.zadd('call-number-sorted-search-set',0,'%s*' % call_number)   

def get_callnumber(record):
    for field_tag in ['086','090','099','050']:
        if record[field_tag] is not None:
            return record[field_tag].value()

def get_previous(call_number):
    current_rank = redis_server.zrank('call-number-sort-set',call_number)
    entities = []
    return get_slice(current_rank-2,current_rank-1)

def get_next(call_number):
    current_rank = redis_server.zrank('call-number-sort-set',call_number)
    logging.error("Current rank is %s" % current_rank)
    return get_slice(current_rank+1,current_rank+2)


def get_redis_info():
    redis_info = {'dbsize':redis_server.dbsize(),
                  'info':redis_server.info(),
                  'call_number_size':len(redis_server.hkeys('call-number-hash'))}
    return redis_info

def get_slice(start,stop):
    """
    Function gets a list of entities saved as Redis records

    :param start: Beginning of 
    :param stop: End of slice of sorted call numbers
    :rtype: List of entities saved as Redis records
    """
    entities = []
    record_slice = redis_server.zrange('call-number-sort-set',start,stop)
    for number in record_slice:
        entities.append(get_record(number))
    return entities

def get_record(call_number):
    record_key = redis_server.hget('call-number-hash',call_number)
    return redis_server.hgetall(record_key)


def ingest_record(marc_record):
    bib_number = marc_record['907']['a'][1:-1]
    call_number = get_callnumber(marc_record)
    if call_number is None:
        return None
    redis_id = redis_server.incr("global:record")
    redis_key = "record:%s" % redis_id
    redis_server.hset(redis_key,"title",marc_record.title())
    redis_server.hset(redis_key,"author",marc_record.author())
    redis_server.hset(redis_key,"bib_number",bib_number)
    redis_server.hset(redis_key,"call_number",call_number)
    isbn = marc_record.isbn()
    if isbn is not None:
        redis_server.hset(redis_key,"isbn",isbn)
    # Create search set
    generate_search_set(call_number)
    redis_server.hset('bib-number-hash',bib_number,redis_key)
    redis_server.hset('call-number-hash',call_number,redis_key)
    redis_server.zadd('call-number-sort-set',0,call_number) 


def ingest_records(marc_file_location):
    marc_reader = pymarc.MARCReader(open(marc_file_location,"rb"))
    for record in marc_reader:
        ingest_record(record)
    

def search(query):
    set_rank = redis_server.zrank('call-number-sorted-set',query)
    output = {'result':[]}
    for row in redis_server.zrange('call-number-sorted-set',set_rank,-1):
        if row[-1] == "*":
            call_number = row[:-1]
            record = get_record(call_number)
            output['result'].append(call_number)
            output['record'] = record
            output['discovery_url'] = '%s%s' % (settings.settings.DISCOVERY_RECORD_URL,
                                                record['bib_number'])
            return output
        else:
            output['result'].append(row)
    return output
