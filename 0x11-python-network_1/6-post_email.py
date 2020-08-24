#!/usr/bin/python3
''' POST request to the passed URL with the email '''
import requests
import sys

if __name__ == '__main__':
    r = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(r.text)
