#!/usr/bin/env python3

"""Main."""

import sys
# from cpu_tues import *
from cpu import * 

cpu = CPU()

# cpu.load(sys.argv[1]) #tues
cpu.load() #mon
cpu.run()