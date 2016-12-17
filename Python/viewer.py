import gtk
import globals


class Application(gtk.Window):

    def __init__(self, appname, size):
        super(Application, self).__init__()
        self.appname = appname
        self.size = size
        self.extensions = {}

    def get_view(self, str_type, params=[]):
        if str_type == 'fixed':
            return gtk.Fixed()
        elif str_type == 'alignment':
            return gtk.Alignment(params[0], params[1], params[2], params[3])
        elif str_type == 'table':
            return gtk.Table(params[0], params[1], True)
        elif str_type == 'button':
            return Button
        elif str_type == 'label':
            return Label
        elif str_type == 'text':
            return Text

    def parse_framework(self, parent, frm):
        self.extensions[frm.name] = self.get_view(frm.type, frm.params)
        for ext in frm.subExtension:
            self.extensions[ext.name] = self.get_view(ext.type)(ext)
            self.extensions[frm.name].attach(self.extensions[ext.name].widget, ext.position[0], ext.position[1], ext.position[2], ext.position[3])
        for view in frm.subFramework:
            self.parse_framework(self.extensions[frm.name].attach, view)
            # self.extensions[view.name] = self.get_view(view.type)()
        parent(self.extensions[frm.name])

    def start(self, main_framework):
        self.parse_framework(self.add, main_framework)
        self.set_size_request(int(self.size[0]), int(self.size[1]))
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title(self.appname)
        # self.set_icon_from_file(icon)
        self.connect("destroy", self.destroy)
        self.show_all()
        gtk.main()

    def destroy(self, widget):
        gtk.main_quit()


class Viewer(object):
    extension = None
    widget = None

    def __init__(self, extension):
        self.extension = extension

    def draw(self):
        self.widget.draw()


class Label(Viewer):
    def __init__(self, extension):
        super(Label, self).__init__(extension)
        self.widget = gtk.Label(self.extension.content['text'])

    def set_label(self, label):
        self.extension.content['text'] = label
        self.widget.set_text(label)

    def get_text(self):
        return self.extension.content['text']


class Button(Viewer):
    def __init__(self, extension):
        global app
        super(Button, self).__init__(extension)
        self.widget = gtk.Button(self.extension.content['text'])
        self.widget.connect("clicked", lambda widget: self.raw(self.extension, globals.app.functions[self.extension.name]['clicked']))

    def set_text(self, text):
        self.extension.content['text'] = text

    def get_text(self):
        return self.extension.content['text']

    def set_active(self, status):
        self.extension.content['is_active'] = status

    def raw(self, extension, func):
        func(extension, globals.views)


class Text(Viewer):
    def __init__(self, extension):
        super(Text, self).__init__(extension)
        # self.widget = gtk.