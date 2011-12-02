"""
 :mod:`marc2skos` MARC to SKOS converts MARCtoFRBR csv file to skos RDF files
 for each FRBR entity.
"""
__author__ = 'Jeremy Nelson'

import urllib2,re,sys
from lxml import etree

import __init__
import common
import namespaces as ns

LOC_MARC_FUNC_CSV = 'http://www.loc.gov/marc/marc-functional-analysis/source/FRBR_Web_Copy.txt'

# Regular expressions used for entity searching
EXPRESSION_RE = re.compile(r"[E|e]xpression*")
ITEM_RE = re.compile(r"[I|i]em*")
MANIFESTATION_RE = re.compile(r"[M|m]anifestation*")
WORK_RE = re.compile(r"[W|w]ork*")
FIXED_POS_RE = re.compile(r"(\d+)-(\d+)")
ROLE_RE = re.compile(r"[\[]*(\w+)[\*|\]|\+]")
DISTRIB_RE = re.compile(r"(distrib.)")


def create_concept(parent_element,**kwargs):
    """
    Function takes a parent element and a dict of values
    to create a skos:Concept element

    :param parent_element: Parent element, either rdf:RDF or skos:Collection
    :param kwargs: Dictionary of keys-values
    """
    skos_concept = etree.SubElement(parent_element,
                                    '{%s}Concept' % ns.SKOS)
    skos_concept.set("{%s}lang" % ns.XML,
                     'en')
    if kwargs.has_key('about'):
        skos_concept.set("{%s}about" % ns.RDF,
                         kwargs.get('about'))
    if kwargs.has_key("scheme"):
        skos_scheme = etree.SubElement(skos_concept,
                                       "{%s}inScheme" % ns.SKOS)
        skos_scheme.set('{%s}resource'  % ns.RDF,
                        kwargs.get("scheme"))
    attrib = {"{%s}about" % ns.RDFS : kwargs.get("marc-tag"),
              '{%s}lang' % ns.XML : 'en'}
    marc_close_match = etree.SubElement(skos_concept,
                                        "{%s}closeMatch" % ns.SKOS,
                                        **attrib)
    if kwargs.has_key('fixed'):
        create_fixed(marc_close_match,
                     kwargs.get('fixed'))
    if kwargs.has_key('subfield'):
        create_subfield(marc_close_match,
                        kwargs.get('subfield'))

            
                
                
def create_fixed(parent,fixed):
    """
    Function checks for fixed field and if valid creates an
    SKOS elements for each position in an OrderedList

    :param parent: Parent element
    :param fixed: Fixed position value, may include range notation
                  in format of xx-xx
    """
    if fixed != 'n/a' and len(fixed) > 0:
        
        label = etree.SubElement(parent,
                                 '{%s}prefLabel' % ns.SKOS,
                                 **{'{%s}lang' % ns.XML : 'en'})
        label.text = 'fixed'
        collection = etree.SubElement(parent,
                                      '{%s}OrderedCollection' % ns.SKOS)
        multiple_positions = FIXED_POS_RE.search(fixed)
        if multiple_positions is not None:
            range_values = multiple_positions.groups()
            for value in range(int(range_values[0]),
                               int(range_values[-1])):
                member = etree.SubElement(collection,
                                          '{%s}member' % ns.SKOS)
                member.text = u"%s" % value
        else:
            member = etree.SubElement(collection,
                                      '{%s}member' % ns.SKOS)
            member.text = fixed
        
                                        

def create_skos(marc_mappings,entity,spec='frbr'):
    """
    Function takes a list of MARC fields and a FRBR or FRAD entity
    and creates a SKOS Concept Scheme relating Fixed and Variable
    values to the entity's roles

    :param marc_mappings: List of MARC21 to FRBR entity mapping
    :param entity: FRBR or FRAD entity name
    :param spec: Specification of entity, FRBR, FRAD, FRBRoo, etc. default is
                 'frbr'
    :rtype lxml.Element:
    """
    nsmap = {'rdf' : ns.RDF,
             'rdfs': ns.RDFS,
             'skos': ns.SKOS}
    rdf_xml = etree.Element("{%s}RDF" % ns.RDF,
                            nsmap=nsmap)
    scheme = "marc2skos-%s-%s.rdf" % (spec.lower(),
                                      entity.lower())
    description = etree.SubElement(rdf_xml,"{%s}Description" % ns.RDF,
                                   **{'{%s}lang' % ns.XML : 'en'})
    description.set("{%s}about" % ns.RDF,
                    scheme)
    for row in marc_mappings:
        marc_map = get_marc_map(row)
        create_concept(rdf_xml,**{'about':"MARC %s to %s %s'%s mapping" % (marc_map['marc-tag'],
                                                                           spec.upper(),
                                                                           entity,
                                                                           marc_map['entity-role']),
                                  'marc-tag':marc_map['marc-tag'][0:3],
                                  'scheme':scheme})
    return rdf_xml

def create_subfield(parent,subfield):
    """
    Function creates a MARC subfield SKOS elements for mapping

    :param parent: Parent element
    :param subfield: MARC field subfield value
    """
    if subfield != 'n/a' and len(subfield) > 0:
        label = etree.SubElement(parent,
                                 '{%s}prefLabel' % ns.SKOS,
                                 **{'{%s}lang' % ns.XML : 'en'})
        label.text = 'subfield'
        notation = etree.SubElement(parent,
                                    '{%s}notation' % ns.SKOS,
                                    **{'{%s}lang' % ns.XML : 'en'})
        notation.text = subfield
    
    
def get_marc_map(row):
    """
    Function takes a row generated from csv file and returns
    a dict.

    :param row: List of MARC21 to entity and role mapping
    :rtype dict:
    """
    return {'indicator-flag':bool(row[0]),
            'marc-tag':row[3],
            'field-name':row[4],
            'subfield':row[5],
            'position':row[6],
            'data element':row[7],
            'additional-info':row[8],
            'entity-role':normalize_role(row[10])}
            
                
def normalize_role(role):
    """
    Takes an FRBR or FRAD attribute or relationship and normalizes text to
    standard role in datastore.

    :param role: Raw role from mapping csv
    :rtype string: Returns a normalized version of the entity's role
    """
    role_regex = ROLE_RE.search(role)
    if role_regex is not None:
        role = role_regex.groups()[0]
    role = role.lower()
    distrib_regex = DISTRIB_RE.search(role)
    if distrib_regex is not None:
        role = DISTRIB_RE.sub('distribution',role)
    return role
        
    

if __name__ == '__main__':
    print("Starting marc2skos utility")
    marc_to_frbr = urllib2.urlopen(LOC_MARC_FUNC_CSV).read().split("\n")
    expr_lst,item_lst,manf_lst,work_lst = [],[],[],[]
    for i,row in enumerate(marc_to_frbr):
        row = row.replace('"','')
        rec = row.split(",")
        if len(rec) < 5:
            break
        entity = rec[9]
        if EXPRESSION_RE.search(entity):
            expr_lst.append(rec)
        if ITEM_RE.search(entity):
            item_lst.append(rec)
        if MANIFESTATION_RE.search(entity):
            manf_lst.append(rec)
        if WORK_RE.search(entity):
            work_lst.append(rec)
        if i%100:
            sys.stderr.write(str("."))
        else:
            sys.stderr.write(i)
    print("Creating SKOS for entities")
    work_skos = create_skos(work_lst,'Work')
    print etree.tostring(work_skos)
    
                                
    
    
        
    
    

