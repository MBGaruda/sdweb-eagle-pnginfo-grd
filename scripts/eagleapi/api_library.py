import requests
import time

from . import api_util

def switch(librarypath, server_url="http://localhost", port=41595, timeout_connect=3, timeout_read=10):
    """EAGLE API:/api/library/switch

    Method: POST
    """
    API_URL = f"{server_url}:{port}/api/library/switch"

    def _init_data(librarypath):
        _data = {}
        if librarypath and librarypath != "":
            _data.update({"libraryPath": librarypath})
        return _data
    data = _init_data(librarypath)

    r_post = requests.post(API_URL, json=data, timeout=(timeout_connect, timeout_read))

    _post = r_post.json()

    if "status" in _post and _post["status"] == "success":

        for cnt in range(10):
            r_get = info(server_url, port, timeout_connect, timeout_read)

            _get = r_get.json()

            if "status" in _get and _get["status"] == "success":
                if _get["data"]["library"]["path"] == librarypath:
                    break
                time.sleep(0.2)

    return r_post

def info(server_url="http://localhost", port=41595, timeout_connect=3, timeout_read=10):
    """EAGLE API:/api/library/info

    Method: GET
    """

    API_URL = f"{server_url}:{port}/api/library/info"

    r_get = requests.get(API_URL, timeout=(timeout_connect, timeout_read))

    return r_get
