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

class culturalContext(common.BaseModel):
    """
    :class:`culturalContext`
    """

    def __init__(self,**kwargs):
        """
        Creates an instance of a :class:`culturalContext`

        :param redis_key: Redis key for vra:culturalContext, default is vra:culturalContext
        """
        if not kwargs.has_key("redis_key"):
            kwargs['redis_key'] = "vra:culturalContext"
        common.BaseModel.__init__(self,**kwargs)

class date(common.BaseModel):
    """
    :class:`date`
    """

    def __init__(self,**kwargs):
        """
        Creates an instance of a :class:`date`

        :param redis_key: Redis key for vra:date, default is vra:date
        """
        if not kwargs.has_key("redis_key"):
            kwargs['redis_key'] = "vra:date"
        common.BaseModel.__init__(self,**kwargs)

class description(common.BaseModel):
    """
    :class:`description`
    """

    def __init__(self,**kwargs):
        """
        Creates an instance of a :class:`description`

        :param redis_key: Redis key for vra:description, default is vra:description
        """
        if not kwargs.has_key("redis_key"):
            kwargs['redis_key'] = "vra:description"
        common.BaseModel.__init__(self,**kwargs)

class inscription(common.BaseModel):
    """
    :class:`inscription`
    """

    def __init__(self,**kwargs):
        """
        Creates an instance of a :class:`inscription`

        :param redis_key: Redis key for vra:inscription, default is
                          vra:inscription
        """
        if not kwargs.has_key("redis_key"):
            kwargs['redis_key'] = "vra:inscription"
        common.BaseModel.__init__(self,**kwargs)

 
class location(common.BaseModel):
    """
    :class:`location`
    """

    def __init__(self,**kwargs):
        """
        Creates an instance of a :class:`location`

        :param redis_key: Redis key for vra:location, default is
                          vra:location
        """
        if not kwargs.has_key("redis_key"):
            kwargs['redis_key'] = "vra:location"
        common.BaseModel.__init__(self,**kwargs)

class material(common.BaseModel):
    """
    :class:`material`
    """

    def __init__(self,**kwargs):
        """
        Creates an instance of a :class:`material`

        :param redis_key: Redis key for vra:material, default is
                          vra:material
        """
        if not kwargs.has_key("redis_key"):
            kwargs['redis_key'] = "vra:material"
        common.BaseModel.__init__(self,**kwargs)

class measurements(common.BaseModel):
    """
    :class:`measurements`
    """

    def __init__(self,**kwargs):
        """
        Creates an instance of a :class:`measurements`

        :param redis_key: Redis key for vra:measurements, default is
                          vra:measurements
        """
        if not kwargs.has_key("redis_key"):
            kwargs['redis_key'] = "vra:measurements"
        common.BaseModel.__init__(self,**kwargs)        
