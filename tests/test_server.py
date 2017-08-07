#!/usr/local/bin/python

import httplib


PASS = '\033[92m'
FAIL = '\033[91m'
END = '\033[0m'


def test_server():
    try:
        hh = None
        connection = httplib.HTTPConnection
        hh = connection('0.0.0.0', '8080')
        hh.request('GET', '')
        if hh.getresponse().getheaders():
            hh.close()
            return True
        raise Exception
    except httplib.socket.error:
        return False


assert test_server()
