#!/usr/bin/python3
''' POST request to the passed URL with the email '''
from urllib import request, parse
import sys


if __name__ == '__main__':
    data = parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
