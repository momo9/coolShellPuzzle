#!/usr/bin/python

import sys

LUT_NAME = 'lut.txt'


def genLut():
    fd = open(LUT_NAME)
    ret = []
    for line in fd:
        ret.append(line.strip('\n'))
    fd.close()
    return ret


def transfer(c, lut):
    if ord('a') <= ord(c) <= ord('z'):
        i = lut.index(c)
        c = chr(ord('a') + i)
    return c


def transContent(content, lut):
    return ''.join(map(lambda x: transfer(x, lut), content))


def getContent(fileName, lut):
    fd = open(fileName)
    content = fd.read()
    fd.close()
    return transContent(content, lut)


if __name__ == "__main__":
    lut = genLut()
    fileName = sys.argv[1]
    print getContent(fileName, lut)
