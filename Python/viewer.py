import gtk
import globals


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


class Alignment(Viewer):
    def __init__(self, extension):
        super(Table, self).__init__(extension)
        self.widget = gtk.Table(extension.params[0], extension.params[1], extension.params[2], extension.params[3])

    def attach(self, widget, extension):
        self.widget.attach(widget, extension.position[0], extension.position[1], extension.position[2], extension.position[3])


class Table(Viewer):
    def __init__(self, extension):
        super(Table, self).__init__(extension)
        self.widget = gtk.Table(extension.position[0], extension.position[1], True)

    def attach(self, widget, extension):
        self.widget.attach(widget, extension.position[0], extension.position[1], extension.position[2], extension.position[3])


class Fixed(Viewer):
    def __init__(self, extension):
        super(Fixed, self).__init__(extension)
        self.widget = gtk.Fixed()

    def attach(self, widget, extension):
        self.widget.put(widget, extension.position[0], extension.position[1])


get_view = {
    'alignment': Alignment,
    'table': Table,
    'fixed': Fixed,
    'button': Button,
    'label': Label,
    'text': Text,
    'list': List,
    'check': CheckButton,
    'pic': Image,
    'input': Entry
}
