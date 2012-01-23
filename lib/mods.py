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
 
 
class baseMODS(models.Model):
    """
    base MODS class contains common attributes used by most elements in
    MODS schema
    """
    lang = models.Attribute()
    script = models.Attribute()
    transliteration = models.Attribute()    
    xml_lang = models.Attribute()
    
class abstract(baseMODS):
    """
    abstract MODS element in Redis datastore
    """
    altRepGroup = models.Attribute()
    displayLabel = models.Attribute()
    mods_type = models.Attribute()
    shareable = models.Attribute(default="no")
    value_of = models.Attribute()
    xlink = models.Attribute()

    def load_xml(self,
                 abstract_element):
        """
        Method takes a MODS element and sets Redis attributes

        :param abstract_element: abstract XML element
        """
        set_attributes(abstract_element,self)
        self.value_of = abstract_element.text
        self.save()
 

class affiliation(baseMODS):
    """
    affiliation MODS element in Redis datastore
    """
    value_of = models.Attribute()
 
    def load_xml(self,
                 affiliation_element):
        """
        Method takes a MODS element and sets Redis datastore
    
        :param affiliation_element: affiliation XML element
        """
        set_attributes(affiliation_element,self)
        self.value_of = affiliation_element.text
        self.save()

class description(baseMODS):
    """
    description MODS element in Redis datastore
    """
    value_of = models.Attribute()
    
    def load_xml(self,
                 description_element):
        """
        Method takes a MODS element and sets Redis datastore
    
        :param description_element: description XML element
        """
        set_attributes(description_element,self)
        self.value_of = description_element.text
        self.save()


class digitalOrigin(baseMODS):
    """
    digitalOrigin MODS element in Redis datastore
    """
    value_of = models.Attribute()
 
    def load_xml(self,
                 digital_origin_element):
        """
        Method takes a MODS element and sets Redis datastore
        values 

        :param digital_origin_element: digitalOrigin XML element
        """
        self.value_of = digital_origin_element.text
        self.save()

class displayForm(baseMODS):
    """
    displayForm MODS element in Redis datastore
    """
    value_of = models.Attribute()
    
    def load_xml(self,
                 display_form_element):
        """
        Method takes MODS element and sets Redis datastore
        
        :param display_form_element: display_form_element
        """
        set_attributes(display_form_element,self)
        self.value_of = display_form_element.text
        self.save()
        
class extent(baseMODS):
    """
    extent MODS element in Redis datastore
    """
    supplied = models.Attribute()
    value_of = models.Attribute()

    def load_xml(self,
                 extent_element):
        """
        Method takes a MODS element and sets Redis datastore
        values
        
        :param extent_element: extent XML element
        """
        set_attributes(extent_element,self)
        self.value_of = extent_element.text
        self.save()

       
class form(baseMODS):
    """
    form MODS element in Redis datastore
    """
    authority = models.Attribute()
    authorityURI = models.Attribute()
    mods_type = models.Attribute()
    value_of = models.Attribute()

    def load_xml(self,
                 form_element):
        """
        Method takes MODS xml element and updates values in Redis
        datastore
        
        :param form_element: form MODS element
        """
        set_attributes(form_element,self)
        self.value_of = form_element.text
        self.save()
       
class genre(baseMODS):
    """
    genre MODS element in Redis datastore
    """
    altRepGroup = models.Attribute()
    authority = models.Attribute()
    authorityURI = models.Attribute()
    displayLabel = models.Attribute()
    mods_type = models.Attribute()
    value_of = models.Attribute()
    valueURI = models.Attribute()
    
    def load_xml(self,
                 genre_element):
        """
        Method takes a MODS element and sets Redis attributes

        :param genre_element: genre XML element
        """
        set_attributes(genre_element,self)
        self.value_of = genre_element.text
        self.save()
        
class namePart(baseMODS):
    """
    name MODS element in Redis datastore
    """
    mods_type = models.Attribute()
    value_of = models.Attribute()
    
    def load_xml(self,
                 namepart_element):
        """
        Method takes a MODS element and sets Redis values

        :param namepart_element: namePart XML element
        """
        set_attributes(namepart_element,self)
        self.value_of = namepart_element.text
        self.save()
        
class roleTerm(baseMODS):
    """
    roleTerm MODS element in Redis datastore
    """
    authority = models.Attribute()
    authorityURI = models.Attribute()
    mods_type = models.Attribute()
    value_of = models.Attribute()
    valueURI = models.Attribute()
    
    def load_xml(self,
                 role_term_element):
        """
        Method takes roleTerm MODS element and sets Redis value
        
        :param role_term_element: roleTerm XML element
        """
        set_attributes(role_term_element,self)
        self.value_of = role_term_element.text
        self.save()
        
