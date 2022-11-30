#!/usr/bin/python3
def uppercase(str):
    ch2 = ''
    for ch in str:
        if ord(ch) in range(97, 123):
            ch2 += chr(ord(ch) - 32)
        else:
            ch2 += ch
    print("{}".format(ch2))
