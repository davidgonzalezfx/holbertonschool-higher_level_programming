#!/usr/bin/python3
''' Github API '''
from requests import get, auth
import sys


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    pwd = sys.argv[2]
    res = get(url, auth=auth.HTTPBasicAuth(user, pwd))
    print(res.json().get('id'))