class role(baseMODS):
    """
    role MODS element in Redis datastore
    """
    mods_type = models.Attribute()
    roleTerms = models.ListField(roleTerm)
    
    def load_xml(self,
                 role_element):
        """
        Method takes MODS element and sets Redis values
        
        :param role_element: role XML element
        """
        set_attributes(role_element,self)
        role_terms = role_element.findall('{%s}roleTerm' % ns.MODS)
        for element in role_terms:
            new_role_term = roleTerm()
            new_role_term.load_xml(element)
            self.roleTerms.append(new_role_term)
        self.save()
        
class name(baseMODS):
    """
    name MODS element in Redis datastore
    """
    affiliations = models.ListField(affiliation)
    altRepGroup = models.Attribute()
    authority = models.Attribute()
    authorityURI = models.Attribute()
    descriptions = models.ListField(description)
    displayForms = models.ListField(displayForm)
    displayLabel = models.Attribute()
    mods_ID = models.Attribute()
    mods_type = models.Attribute()
    nameParts = models.ListField(namePart)
    nameTitleGroup = models.Attribute()
    roles = models.ListField(role)
    usage = models.Attribute()
    xlink = models.Attribute()
    
    def load_xml(self,
                 name_element):
        """
        Method takes a MODS element and sets Redis values in datastore

        :param name_element: name XML element
        """
        set_attributes(name_element,self)
        affiliation_elements = name_element.findall('{%s}affiliation' % ns.MODS)
        for element in affiliation_elements:
            new_affiliation = affiliation()
            affiliation.load_xml(element)
            self.affiliations.append(affiliation)
        description_elements = name_element.findall('{%s}description' % ns.MODS)
        for element in description_elements:
            new_description = description()
            new_description.load_xml(element)
            self.descriptions.append(new_description)
        display_form_elements = name_element.findall('{%s}displayForm' % ns.MODS)
        for element in display_form_elements:
            new_display_form = displayForm()
            new_display_form.load_xml(element)
            self.displayForms.append(new_display_form)
        name_part_elements = name_element.findall('{%s}namePart' % ns.MODS)
        for element in name_part_elements:
            new_name_part = namePart()
            new_name_part.load_xml(element)
            self.nameParts.append(new_name_part)
        role_elements = name_element.findall('{%s}role' % ns.MODS)
        for element in role_elements:
            new_role = role()
            new_role.load_xml(element)
            self.roles.append(new_role)
        self.save()

    

class note(baseMODS):
    """
    note MODS element in Redis datastore
    """
    altRepGroup = models.Attribute()
    displayLabel = models.Attribute()
    mods_ID = models.Attribute()
    mods_type = models.Attribute()
    value_of = models.Attribute()
    xlink = models.Attribute()
    
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
       



class reformattingQuality(models.Model):
    """
    reformattingQuality MODS element in Redis datastore
    """
    value_of = models.Attribute()

    def load_xml(self,
                 reformatting_quality_element):
        """
        Method takes MODS xml element and updates values in Redis datastore

        :param reformatting_quality_element: reformattingQuality MODS element
        """
        self.value_of = reformatting_quality_element
        self.save()


class physicalDescription(baseMODS):
    """
    physicalDescription MODS element in Redis datastore
    """
    altRepGroup = models.Attribute()
    digitalOrigin = models.ReferenceField(digitalOrigin)
    displayLabel = models.Attribute()
    extents = models.ListField(extent)
    forms = models.ListField(form)
    reformattingQualities = models.ListField(reformattingQuality)
    
    def load_xml(self,
                 physical_description_element):
        """
        Method takes MODS xml element and updates values in Redis
        datastore
        
        :param physical_description_element: physicalDescription MODS element
        """
        set_attributes(physical_description_element,self)
        digital_orig_element = physical_description_element.find('{%s}digitalOrigin' % ns.MODS)
        if digital_orig_element is not None:
            new_dig_org = digitalOrigin()
            new_dig_org.load_xml(digital_orig_element)
            self.digitalOrigin = new_dig_org
        extent_elements = physical_description_element.findall('{%s}extent' % ns.MODS)
        for element in extent_elements:
            new_extent = extent()
            new_extent.load_xml(element)
            self.extents.append(new_extent)
        form_elements = physical_description_element.findall('{%s}form' % ns.MODS)
        for element in form_elements:
            new_form = form()
            new_form.load_xml(element)
            self.forms.append(new_form)
        reformatting_elements = physical_description_element.findall('{%s}reformattingQuality' % ns.MODS)
        for element in reformatting_elements:
            new_reformat_quality = reformattingQuality()
            new_reformat_quality.load_xml(element)
            self.reformattingQualities.append(new_reformat_quality)
        self.save()
        
class topic(baseMODS):
    """
    topic MOCS element in Redis datastore
    """
    authority = models.Attribute()
    authorityURI = models.Attribute()
    value_of = models.Attribute()
    valueURI = models.Attribute()
    
    def load_xml(self,
                 topic_element):
        """
        Method takes MODS xml and updates values in Redis datastore
        based on XML values
        
        :param topic_element: topic XML element
        """
        set_attributes(topic_element,self)
        self.value_of = topic_element.text
        self.save()
        
