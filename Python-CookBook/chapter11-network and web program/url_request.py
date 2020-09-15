# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from urllib import request, parse


url = 'http://httpbin.org/get'

parms = {
    'name1': 'value1',
    'name2': 'value2'
}

querystring = parse.urlencode(parms)

u = request.urlopen(url + '?' + querystring)

resp = u.read()

print(resp)