#!/usr/bin/env python

import urllib2 as url2

def post(url, data):
    req = url2.Request(url, json.dumps(data))
    try:
        res = url2.urlopen(req)
    except url2.HTTPError, e:
        return e
    else:
        msg = res.read()
        return msg


def put(url, data):
    opener = url2.build_opener(url2.HTTPHandler)
    request = url2.Request(url, json.dumps(data))
    request.add_header('Content-Type', 'JSON')
    request.get_method = lambda: 'PUT'
    try:
        res = opener.open(request)
    except url2.HTTPError, e:
        return e
    else:
        msg = res.read()
        return msg
