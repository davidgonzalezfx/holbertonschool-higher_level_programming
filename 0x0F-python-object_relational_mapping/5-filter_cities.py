#!/usr/bin/python3
'''
script that takes in the name of a state as an argument and lists all cities
'''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost')

    cursor = db.cursor()
    cursor.execute(
        'SELECT cities.name FROM cities INNER JOIN states ON \
        cities.state_id = states.id WHERE states.name = %s \
        ORDER BY cities.id', (argv[4], ))

    states = cursor.fetchall()
    for state in states:
        print(", ".join(state[1]))

    cursor.close()
    db.close()
