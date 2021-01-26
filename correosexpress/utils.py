# -*- coding: utf-8 -*-
import re
import json


def get_url(debug=False):
    if debug:
        return 'https://test.correosexpress.com/wspsc/apiRestGrabacionEnvio/json/grabacionEnvio'
    else:
        return 'https://www.cexpr.es/wspsc/apiRestGrabacionEnviok8s/json/grabacionEnvio'


def get_json_from_string(string):
    json_string = re.search("{(.*?)}$", string).group(0)
    return json.loads(json.dumps(json_string))
