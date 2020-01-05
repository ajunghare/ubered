
import requests

def do_get(URL,PARAMS=None):
    if PARAMS:
        r = requests.get(url=URL, params=PARAMS)
    else:
        r = requests.get(url=URL)
    return r.json()
