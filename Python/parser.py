from xml.dom.minidom import parse
import xml.dom.minidom


class extension:

    def __init__(self, exttype, name, position, parent_viewer):
        self.type = exttype
        self.name = name
        self.position = position if position != 'auto' else None
        self.parent_viewer = parent_viewer if parent_viewer != 'main' else None

    def __repr__(self):
        return "%s(%s)" % (self.name, self.type)

    def __str__(self):
        return "%s(%s)" % (self.name, self.type)

    def setcontent(self, content):
        self.content = content


def parse_xml(xml_path):
    DOMTree = parse(xml_path)
    elements = DOMTree.documentElement
    if not elements.hasAttribute('appname'):
        raise Exception("XML file corrupted")

    title = elements.getAttribute('appname')
    print title
    exts = elements.getElementsByTagName('extension')
    extensions = []
    for ext in exts:
        if not ext.hasAttribute('type') or not ext.hasAttribute('name'):
            raise Exception("XML file corrupted")
        content = {}
        ext_ = extension(exttype=ext.getAttribute('type'), name=ext.getAttribute('name'), position=ext.getElementsByTagName('position')[0], parent_viewer=ext.getElementsByTagName('parent_viewer')[0])
        if (ext_.type == 'button'):
            content['text'] = ext.getElementsByTagName('text')[0]
            try:
                content['is_active'] = ext.getElementsByTagName('is_active')[0]
            except:
                content['is_active'] =True

        ext_.setcontent(content)
        extensions.append(ext_)
    print extensions
