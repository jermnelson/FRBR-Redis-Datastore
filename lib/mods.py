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

class baseMODSDate(models.Model):
    """
    base MODS date class contains common attributes used by date elements
    in MODS schema
    """
    encoding = models.Attribute()
    point = models.Attribute()
    keyDate = models.Attribute()
    qualifier = models.Attribute()
    
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

class classification(baseMODS):
    """
    class classification MODS element in Redis datastore
    """
    altRepGroup = models.Attribute()
    authority = models.Attribute()
    authorityURI = models.Attribute()
    displayLabel = models.Attribute()
    edition = models.Attribute()
    usage = models.Attribute()
    value_of = models.Attribute()
    valueURI = models.Attribute()

    def load_xml(self,
                 classification_element):
        """
        Method takes MODS element and sets Redis datastore values

        :param date_captured_element: dateCaptured XML element
        """
        set_attributes(classification_element,self)
        self.value_of = classification_element.text
        self.save()


class date(baseMODSDate):
    """
    date MDOS element in Redis datastore
    """
    value_of = models.Attribute()


    def load_xml(self,
                 date_element):
        """
        Method takes MODS element and sets Redis datastore values

        :param date_captured_element: dateCaptured XML element
        """
        set_attributes(date_element,self)
        self.value_of = date_element.text
        self.save()


class dateCaptured(baseMODSDate):
    """
    dateCaptured MODS element in Redis datastore
    """
    value_of = models.Attribute()

    def load_xml(self,
                 date_captured_element):
        """
        Method takes MODS element and sets Redis datastore values

        :param date_captured_element: dateCaptured XML element
        """
        set_attributes(date_captured_element,self)
        self.value_of = date_captured_element.text
        self.save()

class dateCreated(baseMODSDate):
    """
    dateCreated MODS element in Redis datastore
    """
    keyDate = models.Attribute()
    value_of = models.Attribute()

    def load_xml(self,
                 date_created_element):
        """
        Method takes MODS element and sets Redis datastore values

        :param date_created_element: dateCreated XML element
        """
        set_attributes(date_created_element,self)
        
        self.value_of = date_created_element.text
        self.save()

class dateIssued(baseMODSDate):
    """
    dateIssued MODS element in Redis datastore
    """
    keyDate = models.Attribute()
    value_of = models.Attribute()

    def load_xml(self,
                 date_issued_element):
        """
        Method takes MODS element and sets Redis datastore values

        :param date_issued_element: dateIssued XML element
        """
        set_attributes(date_issued_element,self)
        self.value_of = date_issued_element.text
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
    end = models.Attribute()
    start = models.Attribute()
    supplied = models.Attribute()
    unit = models.Attribute()
    value_of = models.Attribute()
    

    def load_xml(self,
                 extent_element):
        """
        Method takes a MODS element and sets Redis datastore
        values
        
        :param extent_element: extent XML element
        """
        set_attributes(extent_element,self)
        if hasattr(extent_element,'text'):
            self.value_of = extent_element.text
        end_element = extent_element.find('{%s}end' % ns.MODS)
        if end_element is not None:
            self.end = end_element.text
        start_element = extent_element.find('{%s}start' % ns.MODS)
        if start_element is not None:
            self.start = start_element.text
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

class identifier(baseMODS):
    """
    identifier MODS element in Redis datastore
    """
    invalid = models.Attribute()
    mods_type = models.Attribute()
    value_of = models.Attribute()

    def load_xml(self,
                 identifier_element):
        """
        Method takes a MODS element and sets Redis attributes

        :param identifier_element: identifier XML element
        """
        set_attributes(identifier_element,self)
        self.value_of = identifier_element.text
        self.save()

    

class url(models.Model):
    """
    url MODS element in Redis datastore
    """
    access = models.Attribute()
    dateLastAccessed = models.Attribute()
    displayLabel = models.Attribute()
    note = models.Attribute()
    usage = models.Attribute()
    value_of = models.Attribute()

    def load_xml(self,
                 url_element):
        """
        Method takes a MODS element and sets Redis attributes

        :param url_element: url XML element
        """
        set_attributes(url_element,self)
        self.value_of = url_element.text
        self.save()
    

class detail(models.Model):
    """
    detail MODS element in Redis datastore
    """
    caption = models.Attribute()
    mods_type = models.Attribute()
    number = models.Attribute()

    def load_xml(self,
                 detail_element):
        """
        Method takes a MODS element and sets Redis values

        :param detail_element: detail XML element
        """
        set_attributes(detail_element,self)
        caption_element = detail_element.find('{%s}caption' % ns.MODS)
        if caption_element is not None:
            self.caption = caption_element.text
        number_element = detail_element.find('{%s}number' % ns.MODS)
        if number_element is not None:
            self.number = number_element.text
        self.save()

