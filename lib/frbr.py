"""
  frbr.py -- Models for FRBR Redis datastore
"""
__author__ = "Jeremy Nelson"

import datetime,os,logging
import redis,urllib2
import namespaces as ns
import common
from lxml import etree

FRBR_RDF_URL = 'http://metadataregistry.org/schema/show/id/5.rdf'

def load_rdf(rdf_url=FRBR_RDF_URL):
    """
    Function takes an URL to a RDF file and creates a FRBR Redis
    datastore using key syntax of **frbr.reg_name**

    :param rdf_url: URL of FRBR RDF, default is FRBR_RDF_URL
                    constant.
    """
    raw_frbr_rdf = urllib2.urlopen(rdf_url).read()
    frbr_rdf = etree.XML(raw_frbr_rdf)
    rdf_descriptions = frbr_rdf.findall('{%s}Description' % \
                                        ns.RDF)
    for element in rdf_descriptions:
        about_url = element.attrib['{%s}about' % ns.RDF]
        rdf_type = element.find('{%s}type' % ns.RDF)
        rdfs_label = element.find('{%s}label' % ns.RDFS)
        reg_name = element.find('{%s}name' % ns.REG)
        if reg_name is not None:
            redis_key = 'frbr.%s' % reg_name.text
        elif rdfs_label is not None:
            redis_key = 'frbr.%s' % rdfs_label.strip()
        else:
            redis_key = None
        skos_definition = element.find('{%s}definition' % ns.SKOS)
        if rdf_type is not None:
            if rdf_type.attrib.has_key('{%s}resource' % ns.RDF):
                resource_type = rdf_type.attrib['{%s}resource' % ns.RDF]
                if resource_type == 'http://www.w3.org/2002/07/owl#Class':
                    common.redis_server.set("%s:label" % redis_key,
                                            rdfs_label.text)
                    common.redis_server.set("%s:definition" % redis_key,
                                            skos_definition.text)
                    print("Added %s with key %s to datastore" % (rdfs_label,
                                                                 redis_key))


class Expression(common.BaseModel):
    """
    :class:`Expression` class includes attributes and roles with other Entities in 
    the datastore.
    """

    def __init__(self,**kwargs):
        """
        Creates an instance of :class:`Expression` 

        :param redis_key: Redis key for FRBR Expression, default is frbr:Expression
        """ 
        if not kwargs.has_key("redis_key"):
            kwargs['redis_key'] = 'frbr:Expression'
        common.BaseModel.__init__(self,**kwargs) 

    def date(self,date=None):
        """
        Method returns :class:`Expression` instance's date or set of date 
       
        :param date: Optional date to add to the set of dates for 
                     :class:`Expression` 
        """
        return self.get_or_set_property("date",date)

    def distingushing_characteristic(self,characteristic=None):
        """
        Method returns :class:`Expression` instance's context or set of contexts 
        
        :param context: Optional form to add to the set of forms for the
                        :class:`Expression`
        """
        return self.get_or_set_property("distingushing characteristic",
                                        characteristic)

    def extensibility(self,extensibility=None):
        """
        Method returns :class:`Expression` instance's entity or set of
        entities that extends the current instance.  
        
        :param context: Optional entity to add to the set of extensibility for the
                        :class:`Expression`
        """
        return self.get_or_set_property("extensibility",
                                        extensibility)
    def extent(self,entity=None):
        """
        Method returns :class:`Expression` instance's entity or set of
        entities that make up the extent for the instance.  
        
        :param context: Optional entity to add to the set of extent for the
                        :class:`Expression`
        """
        return self.get_or_set_property("extent",
                                        entity)


    def form(self,form=None):
        """
        Method returns :class:`Expression` instance's form or set of forms 
        
        :param form: Optional form to add to the set of forms for the
                     :class:`Expression`
        """
        return self.get_or_set_property("form",form)
    

    def language(self,language=None):
        """
        Method returns :class:`Expression` instance's form or set of forms 
        
        :param form: Optional form to add to the set of forms for the
                     :class:`Expression`
        """
        return self.get_or_set_property("language",language)



    def realized_by(self,entity=None):
        """
        Method returns :class:`Expression` instance realized by either a Person or
        CorporateBody.
        
        :param title: Optional form to add to the set of forms for the
                      :class:`Expression`
        """
        return self.get_or_set_property("realized by",entity)

    def revisability(self,entity=None):
        """
        Method returns :class:`Expression` instance's revisability 
        
        :param form: Optional entity to add to the set of entity for the
                     :class:`Expression`
        """
        return self.get_or_set_property("revisability",entity)

    def summarization(self,summarization=None):
        """
        Method returns :class:`Expression` instance's title or set of titles 
        
        :param summarization: Optional summarization to add to the set of 
                              summarizationforms for the :class:`Expression`
        """
        return self.get_or_set_property("summarization",summarization)



    def title(self,title=None):
        """
        Method returns :class:`Expression` instance's title or set of titles 
        
        :param title: Optional form to add to the set of forms for the
                      :class:`Expression`
        """
        return self.get_or_set_property("title",title)


class Work(common.BaseModel):
    """
    :class:`Work` class includes attributes and roles with other Entities in 
    the datastore.
    """

    def __init__(self,**kwargs):
        """
        Creates an instance of :class:`Work` 

        :param redis_key: Redis key for FRBR Work, default is frbr:Work
        """ 
        if not kwargs.has_key("redis_key"):
            kwargs['redis_key'] = 'frbr:Work'
        common.BaseModel.__init__(self,**kwargs) 



    def audience(self,audience=None):
        """
        Method returns entity or entities that created :class:`Work` instance 
        
        :param entity: Optional entity to add to the set of creators for the
                       :class:`Work`
        """
        return self.get_or_set_property("intended audience",
                                        audience)

 
    def created_by(self,entity=None):
        """
        Method returns entity or entities that created :class:`Work` instance 
        
        :param entity: Optional entity to add to the set of creators for the
                       :class:`Work`
        """
        return self.get_or_set_property("created by",entity)


    def context(self,context=None):
        """
        Method returns :class:`Work` instance's context or set of contexts 
        
        :param context: Optional form to add to the set of forms for the
                        :class:`Work`
        """
        return self.get_or_set_property("context",context)


    def created_on(self,new_date=None):
        """
        Method returns the date of when :class:`Work` instance was originally
        created
        
        :param new_date: Optional, replaces existing date or adds new date
        """
        if new_date is not None:
            common.redis_server.hset(self.redis_key,"date created",new_date)
        return common.redis_server.hget(self.redis_key,"date created")



    def distingushing_characteristic(self,characteristic=None):
        """
        Method returns :class:`Work` instance's context or set of contexts 
        
        :param context: Optional form to add to the set of forms for the
                        :class:`Work`
        """
        return self.get_or_set_property("distingushing characteristic",
                                        characteristic)


    def form(self,form=None):
        """
        Method returns :class:`Work` instance's form or set of forms 
        
        :param form: Optional form to add to the set of forms for the
                     :class:`Work`
        """
        return self.get_or_set_property("form",form)


    def termination(self,termination=None):
        """
        Method returns :class:`Work` instance's intended termination
        
        :param termination: Optional termintation date for the
                            :class:`Work` instance.
        """
        return self.get_or_set_property("intended termination",
                                        termination)


    def title(self,title=None):
        """
        Method returns :class:`Work` instance's title or set of titles 
        
        :param title: Optional form to add to the set of forms for the
                      :class:`Work`
        """
        return self.get_or_set_property("title",title)

  
