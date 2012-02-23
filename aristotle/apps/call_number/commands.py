import pymarc,redis


redis_server = redis.StrictRedis(host='solr.coloradocollege.edu',
                                 port=6379,
                                 db=4)

def get_callnumber(record):
    for field_tag in ['086','090','099','050']:
        if record[field_tag] is not None:
            return record[field_tag].value()

def get_slice(start,end):
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

def ingest_records(marc_file):
    marc_reader = pymarc.MARCReader(open(marc_file,"rb"))
    for record in marc_reader:
        bib_number = record['907']['a'][1:-1]
        call_number = get_callnumber(record)
        redis_id = redis_server.incr("global:record")
        redis_key = "record:%s" % redis_id
        redis_server.hset(redis_key,"title",record.title())
        redis_server.hset(redis_key,"author",record.author())
        redis_server.hset(redis_key,"bib_number",bib_number)
        redis_server.hset(redis_key,"call_number",call_number)
        redis_server.rpush("all_records",redis_id)
        redis_server.hset('bib_numbers',bib_number,redis_key)
    redis_server.sort("all_records",
                      by="record:*->call_number",
                      alpha=True,
                      store="call_numbers")
    sorted_callnumbers = redis_server.lrange('call_numbers',0,-1)
    for i,redis_id in enumerate(sorted_callnumbers):
        redis_server.hset("record:%s" % redis_id,
                          "sort-position",
                          i)