class languageTerm(models.Model):
    """
    languageTerm MODS element in Redis datastore
    """
    authority = models.Attribute()
    authorityURI = models.Attribute()
    mods_type = models.Attribute()
    value_of = models.Attribute()
    valueURI = models.Attribute()

    def load_xml(self,
                 language_term_element):
        """
        Method takes a MODS element and sets Redis attributes

        :param language_term_element: languageTerm XML element
        """
        set_attributes(language_term_element,self)
        self.value_of = language_term_element.text
        self.save()

class language(models.Model):
    """
    language MODS element in Redis datastore
    """
    languageTerms = models.ListField(languageTerm)
    objectPart = models.Attribute()

    def load_xml(self,
                 language_element):
        """
        Method takes a MODS element and sets Redis attributes

        :param language_element: language XML element
        """
        set_attributes(language_element,self)
        language_terms_elements = language_element.findall("{%s}languageTerm" % ns.MODS)
        for element in language_terms_elements:
            new_lang_term = languageTerm()
            new_lang_term.load_xml(element)
            self.languageTerms.append(new_lang_term)
        self.save()

class location(baseMODS):
    """
    location MODS element in Redis datastore
    """
    altRepGroup = models.Attribute()
    displayLabel = models.Attribute()
    urls = models.ListField(url)

    def load_xml(self,
                 location_element):
        """
        Method takes a MODS element and sets Redis attributes

        :param location_element: location XML element
        """
        set_attributes(location_element,self)
        url_elements = location_element.findall('{%s}url' % ns.MODS)
        for element in url_elements:
            new_url = url()
            new_url.load_xml(element)
            self.urls.append(new_url)
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
    valueURI = models.Attribute()
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
       
class placeTerm(baseMODS):
    """
    placeTerm MODS element in Redis datastore
    """
    authority = models.Attribute()
    authorityURI = models.Attribute()
    mods_type = models.Attribute()
    value_of = models.Attribute()
    valueURI = models.Attribute()

    def load_xml(self,
                 place_term_element):
        """
        Method takes MODS xml element and updates values in Redis
        datastore
        
        :param place_element: place MODS element
        """
        set_attributes(place_term_element,self)
        self.value_of = place_term_element.text
        self.save()

class place(baseMODS):
    """
    place MODS element in Redis datastore
    """
    placeTerms = models.ListField(placeTerm)

    def load_xml(self,
                 place_element):
        """
        Method takes MODS xml element and updates values in Redis
        datastore
        
        :param place_element: place MODS element
        """
        set_attributes(place_element,self)
        placeterm_elements = place_element.findall('{%s}placeTerm' % ns.MODS)
        for element in placeterm_elements:
            new_place_term = placeTerm()
            new_place_term.load_xml(element)
            self.placeTerms.append(new_place_term)
        self.save()

class publisher(baseMODS):
    """
    publiser MODS element in Redis datastore
    """
    supplied = models.Attribute()
    value_of = models.Attribute()

    def load_xml(self,
                 publisher_element):
        """
        Method takes MODS xml element and updates values in Redis
        datastore
        
        :param publisher_element: publisher MODS element
        """
        set_attributes(publisher_element,self)
        self.value_of = publisher_element.text
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
        self.value_of = reformatting_quality_element.text
        self.save()

class targetAudience(baseMODS):
    """
    targetAudience MODS element in Redis datastore
    """
    authority = models.Attribute()
    value_of = models.Attribute()

    def load_xml(self,
                 target_audience_element):
        """
        Method takes MODS xml element and updates values in Redis datastore

        :param target_audience_element: targetAudience MODS element
        """
        set_attributes(target_audience_element,self)
        self.value_of = target_audience_element.text
        self.save()

    
    
