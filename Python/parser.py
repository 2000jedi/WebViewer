from xml.dom.minidom import parse
from sys import stderr


class Extension:

    def __init__(self, exttype, name, position, parent_viewer):
        self.type = exttype
        self.name = name
        self.position = position if position != 'auto' else None
        self.parent_viewer = parent_viewer if parent_viewer != 'main' else None
        self.content = None

    def __repr__(self):
        return "%s(%s)" % (self.name, self.type)

    def __str__(self):
        return "%s(%s)" % (self.name, self.type)

    def set_content(self, content):
        self.content = content


def tag_exist(xml, tag, default):
    return str(xml.getElementsByTagName(tag)[0]) if len(xml.getElementsByTagName(tag)) == 1 else default


def specified_extension(ext, ext_type):
    if ext_type == 'button':
        return {
            'text': str(ext.getElementsByTagName('text')[0]),
            'is_active': tag_exist(ext, 'is_active', 'true') == 'true'
        }
    if ext_type == 'label':
        return {
            'text': str(ext.getElementsByTagName('text')[0]),
            'font_size': int(tag_exist(ext, 'font_size', 12))
        }
    if ext_type == 'text':
        return {
            'default': tag_exist(ext, 'default_text', ''),
            'font_size': int(tag_exist(ext, 'font_size', 12))
        }
    if ext_type == 'pic':
        return {
            'path': str(ext.getElementsByTagName('path')[0])
        }


def parse_position(position):
    position = str(position)
    if position == 'auto':
        return None
    return position.split('\|')


def parse_xml(xml_path):
    dom_tree = parse(xml_path)
    elements = dom_tree.documentElement
    if not elements.hasAttribute('appname'):
        raise Exception("XML file corrupted")

    title = elements.getAttribute('appname')
    extensions = []
    for ext in elements.getElementsByTagName('extension'):
        try:
            ext_ = Extension(exttype=str(ext.getAttribute('type')), name=str(ext.getAttribute('name')), position=parse_position(ext.getElementsByTagName('position')[0]), parent_viewer=str(ext.getElementsByTagName('parent_viewer')[0]))
            ext_.set_content(specified_extension(ext, ext_.type))
        except:
            stderr.write('XML file corrupted\n')
            return None
        extensions.append(ext_)
    return title, extensions
