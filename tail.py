#!/usr/bin/env python3

"""
Usage:
	tail.py <lines> <filename>
"""

import sys

try:
    lines = int(sys.argv[1])
    file = sys.argv[2]
except:
    print(__doc__)
    sys.exit(1)

with open(file) as myfile:
    firstlines = myfile.readlines()[-lines:]
    print('--' + sys.argv[2] + '--')
    [print(x.strip()) for x in firstlines]
    myfile.close()