class originInfo(baseMODS):
    """
    originInfo MODS element in Redis datastore
    """
    altRepGroup = models.Attribute()
    dateCaptured = models.ReferenceField(dateCaptured)
    dateCreated = models.ReferenceField(dateCreated)
    dateIssueds = models.ListField(dateIssued)
    displayLabel = models.Attribute()
    issuance = models.Attribute()
    places = models.ListField(place)
    publishers = models.ListField(publisher)

    def load_xml(self,
                 origin_info_element):
        """
        Method takes MODS xml element and updates values in Redis
        datastore
        
        :param origin_info_element: originInfo MODS element
        """
        set_attributes(origin_info_element,self)
        dateCaptured_element = origin_info_element.find('{%s}dateCaptured' % ns.MODS)
        if dateCaptured_element is not None:
            new_date_captured = dateCaptured()
            new_date_captured.load_xml(dateCaptured_element)
            self.dateCaptured = new_date_captured 
        dateCreated_element = origin_info_element.find('{%s}dateCreated' % ns.MODS)
        if dateCreated_element is not None:
            new_date_created = dateCreated()
            new_date_created.load_xml(dateCreated_element)
            self.dateCreated = new_date_created
        dateIssued_elements = origin_info_element.findall('{%s}dateIssued' % ns.MODS)
        for element in dateIssued_elements:
            new_date_issued = dateIssued()
            new_date_issued.load_xml(element)
            self.dateIssueds.append(new_date_issued)
        issuance_element = origin_info_element.find('{%s}issuance' % ns.MODS)
        if issuance_element is not None:
            self.issuance = issuance_element.text
        place_elements = origin_info_element.findall('{%s}place' % ns.MODS)
        for element in place_elements:
            new_place = place()
            new_place.load_xml(element)
            self.places.append(new_place)
        publishers = origin_info_element.findall('{%s}publisher' % ns.MODS)
        for element in publishers:
            new_publisher = publisher()
            new_publisher.load_xml(element)
            self.publishers.append(new_publisher)
        self.save()
        

class part(models.Model):
    """
    part MODS element in Redis datastore
    """
    dates = models.ListField(date)
    details = models.ListField(detail)
    extents = models.ListField(extent)
    mods_ID = models.Attribute()
    mods_type = models.Attribute()
    

    def load_xml(self,
                 part_element):
        """
        Method takes MODS xml element and updates values in Redis
        datastore
        
        :param part_element: part MODS element
        """
        set_attributes(part_element,self)
        date_elements  = part_element.findall('{%s}date' % ns.MODS)
        for element in date_elements:
            new_date = date()
            new_date.load_xml(element)
            self.dates.append(new_date)
        detail_elements = part_element.findall('{%s}detail' % ns.MODS)
        for element in detail_elements:
            new_detail = detail()
            new_detail.load_xml(element)
            self.details.append(new_detail)
        extent_elements = part_element.findall('{%s}extent' % ns.MODS)
        for element in extent_elements:
            new_extent = extent()
            new_extent.load_xml(element)
            self.extents.append(new_extent)   
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
        
class geographic(baseMODS):
    """
    geographic MOCS element in Redis datastore
    """
    authority = models.Attribute()
    authorityURI = models.Attribute()
    value_of = models.Attribute()
    valueURI = models.Attribute()
    
    def load_xml(self,
                 geographic_element):
        """
        Method takes MODS xml and updates values in Redis datastore
        based on XML values
        
        :param geographic_element: geographic XML element
        """
        set_attributes(geographic_element,self)
        self.value_of = geographic_element.text
        self.save()
        
class temporal(baseMODS):
    """
    temporal MOCS element in Redis datastore
    """
    authority = models.Attribute()
    authorityURI = models.Attribute()
    value_of = models.Attribute()
    valueURI = models.Attribute()
    
    def load_xml(self,
                 temporal_element):
        """
        Method takes MODS xml and updates values in Redis datastore
        based on XML values
        
        :param temporal_element: temporal XML element
        """
        set_attributes(temporal_element,self)
        self.value_of = temporal_element.text
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
    genres = models.ListField(genre)
    geographics = models.ListField(geographic)
    mods_ID = models.Attribute()
    names = models.ListField(name)
    usage = models.Attribute()
    temporals = models.ListField(temporal)
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
        genre_elements = subject_element.findall('{%s}genre' % ns.MODS)
        for element in genre_elements:
            new_genre = genre()
            new_genre.load_xml(element)
            self.genres.append(new_genre)
        geographic_elements = subject_element.findall('{%s}geographic' % ns.MODS)
        for element in geographic_elements:
            new_geographic = geographic()
            new_geographic.load_xml(element)
            self.geographics.append(new_geographic)
        name_elements = subject_element.findall('{%s}name' % ns.MODS)
        for element in name_elements:
            new_name = name()
            new_name.load_xml(element)
            self.names.append(new_name)
        temporal_elements = subject_element.findall('{%s}temporal' % ns.MODS)
        for element in temporal_elements:
            new_temporal = temporal()
            new_temporal.load_xml(element)
            self.temporals.append(new_temporal)
        topic_elements = subject_element.findall('{%s}topic' % ns.MODS)
        for element in topic_elements:
            new_topic = topic()
            new_topic.load_xml(element)
            self.topics.append(new_topic)
        self.save()
        
        
