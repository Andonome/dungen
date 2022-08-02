#!/usr/bin/python

# phase1 deals with stage 1: making the space
from phase1 import *
from graph import *

setting = random.choice(["mine", "deep"])

dungeon = makeDunList(setting)

dungeon = joinDun(dungeon)


dungeon = graph(dungeon)

for x in range(len(dungeon)):
    print(dungeon[x])
