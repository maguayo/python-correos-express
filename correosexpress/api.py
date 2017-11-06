# -*- coding: utf-8 -*-
from correosexpress.utils import get_url
import requests
from requests.auth import HTTPBasicAuth


class API(object):
    __slots__ = (
        'url',
        'username',
        'password',
    )

    def __init__(self, username, password, debug=False):
        self.url = get_url(debug)
        self.username = username
        self.password = password

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def connect(self, data):
        headers = {'Content-type': 'application/json'}
        return requests.post(
            self.url, data=data,
            auth=HTTPBasicAuth(self.username, self.password),
            headers=headers, verify=False)

    def test_connection(self):
        headers = {'Content-type': 'application/json'}
        resp = requests.post(
            self.url, data='',
            auth=HTTPBasicAuth(self.username, self.password),
            headers=headers, verify=False)
        if resp.status_code == 200:
            return 'OK'
        else:
            return resp.text