class subTitle(baseMODS):
    """
    subtitle MODS element in Redis datastore
    """
    value_of = models.Attribute()
    
    def load_xml(self,
                 subtitle_element):
        """
        Method takes MODS xml and updates values in Redis datastore
        based on XML values
        
        :param subtitle_element: subTitle XML element
        """
        set_attributes(subtitle_element,self)
        self.value_of = subtitle_element.text
        self.save()
        

class tableOfContents(baseMODS):
    """
    tableOfContents MODS element in Redis datastore
    """
    displayLabel = models.Attribute()
    mods_type = models.Attribute()
    xlink = models.Attribute()
    xml_lang = models.Attribute()

    def load_xml(self,
                 toc_element):
        """
        Method takes MODS xml and updates values in Redis datastore
        based on XML values
        
        :param subtitle_element: title XML element
        """
        set_attributes(toc_element,self)
        self.value_of = toc_element.text
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
    nonSort = models.Attribute()
    partName = models.Attribute()
    subTitles = models.ListField(subTitle)
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
        nonsort_element = title_info_element.find('{%s}nonSort' % ns.MODS)
        if nonsort_element is not None:
            self.nonSort = nonsort_element.text
        partname_element = title_info_element.find('{%s}partName' % ns.MODS)
        if partname_element is not None:
            self.partName = partname_element.text
        subTitles = title_info_element.findall('{%s}subTitle' % ns.MODS)
        for element in subTitles:
            new_subTitle = subTitle()
            new_subTitle.load_xml(element)
            self.subTitles.append(new_subTitle)
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

class recordChangeDate(baseMODSDate):
    """
    recordChangeDate MODS element in Redis datastore
    """
    value_of = models.Attribute()

    def load_xml(self,
                 record_change_date_element):
        """
        Method takes MODS xml and updates values in Redis datastore
        based on XML values
        
        :param record_change_date_element: recordChangeDate XML element
        """
        set_attributes(record_change_date_element,self)
        self.value_of = record_change_date_element.text
        self.save()

class recordContentSource(models.Model):
    """
    recordContentSource MODS element in Redis datastore
    """
    authority = models.Attribute()
    value_of  = models.Attribute()

    def load_xml(self,
                 record_content_element):
        """
        Method takes MODS xml and updates values in Redis datastore
        based on XML values
        
        :param record_content_element: recordContent XML element
        """
        set_attributes(record_content_element,self)
        self.value_of = record_content_element.text
        self.save()

class recordCreationDate(baseMODSDate):
    """
    recordCreationDate MODS element in Redis datastore
    """
    value_of = models.Attribute()

    def load_xml(self,
                 record_creation_date_element):
        """
        Method takes MODS xml and updates values in Redis datastore
        based on XML values
        
        :param record_creation_date_element: recordCreationDate XML element
        """
        set_attributes(record_creation_date_element,self)
        self.value_of = record_creation_date_element.text
        self.save()

class recordIdentifier(models.Model):
    """
    recordIdentifier MODS element in Redis datastore
    """
    identifier = models.Attribute()
    value_of  = models.Attribute()

    def load_xml(self,
                 record_identifier_element):
        """
        Method takes MODS xml and updates values in Redis datastore
        based on XML values
        
        :param record_content_element: recordIdentifier XML element
        """
        set_attributes(record_identifier_element,self)
        self.value_of = record_identifier_element.text
        self.save()        

class recordInfo(baseMODS):
    """
    recordInfo MODS element in Redis datastore
    """
    recordContentSources = models.ListField(recordContentSource)
    recordCreationDate = models.ReferenceField(recordCreationDate)
    recordChangeDates = models.ListField(recordChangeDate)
    recordIdentifiers = models.ListField(recordIdentifier)

    def load_xml(self,
                 record_info_element):
        """
        Method takes MODS xml and updates values in Redis datastore
        based on XML values
        
        :param record_info_element: recordInfo XML element
        """
        set_attributes(record_info_element,self)
        rec_content_source_elements = record_info_element.findall('{%s}recordContentSource' % ns.MODS)
        for element in rec_content_source_elements:
            new_rec_content = recordContentSource()
            new_rec_content.load_xml(new_rec_content)
            self.recordContentSources.append(new_rec_content)
        rec_creation_element = record_info_element.find('{%s}recordCreationDate' % ns.MODS)
        if rec_creation_element is not None:
            new_rec_creation = recordCreationDate()
            new_rec_creation.load_xml(rec_creation_element)
            self.recordCreationDate = new_rec_creation
        rec_change_dates = record_info_element.findall('{%s}recordChangeDate' % ns.MODS)
        for element in rec_change_dates:
            new_change_date = recordChangeDate()
            new_change_date.load_xml(element)
            self.recordChangeDates.append(new_change_date)
        rec_identifiers = record_info_element.findall('{%s}recordIdentifier' % ns.MODS)
        for element in rec_identifiers:
            new_identifier = recordIdentifier()
            new_identifier.load_xml(element)
            self.recordIdentifiers.append(element)
        self.save()
        

