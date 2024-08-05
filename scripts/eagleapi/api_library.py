import requests

from . import api_util

def switch(librarypath, server_url="http://localhost", port=41595, timeout_connect=3, timeout_read=10):
    """EAGLE API:/api/library/switch

    Method: POST

    Returns:
        Response: return of requests.post
    """
    API_URL = f"{server_url}:{port}/api/library/switch"

    def _init_data(librarypath):
        _data = {}
        if librarypath and librarypath != "":
            _data.update({"libraryPath": librarypath})
        return _data
    data = _init_data(librarypath)

    r_post = requests.post(API_URL, json=data, timeout=(timeout_connect, timeout_read))

    return r_post
