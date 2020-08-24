#!/usr/bin/python3
''' Github commits '''
from requests import get, auth
import sys


if __name__ == '__main__':
    try:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
        res = get(url)
        jsonify = res.json()
        for i in range(0, 10):
            print('{}: {}'.format(jsonify[i].get('sha'), jsonify[i].get(
                'commit').get('author').get('name')))
    except:
        pass