class relatedItem(baseMODS):
    """
    relatedItem MODS element in Redis datastore
    """
    mods_type = models.Attribute()
    names = models.ListField(name)
    originInfos= models.ListField(originInfo)
    parts = models.ListField(part)
    titleInfos = models.ListField(titleInfo)

    def load_xml(self,
                 related_item_element):
        """
        Method takes MODS xml and updates values in Redis datastore
        based on XML values
        
        :param related_item_element: relatedItem XML element
        """
        set_attributes(related_item_element,self)
        name_elements = related_item_element.findall('{%s}name' % ns.MODS)
        for element in name_elements:
            new_name = name()
            new_name.load_xml(element)
            self.names.append(new_name)        
        origin_info_elements = related_item_element.findall('{%s}originInfo' % ns.MODS)
        for element in origin_info_elements:
            new_origin_info = originInfo()
            new_origin_info.load_xml(element)
            self.originInfos.append(new_origin_info)
        part_elements = related_item_element.findall('{%s}part' % ns.MODS)
        for element in part_elements:
            new_part = part()
            new_part.load_xml(element)
            self.parts.append(new_part)
        titleInfos = related_item_element.findall('{%s}titleInfo' % ns.MODS)
        for element in titleInfos:
            new_titleInfo = titleInfo()
            new_titleInfo.load_xml(element)
            self.titleInfos.append(new_titleInfo)
        self.save()
        
        


        
class mods(models.Model):
    """
     Root MODS element in Redis datastore
    """
    abstracts = models.ListField(abstract)
##    accessCondition
    classifications = models.ListField(classification)
##    extension
    genres = models.ListField(genre)
    identifiers = models.ListField(identifier)
    languages = models.ListField(language)
    locations = models.ListField(location)
    names = models.ListField(name)
    notes = models.ListField(note)
    originInfos= models.ListField(originInfo)
##    part
    physicalDescriptions = models.ListField(physicalDescription)
    recordInfo = models.ReferenceField(recordInfo)
    relatedItems = models.ListField(relatedItem)
    subjects = models.ListField(subject)
    tableOfContents = models.ListField(tableOfContents)
    targetAudiences = models.ListField(targetAudience)
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
        classification_elements = mods_xml.findall('{%s}classification' % ns.MODS)
        for element in classification_elements:
            new_classification = classification()
            new_classification.load_xml(element)
            self.classifications.append(new_classification)
        genre_elements = mods_xml.findall('{%s}genre' % ns.MODS)
        for element in genre_elements:
            new_genre = genre()
            new_genre.load_xml(element)
            self.genres.append(new_genre)
        identifier_elements = mods_xml.findall('{%s}identifier' % ns.MODS)
        language_elements = mods_xml.findall('{%s}language' % ns.MODS)
        for element in language_elements:
            new_language = language()
            new_language.load_xml(element)
            self.languages.append(new_language)
        for element in identifier_elements:
            new_identifier = identifier()
            new_identifier.load_xml(element)
            self.identifiers.append(new_identifier)
        location_elements = mods_xml.findall('{%s}location' % ns.MODS)
        for element in location_elements:
            new_location = location()
            new_location.load_xml(element)
            self.locations.append(new_location)
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
        origin_info_elements = mods_xml.findall('{%s}originInfo' % ns.MODS)
        for element in origin_info_elements:
            new_origin_info = originInfo()
            new_origin_info.load_xml(element)
            self.originInfos.append(new_origin_info)
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
        relatedItems = mods_xml.findall('{%s}relatedItem' % ns.MODS)
        for element in relatedItems:
            new_relatedItem = relatedItem()
            new_relatedItem.load_xml(element)
            self.relatedItems.append(new_relatedItem)
        targetAudiences = mods_xml.findall('{%s}targetAudience' % ns.MODS)
        for element in targetAudiences:
            new_target_audience = targetAudience()
            new_target_audience.load_xml(element)
            self.targetAudiences.append(new_target_audience)
        titleInfos = mods_xml.findall('{%s}titleInfo' % ns.MODS)
        toc_elements = mods_xml.findall('{%s}tableOfContents' % ns.MODS)
        for element in toc_elements:
            new_toc = tableOfContents()
            new_toc.load_xml(element)
            self.tableOfContents.append(new_toc)
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
