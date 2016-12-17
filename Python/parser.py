from xml.dom.minidom import parse
from sys import stderr


class Extension:
    def __init__(self, exttype, name, position):
        self.type = exttype
        self.name = name
        self.position = [int(i) for i in position.split(',')]
        self.content = None

    def __repr__(self):
        return "%s(%s)" % (self.name, self.type)

    def __str__(self):
        return "%s(%s)" % (self.name, self.type)

    def set_content(self, content):
        self.content = content


class Framework:
    def __init__(self, name, type, sub_framework, sub_extension, params):
        self.name = name
        self.type = type
        self.subFramework = sub_framework
        self.subExtension = sub_extension
        self.params = [int(i) for i in str(params).split(',')]

    def __repr__(self):
        return "%s(%s)" % (self.name, self.type)

    def __str__(self):
        return "%s(%s)" % (self.name, self.type)


def getText(leaf):
    nodelist = leaf.childNodes
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)


def tag_exist(xml, tag, default):
    return str(xml.getElementsByTagName(tag)[0]) if len(xml.getElementsByTagName(tag)) == 1 else default


def specified_extension(ext, ext_type):
    if ext_type == 'button':
        return {
            'text': getText(ext.getElementsByTagName('text')[0]),
            'is_active': tag_exist(ext, 'is_active', 'true') == 'true'
        }
    if ext_type == 'label':
        return {
            'text': getText(ext.getElementsByTagName('text')[0]),
            'font_size': int(tag_exist(ext, 'font_size', 12))
        }
    if ext_type == 'text':
        return {
            'default': tag_exist(ext, 'default_text', ''),
            'font_size': int(tag_exist(ext, 'font_size', 12)),
            'is_active': tag_exist(ext, 'is_active', 'true') == 'true'
        }
    if ext_type == 'pic':
        return {
            'path': getText(ext.getElementsByTagName('path')[0])
        }


def walk(framework):
    raw_frameworks = framework.getElementsByTagName('framework')
    frameworks = []
    for frm in raw_frameworks:
        frameworks.append(walk(frm))
    raw_extensions = framework.getElementsByTagName('extension')
    extensions = []
    for ext in raw_extensions:
        #try:
        ext_ = Extension(exttype=str(ext.getAttribute('type')), name=str(ext.getAttribute('name')), position=getText(ext.getElementsByTagName('position')[0]))
        ext_.set_content(specified_extension(ext, ext_.type))
        #except Exception as e:
        #    stderr.write('XML file corrupted\n')
        #    return None
        extensions.append(ext_)
    return Framework(framework.getAttribute('name'), framework.getAttribute('type'), frameworks, extensions, framework.getAttribute('params'))


def parse_xml(xml_path):
    dom_tree = parse(xml_path)
    elements = dom_tree.documentElement
    if not elements.hasAttribute('appname') or not elements.hasAttribute('size'):
        raise Exception("XML file corrupted")
    title = elements.getAttribute('appname')
    size = str(elements.getAttribute('size')).split('X')

    raw_framework = elements.getElementsByTagName('framework')[0]
    main_framework = walk(raw_framework)

    return title, size, main_framework
