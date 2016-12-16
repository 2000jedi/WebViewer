import gtk


class Viewer(object):
    subs = None
    extension = None
    widget = None

    def __init__(self, extension, subs):
        self.extension = extension
        self.subs = subs

    def draw(self):
        widget.draw()


class Label(Viewer):
    def __init__(self, extension, subs):
        super.__init__(extension, subs)
        widget = gtk
        widget

    def set_label(self, label):
        self.extension.content['label'] = label

    def get_text(self):
        return self.extension.content['label']

class Button(Viewer):
    def set_text(self, text):
        self.extension.content['text'] = text

    def get_text(self):
        return self.extension.content['text']

    def set_active(self, status):
        self.extension.content['is_active'] = status

    def onclick(self, func):
        global views
        func(self, views)

    def onpress(self, func):
        global views
        func(self, views)

    def onrelease(self, func):
        global views
        func(self, views)

