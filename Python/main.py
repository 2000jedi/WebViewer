from sys import stderr
from os.path import join, curdir
import parser
reload(parser)


def main(app_name):
    app_path = join(curdir, app_name)
    xml_path = join(app_path, 'view.xml')

    global views
    views = parser.parse_xml(xml_path)
    app = None

    try:
        app = __import__(app_name + '.extensions', fromlist=[app_name])
    except ImportError as e:
        stderr.write(e.message + '\n')
        return
    print app.functions


main('test')
