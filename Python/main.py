from xml.dom.minidom import parse
import xml.dom.minidom
import os

import parser
reload(parser)


def main(app_name):
    app_path = os.path.join(os.path.curdir, app_name)
    xml_path = os.path.join(app_path, 'view.xml')

    parser.parse_xml(xml_path)

main('test')
