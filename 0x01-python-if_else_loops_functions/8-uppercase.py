#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        word = ord(str[i])
        if (word >= 97 and word <= 122):
            word -= 32
        print("{:c}".format(word), end="")
    print()
