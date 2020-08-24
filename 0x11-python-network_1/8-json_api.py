#!/usr/bin/python3
''' Search API '''
import requests
import sys


if __name__ == '__main__':
    data = {'q': ''}

    try:
        data['q'] = sys.argv[1]
    except:
        pass

    res = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        jsonify = res.json()
        if not jsonify:
            print('No result')
        else:
            print('[{}] {}'.format(jsonify.get('id'), jsonify.get('name')))
    except:
        print('Not a valid JSON')
