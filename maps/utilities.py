__author__ = 'Jeremy Nelson'
import os
import __init__
import lib.namespaces as ns
from lxml import etree

nsmap = {'marc': ns.MARC,
         'rdf' : ns.RDF,
         'rdfs': ns.RDFS,
         'skos': ns.SKOS}

rda_filename = '%s/fixures/RDAGroup1Elements.rdf' % os.curdir
rda_entities = open(rda_filename,'rb').read()
rda_rel = etree.XML(rda_entities)

def create_skeleton(entity_url):
    """
    Creates SKOS mapping skeleton for RDA Group 1 Elements
    """
    rdf_xml = etree.Element("{%s}RDF" % ns.RDF,
                            nsmap=nsmap)
    # Get all properties associated with entities
    rda_domains = rda_rel.findall('{%s}Description/{%s}domain[@{%s}resource="%s"]' % (ns.RDF,
                                                                                         ns.RDFS,
                                                                                         ns.RDF,
                                                                                         entity_url))
    for element in rda_domains:
        parent_desc = element.getparent()
        new_desc = etree.SubElement(rdf_xml,
                                    "{%s}Description" % ns.RDF)
        new_desc.set("{%s}about" % ns.RDF,
                     parent_desc.attrib['{%s}about' % ns.RDF])
        new_domain = etree.SubElement(new_desc,
                                      "{%s}domain" % ns.RDFS)
        new_domain.set("{%s}resource" % ns.RDF,
                       entity_url)
        old_label = parent_desc.find("{%s}label" % ns.RDFS)
        raw_label = old_label.text
        # Strip out entity name from label
        if raw_label.count("(") > 0:
            new_label_text = raw_label[:raw_label.index("(")].strip()
        else:
            new_label_text = raw_label.strip()
        new_label = etree.SubElement(new_desc,
                                     "{%s}label" % ns.RDFS)
        new_label.text = new_label_text
        new_collection = etree.SubElement(new_desc,
                                          "{%s}Collection" % ns.SKOS)
        
    return rdf_xml
        
    
    

def generate_skos_skeletons():
    print("Generating FRBR RDA Work")
    work_xml = create_skeleton("http://rdvocab.info/uri/schema/FRBRentitiesRDA/Work")
    work_fo = open('maps/frbr-rda-work-marc.rdf','wb')
    work_fo.write(etree.tostring(work_xml,
                                 encoding="utf-8",
                                 pretty_print=True,
                                 xml_declaration=True))
    work_fo.close()
    expression_xml = create_skeleton("http://rdvocab.info/uri/schema/FRBRentitiesRDA/Expression")
    expr_fo = open('maps/frbr-rda-expression-marc.rdf','wb')
    expr_fo.write(etree.tostring(expression_xml,
                                 encoding="utf-8",
                                 pretty_print=True,
                                 xml_declaration=True))
    expr_fo.close()
    manifestation_xml = create_skeleton("http://rdvocab.info/uri/schema/FRBRentitiesRDA/Manifestation")
    manf_fo = open('maps/frbr-rda-manifestation-marc.rdf','wb')
    manf_fo.write(etree.tostring(manifestation_xml,
                                 encoding="utf-8",
                                 pretty_print=True,
                                 xml_declaration=True))
    manf_fo.close()
    item_xml = create_skeleton("http://rdvocab.info/uri/schema/FRBRentitiesRDA/Item")
    item_fo = open('maps/frbr-rda-item-marc.rdf','wb')
    item_fo.write(etree.tostring(item_xml,
                                 encoding="utf-8",
                                 pretty_print=True,
                                 xml_declaration=True))
    item_fo.close()
    print("Finished")

if __name__ == '__main__':
    generate_skos_skeletons()
