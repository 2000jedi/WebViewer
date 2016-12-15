import requests


def get(url, param={}, special=None):
    if special is None:
        return requests.get(url, params=param).text
    elif special == 'json':
        return requests.get(url, params=param).json()
    elif special == 'binary':
        return requests.get(url, params=param).content
    else:
        return 'Cannot detect mode ', special


def post(url, param={}, special=None):
    if special is None:
        return requests.post(url, params=param).text
    elif special == 'json':
        return requests.post(url, params=param).json()
    elif special == 'binary':
        return requests.post(url, params=param).content
    else:
        return 'Cannot detect mode ', special
