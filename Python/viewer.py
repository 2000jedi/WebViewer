import gtk
import globals


class Application(gtk.Window):

    def __init__(self, appname, size):
        gtk.gdk.threads_init()
        super(Application, self).__init__()
        self.appname = appname
        self.size = size
        self.extensions = {}

    def get_view(self, str_type, params=None):
        if str_type == 'alignment':
            return gtk.Alignment(params[0], params[1], params[2], params[3])
        elif str_type == 'table':
            return gtk.Table(params[0], params[1], True)
        elif str_type == 'button':
            return Button
        elif str_type == 'label':
            return Label
        elif str_type == 'text':
            return Text
        elif str_type == 'list':
            return List
        elif str_type == 'check':
            return CheckButton
        elif str_type == 'pic':
            return Image
        elif str_type == 'input':
            return Entry

    def parse_framework(self, parent, frm):
        self.extensions[frm.name] = self.get_view(frm.type, frm.params)
        for ext in frm.subExtension:
            self.extensions[ext.name] = self.get_view(ext.type)(ext)
            self.extensions[frm.name].attach(self.extensions[ext.name].widget, ext.position[0], ext.position[1], ext.position[2], ext.position[3])
        for view in frm.subFramework:
            self.parse_framework(self.extensions[frm.name].attach, view)
        parent(self.extensions[frm.name])

    def start(self, main_framework):
        self.parse_framework(self.add, main_framework)
        self.set_size_request(int(self.size[0]), int(self.size[1]))
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title(self.appname)
        # self.set_icon_from_file(icon)
        self.connect("destroy", self.destroy)
        self.show_all()
        gtk.threads_enter()
        gtk.main()
        gtk.threads_leave()

    def destroy(self, widget):
        gtk.main_quit()


class Viewer(object):
    extension = None
    widget = None

    def __init__(self, extension):
        self.extension = extension

    @staticmethod
    def raw(extension, func):
        func(extension, globals.views)


class Label(Viewer):
    def __init__(self, extension):
        super(Label, self).__init__(extension)
        self.widget = gtk.Label(self.extension.content['text'])

    def set_label(self, label):
        self.extension.content['text'] = label
        self.widget.set_text(label)

    def get_label(self):
        return self.extension.content['text']


class Button(Viewer):
    def __init__(self, extension):
        global app
        super(Button, self).__init__(extension)
        self.widget = gtk.Button(self.extension.content['text'])
        self.widget.connect("clicked", lambda widget: self.raw(self.extension, globals.app.functions[self.extension.name]['clicked']))

    def set_label(self, text):
        self.extension.content['text'] = text
        self.widget.set_label(text)

    def get_label(self):
        return self.extension.content['text']


class Text(Viewer):
    def __init__(self, extension):
        super(Text, self).__init__(extension)
        self.widget = gtk.Notebook()


class List(Viewer):
    def __init__(self, extension):
        super(List, self).__init__(extension)
        self.widget = gtk.List()


class CheckButton(Viewer):
    def __init__(self, extension):
        super(CheckButton, self).__init__(extension)
        self.widget = gtk.CheckButton()
        self.set_active(extension.content['active'])

    def set_active(self, active):
        self.widget.set_active(active)

    def get_active(self):
        return self.widget.get_active()


class ComboBox(Viewer):
    def __init__(self, extension):
        super(ComboBox, self).__init__(extension)
        self.widget = gtk.combo_box_entry_new_text()

    def add(self, text):
        self.widget.append_text(text)

    def get_selected(self):
        return self.widget.get_active_text()


class Image(Viewer):
    def __init__(self, extension):
        super(Image, self).__init__(extension)
        self.widget = gtk.Image()
        try:
            self.widget.set_from_file(extension.content['image'])
        except:
            pass

    def set_image(self, file_path):
        self.widget.set_from_file(file_path)


class Entry(Viewer):
    def __init__(self, extension):
        super(Entry, self).__init__(extension)
        self.widget = gtk.Entry()
        self.widget.add_events(gtk.gdk.KEY_RELEASE_MASK)
        self.widget.set_text(extension.content['default'])

    def set_text(self, text):
        self.widget.set_text(text)

    def get_text(self):
        return self.widget.get_text()
