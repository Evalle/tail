#!/usr/bin/env python3

"""
Usage:
    head.py <lines> <filename>
"""

import sys

try:
    lines = int(sys.argv[1])
    filename = sys.argv[2]
except:
    print(__doc__)
    sys.exit(1)

with open(filename) as myfile:
    firstlines = myfile.readlines()[:lines]
    [print(x.strip()) for x in firstlines]
    myfile.close()
