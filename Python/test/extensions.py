from Python import web


def testbutton_onclick(extension, views):
    class get_(web.Get):
        def after_completed(self):
            self.after_complete_param.set_label(self.result)

    display = views['display']
    get_('http://www.bilibili.com/', after_complete=display).get()


functions = {
    'testbutton': {'clicked': testbutton_onclick}
}
