import requests
from tomorrow import threads


class Get:
    def __init__(self, url, param=None, special=None, after_complete=None):
        self.url = url
        self.param = {} if param is None else param
        self.special = special
        self.result = ""
        self.completed = False
        self.thread = None
        self.after_complete_param = after_complete

    def after_completed(self):
        pass

    @threads(5, timeout=30)
    def get(self):
        if self.special is None:
            self.result = requests.get(self.url, params=self.param, timeout=10).text
        elif self.special == 'json':
            self.result = requests.get(self.url, params=self.param).json()
        elif self.special == 'binary':
            self.result = requests.get(self.url, params=self.param).content
        else:
            self.result = 'Cannot detect mode ', self.special
        self.completed = True
        self.after_completed()


class Post:
    def __init__(self, url, param=None, special=None, after_complete=None):
        self.url = url
        self.param = {} if param is None else param
        self.special = special
        self.result = ""
        self.completed = False
        self.thread = None
        self.after_complete_param = after_complete

    def after_completed(self):
        pass

    @threads(5, timeout=30)
    def post(self):
        if self.special is None:
            self.result = requests.post(self.url, params=self.param).text
        elif self.special == 'json':
            self.result = requests.post(self.url, params=self.param).json()
        elif self.special == 'binary':
            self.result = requests.post(self.url, params=self.param).content
        else:
            self.result = 'Cannot detect mode ', self.special
        self.completed = True
        self.after_completed()
