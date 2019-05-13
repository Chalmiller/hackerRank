#!/bin/python

from __future__ import print_function

import os
import sys


def findPoint(px, py, qx, qy):
    rpx = 2*qx - px
    rpy = 2*qy - py

    if (qx == 0 and qy == 0):
        rpx = -1*px
        rpy = -1*py
        return rpx, rpy
    else:
        return rpx, rpy


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    for n_itr in xrange(n):
        pxPyQxQy = raw_input().split()

        px = int(pxPyQxQy[0])

        py = int(pxPyQxQy[1])

        qx = int(pxPyQxQy[2])

        qy = int(pxPyQxQy[3])

        result = findPoint(px, py, qx, qy)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
