from xml.dom.minidom import parse
import xml.dom.minidom
import os

def parse_xml(xml_path):
    DOMTree = parse(xml_path)
    elements = DOMTree.documentElement
    title = elements.getAttribute('appname')
    print title
    exts = elements.getElementsByTagName('extension')
    for ext in exts:
        print ext.getAttribute('type')

