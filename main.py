#!/usr/bin/python

# phase1 deals with stage 1: making the space
from phase1 import *

dungeon = makedun()

for x in range(1, len(dungeon) + 1):
    print(str(x) + ": " + dungeon[x]["name"])

