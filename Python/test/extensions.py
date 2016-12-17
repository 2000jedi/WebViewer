import web
import file


def testbutton_onclick(extension, views):
    display = views['display']
    # display.set_label(web.get('https://github.com/2000jedi/SAM.git'))
    display.set_label('Hi')


functions = {
    'testbutton': {'clicked': testbutton_onclick}
}
