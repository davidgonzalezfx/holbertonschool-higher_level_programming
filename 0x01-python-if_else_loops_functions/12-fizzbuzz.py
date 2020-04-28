#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i != 1):
            print(' ', end='')
        if (i % 3 == 0):
            print('Fizz', end='')
        if (i % 5 == 0):
            print('Buzz', end='')
        if(not((i % 5 == 0) or (i % 3 == 0))):
            print('{}'.format(i), end='')
