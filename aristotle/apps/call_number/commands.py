"""
 :mod:`commands` Call Number Helper Utilities
"""
import pymarc,redis,re


redis_server = redis.StrictRedis(host='0.0.0.0',
                                 port=6379,
                                 db=4)

english_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
                    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
                    'Y', 'Z']

lccn_first_cutter_re = re.compile(r"^(\D+)(\d+)")

def generate_search_set(call_number):
    sections = call_number.split(".")
    first_cutter = sections[0].strip()
    for i in range(0,len(first_cutter)):
        redis_server.zadd('call-number-sorted-set',0,first_cutter[0:i])
    redis_server.zadd('call-number-sorted-set',0,first_cutter)
    redis_server.zadd('call-number-sorted-set',0,'%s*' % call_number)   

def get_callnumber(record):
    for field_tag in ['086','090','099','050']:
        if record[field_tag] is not None:
            return record[field_tag].value()

def get_previous(call_number):
    current_rank = redis_server.zrank('call-number-sort-set',call_number)
    entities = []
    previous_callnumbers = redis_server.zrange('call-number-sort-set',current_rank-2,current_rank-1)
    for number in previous_callnumbers:
        entities.append(record(number))
    return entities    

def get_next(call_number):
    current_rank = redis_server.zrank('call-number-sort-set',call_number)
    entities = []
    next_callnumbers = redis_server.zrange('call-number-sort-set',current_rank+1,current_rank+2)
    for number in next_callnumbers:
        entities.append(record(number))
    return entities    


def old_get_slice(start,end):
    entities = []
    positions = redis_server.lrange('call_numbers',
                                    start,
                                    end)
    for redis_id in positions:
        entity = redis_server.hgetall("record:%s" % redis_id)
        if entity['author'] == 'None':
            entity['author'] = None
        else:
            entity['author'] = [entity['author'],]
        entities.append(entity)
    return entities


def ingest_record(marc_record):
    bib_number = record['907']['a'][1:-1]
    call_number = get_callnumber(marc_record)
    if call_number is None:
        return None
    redis_id = redis_server.incr("global:record")
    redis_key = "record:%s" % redis_id
    redis_server.hset(redis_key,"title",marc_record.title())
    redis_server.hset(redis_key,"author",record.author())
    redis_server.hset(redis_key,"bib_number",bib_number)
    redis_server.hset(redis_key,"call_number",call_number)
    isbn = record.isbn()
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
    

def old_ingest_records(marc_file):
    marc_reader = pymarc.MARCReader(open(marc_file,"rb"))
    for record in marc_reader:
                call_number = get_callnumber(record)
        if call_number is None:
            pass
        else:
                        redis_server.rpush("all_records",redis_id)
            redis_server.sort("all_records",
                      by="record:*->call_number",
                      alpha=True,
                      store="call_numbers")
    sorted_callnumbers = redis_server.lrange('call_numbers',0,-1)
    for i,redis_id in enumerate(sorted_callnumbers):
        redis_server.hset("record:%s" % redis_id,
                          "sort-position",
                          i)


def record(call_number):
    record_key = redis_server.hget('call-number-hash',call_number)
    return redis_server.hgetall(record_key)

def search(query):
    set_rank = redis_server.zrank('call-number-sorted-set',,query)
    result = []
    for row in redis_server.zrange('call-number-sorted-set',set_rank,-1):
        if row[-1] == "*":
            result.append(row[:-1])
            return result
        else:
            result.append(row)
    return result
