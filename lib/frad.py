"""
  :mods:`frad` Functional Requirements for Authority Data (FRAD) Redis
               set-up and support
"""
__author__ = 'Jeremy Nelson'

import common

FRAD_RDF_URL = 'http://metadataregistry.org/schema/show/id/24.rdf'


def load_rdf(rdf_url=FRAD_RDF_URL):
    pass

class CorporateBody(common.BaseModel):
    """
    :class:`CorporateBody` class includes attributes and roles with other
    Entities in the datastore.
    """

    def __init__(self,**kwargs):
        """
        Creates an instance of :class:`CorporateBody` 

        :param redis_key: Redis key for FRAD CorporateBody, default is
                          frad:CorporateBody
        """ 
        if not kwargs.has_key("redis_key"):
            kwargs['redis_key'] = 'frad:CorporateBody'
        common.BaseModel.__init__(self,**kwargs)


class Family(common.BaseModel):
    """
    :class:`Family` class includes attributes and roles with other
    Entities in the datastore.
    """

    def __init__(self,**kwargs):
        """
        Creates an instance of :class:`Family` 

        :param redis_key: Redis key for FRAD Family, default is
                          frad:Family
        """ 
        if not kwargs.has_key("redis_key"):
            kwargs['redis_key'] = 'frad:Family'
        common.BaseModel.__init__(self,**kwargs)


