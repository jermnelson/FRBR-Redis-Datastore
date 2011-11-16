"""
:mod:`vra`   Models for VRA Redis datastore 
"""
__author__ = "Jeremy Nelson"

import common

class agent(common.BaseModel):
    """
    :class:`agent`
    """

    def __init__(self,**kwargs):
        """
        Creates an instance of a :class:`agent`

        :param redis_key: Redis key for vra:agent, default is vra:agent
        """
        if not kwargs.has_key("redis_key"):
            kwargs['redis_key'] = "vra:agent"
        common.BaseModel.__init__(self,**kwargs)
