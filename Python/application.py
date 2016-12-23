import gtk
import viewer
reload(viewer)


class Application(gtk.Window):
    def __init__(self, appname, size):
        gtk.gdk.threads_init()
        super(Application, self).__init__()
        self.appname = appname
        self.size = size
        self.extensions = {}

    def parse_framework(self, parent, frm):
        self.extensions[frm.name] = viewer.get_view[frm.type](frm)
        for ext in frm.subExtension:
            self.extensions[ext.name] = viewer.get_view[ext.type](ext)
            self.extensions[frm.name].attach(self.extensions[ext.name].widget, ext)
        for view in frm.subFramework:
            self.parse_framework(self.extensions[frm.name], view)
        parent.attach(self.extensions[frm.name], frm)

    def attach(self, widget, extension):
        self.add(widget)

    def start(self, main_framework):
        self.parse_framework(self, main_framework)
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
