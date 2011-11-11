"""
:mod:`lib.cidoc_crm` Supports the classes and relationships required
by `lib.frbr_oo` and `lib.frbr` among other modules.

Supporting Documentation
------------------------
    * _CIDOC CRM: http://www.cidoc-crm.org/docs/cidoc_crm_version_5.0.3.pdf
"""
__author__ = 'Jeremy Nelson'

import common,os,datetime 
import namespaces as ns
from lxml import etree


class CRMEntity(common.BaseModel):
    """
    :class:`CRMEntity` is the base  
