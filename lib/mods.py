"""
  :mod:`mods` -- MODS Redis set-up and support
"""
__author__ = 'Jeremy Nelson'

import datetime,os,logging
from redisco import models,connection_setup
import redis,urllib2,common
from lxml import etree
import namespaces as ns


def set_attributes(xml_element,
                   redis_mods):
    """
    Helper function take XML element and Redis MODS object
    and iterites through all of the XML's attributes and
    checks and sets any existing attributes in the Redis
    MODS object

    :param xml_element: XML element
    :param redis_mods: Redis MODS object
    """
    for attribute,value in xml_element.attrib.iteritems():
        if hasattr(redis_mods,attribute):
            setattr(redis_mods,attribute,value)
    if xml_element.attrib.has_key('type') and hasattr(redis_mods,'mods_type'):
        setattr(redis_mods,'mods_type',xml_element.attrib['type'])
    redis_mods.save()
    
class abstract(models.Model):
    """
    abstract MODS element in Redis datastore
    """
    altRepGroup = models.Attribute()
    displayLabel = models.Attribute()
    mods_type = models.Attribute()
    shareable = models.Attribute(default="no")
    value_of = models.Attribute()
    xlink = models.Attribute()
    xml_lang = models.Attribute()

    def load_xml(self,
                 abstract_element):
        """
        Method takes a MODS element and sets Redis attributes

        :param abstract_element: abstract XML element
        """
        set_attributes(abstract_element,self)
        self.value_of = abstract_element.text
        self.save()
        
        
class genre(models.Model):
    """
    genre MODS element in Redis datastore
    """
    altRepGroup = models.Attribute()
    authority = models.Attribute()
    authorityURI = models.Attribute()
    displayLabel = models.Attribute()
    mods_type = models.Attribute()
    script = models.Attribute()
    transliteration = models.Attribute()
    value_of = models.Attribute()
    valueURI = models.Attribute()
    xml_lang = models.Attribute()

    def load_xml(self,
                 genre_element):
        """
        Method takes a MODS element and sets Redis attributes

        :param genre_element: genre XML element
        """
        set_attributes(genre_element,self)
        self.value_of = genre_element.text
        self.save()

class note(models.Model):
    """
    note MODS element in Redis datastore
    """
    altRepGroup = models.Attribute()
    displayLabel = models.Attribute()
    mods_ID = models.Attribute()
    script = models.Attribute()
    transliteration = models.Attribute()
    mods_type = models.Attribute()
    value_of = models.Attribute()
    xlink = models.Attribute()
    xml_lang = models.Attribute()

    def load_xml(self,
                 note_element):
        """
        Method takes MODS xml and updates values in Redis datastores
        based on XML values

        :param note_element: note MODS XML element
        """
        set_attributes(note_element,self)
        self.value_of = note_element.text
        self.save()
       

class form(models.Model):
    """
    form MODS element in Redis datastore
    """
    

class physicalDescription(models.Model):
    """
    physicalDescription MODS element in Redis datastore
    """
    altRepGroup = models.Attribute()
    displayLabel = models.Attribute()
    lang = models.Attribute()
    script = models.Attribute()
    transliteration = models.Attribute()
    xml_lang = models.Attribute()
    
    def load_xml(self,
                 physical_description_element):
        """
        Method takes MODS xml element and updates values in Redis
        datastore
        
        :param physical_description_element: physicalDescription MODS element
        """
        set_attributes(physical_description_element)
        self.save()
    
class typeOfResource(models.Model):
    """
    typeOfResource MODS element in Redis datastore
    """
    collection = models.Attribute()
    manuscript = models.Attribute()
    displayLabel = models.Attribute()
    usage = models.Attribute()
    value_of = models.Attribute()
    
    def load_xml(self,
                 type_of_resource_element):
        """
        Method takes MODS xml and updates values in Redis datastore
        based on XML values
        
        :param type_of_resource_element: typeOfResource XML element
        """
        set_attributes(type_of_resource_element)
        self.value_of = type_of_resource_element.text
        self.save()
        
class mods(models.Model):
    """
     Root MODS element in Redis datastore
    """
    abstracts = models.ListField(abstract)
##    accessCondition
##    classification
##    extension
    genres = models.ListField(genre)
##    identifier
##    language
##    location
##    name
    notes = models.ListField(note)
##    originInfo
##    part
    physicalDescriptions = models.ListField(physicalDescription)
##    recordInfo
##    relatedItem
##    subject
##    tableOfContents
##    targetAudience
##    titleInfo
    typeOfResources = models.ListField(typeOfResource)
    mods_ID = models.Attribute()
    version = models.Attribute(default="3.4")

    def load_xml(self,
                  mods_xml):
        """
        Method takes MODS xml and updates values in Redis datastores
        based on XML values
        """
        abstract_elements = mods_xml.findall('{%s}abstract' % ns.MODS)
        for element in abstract_elements:
            new_abstract = abstract()
            new_abstract.load_xml(element)
            self.abstracts.append(new_abstract)
        genre_elements = mods_xml.findall('{%s}genre' % ns.MODS)
        for element in genre_elements:
            new_genre = genre()
            new_genre.load_xml(element)
            self.genres.append(new_genre)
        note_elements = mods_xml.findall('{%s}note' % ns.MODS)
        for element in note_elements:
            new_note = note()
            new_note.load_xml(element)
            self.notes.append(new_note)
        self.save()
            



# EXAMPLE USAGE
##redis_key = "mods:%s" % redis_server.incr("global:mods")
##redis_server.hset(redis_key,"abstract","Atomic text")
##accessCondition_key = "%s:accessCondition:%s" % (redis_key,
##                                                 redis_server.incr("global:%s:accessCondition"))
##redis_server.hset(accessCondition_key,'creation',1969)
##redis_server.hset(redis_key,'accessCondition',accessCondition_key)
