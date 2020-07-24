#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

file = sys.argv[1]

if len(sys.argv) < 2:
    print("you need to give a second file name")
    sys.exit()

cpu.load(file)

cpu.run()
