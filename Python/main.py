from sys import stderr
from os.path import join, curdir
import parser
import viewer
import globals
reload(parser)
reload(viewer)


def main(app_name):
    app_path = join(curdir, app_name)
    xml_path = join(app_path, 'view.xml')

    views = parser.parse_xml(xml_path)
    try:
        globals.app = __import__(app_name + '.extensions', fromlist=[app_name])
    except ImportError as e:
        stderr.write(e.message + '\n')
        return

    main_window = viewer.Application(views[0], views[1])
    globals.views = main_window.extensions
    main_window.start(views[2])


main('test')