class subject(baseMODS):
    """
    subject MODS element in Redis datastore
    """
    altRepGroup = models.Attribute()
    authority = models.Attribute()
    authorityURI = models.Attribute()
    displayLabel = models.Attribute()
    mods_ID = models.Attribute()
    usage = models.Attribute()
    topics = models.ListField(topic)
    valueURI = models.Attribute()
    
    def load_xml(self,
                 subject_element):
        """
        Method takes MODS xml and updates values in Redis datastore
        based on XML values
        
        :param subject_element: subject XML element
        """
        set_attributes(subject_element,self)
        topic_elements = subject_element.findall('{%s}topic' % ns.MODS)
        for element in topic_elements:
            new_topic = topic()
            new_topic.load_xml(element)
            self.topics.append(new_topic)
        self.save()
        
        
class subtitle(baseMODS):
    """
    subtitle MODS element in Redis datastore
    """
    value_of = models.Attribute()
    
    def load_xml(self,
                 subtitle_element):
        """
        Method takes MODS xml and updates values in Redis datastore
        based on XML values
        
        :param subtitle_element: title XML element
        """
        set_attributes(subtitle_element,self)
        self.value_of = subtitle_element.text
        self.save()
        
    
class title(baseMODS):
    """
    title MODS element in Redis datastore
    """
    value_of = models.Attribute()
    
    def load_xml(self,
                 title_element):
        """
        Method takes MODS xml and updates values in Redis datastore
        based on XML values
        
        :param title_element: title XML element
        """
        set_attributes(title_element,self)
        self.value_of = title_element.text
        self.save()
        
        
class titleInfo(baseMODS):
    """
    titleInfo MODS element in Redis datastore
    """
    altRepGroup = models.Attribute()
    authority = models.Attribute()
    authorityURI = models.Attribute()
    displayLabel = models.Attribute()
    mods_ID = models.Attribute()
    mods_type = models.Attribute()
    subtitles = models.ListField(subtitle)
    supplied = models.Attribute()
    title = models.ReferenceField(title)
    valueURI = models.Attribute()
    value_of = models.Attribute()
    usage = models.Attribute()
    
    def load_xml(self,
                 title_info_element):
        """
        Method takes MODS xml and updates values in Redis datastore
        based on XML values
        
        :param title_info_element: titleInfo XML element
        """
        set_attributes(title_info_element,self)
        title_element = title_info_element.find('{%s}title' % ns.MODS)
        if title_element is not None:
            new_title = title()
            new_title.load_xml(title_element)
            self.title = new_title
        self.save()
        
class typeOfResource(baseMODS):
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
        set_attributes(type_of_resource_element,self)
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
    names = models.ListField(name)
    notes = models.ListField(note)
##    originInfo
##    part
    physicalDescriptions = models.ListField(physicalDescription)
##    recordInfo
##    relatedItem
    subjects = models.ListField(subject)
##    tableOfContents
##    targetAudience
    titleInfos = models.ListField(titleInfo)
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
        name_elements = mods_xml.findall('{%s}name' % ns.MODS)
        for element in name_elements:
            new_name = name()
            new_name.load_xml(element)
            self.names.append(new_name)
        note_elements = mods_xml.findall('{%s}note' % ns.MODS)
        for element in note_elements:
            new_note = note()
            new_note.load_xml(element)
            self.notes.append(new_note)
        physical_descriptions = mods_xml.findall('{%s}physicalDescription' % ns.MODS)
        for element in physical_descriptions:
            new_physical_desc = physicalDescription()
            new_physical_desc.load_xml(element)
            self.physicalDescriptions.append(new_physical_desc)
        subjects = mods_xml.findall('{%s}subject' % ns.MODS)
        for element in subjects:
            new_subject = subject()
            new_subject.load_xml(element)
            self.subjects.append(new_subject)
        titleInfos = mods_xml.findall('{%s}titleInfo' % ns.MODS)
        for element in titleInfos:
            new_titleInfo = titleInfo()
            new_titleInfo.load_xml(element)
            self.titleInfos.append(new_titleInfo)
        type_of_resources = mods_xml.findall('{%s}typeOfResource' % ns.MODS)
        for element in type_of_resources:
            new_type_of_resource = typeOfResource()
            new_type_of_resource.load_xml(element)
            self.typeOfResources.append(new_type_of_resource)
        self.save()
            



# EXAMPLE USAGE
##redis_key = "mods:%s" % redis_server.incr("global:mods")
##redis_server.hset(redis_key,"abstract","Atomic text")
##accessCondition_key = "%s:accessCondition:%s" % (redis_key,
##                                                 redis_server.incr("global:%s:accessCondition"))
##redis_server.hset(accessCondition_key,'creation',1969)
##redis_server.hset(redis_key,'accessCondition',accessCondition_key)
