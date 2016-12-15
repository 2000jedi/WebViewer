import web
import file


def testbutton_onclick(extension, views):
    display = views.getview('main').getextension('display')
    display.set_label(web.get('https://github.com/2000jedi/SAM.git'))


functions = [
    ('testbutton', 'onclick', testbutton_onclick)
]
