"""
 :mod:`rda_toolkit_mapper` Uses RDA Toolkit Mappings to create SKOS files for
 MARC and MODS imports into FRBR-Redis datastore.
"""
__author__ = 'Jeremy Nelson'

import sys,datetime,os
from BeautifulSoup import BeautifulSoup
from lxml import etree
import __init__
print(__init__.LIB_ROOT)
import lib.namespaces as ns

def create_rda_toolkit_skos(raw_html_filename):
    full_path = os.path.join(FIXURES,raw_html_filename)
    raw_html_file = open(full_path,'rb')
    raw_html = raw_html_file.read()
    raw_html_file.close()
    html_soup = BeautifulSoup(raw_html)
    


if __name__ == '__main__':
    rda_marc_bib_html = 'rda-marc-bibliographic-mapping.html'
    create_rda_toolkit_skos(rda_marc_bib_html)
