#!/usr/bin/python

# phase1 deals with stage 1: making the space
from phase1 import *
from phase2 import *
from phase3 import *
from graph import *

import random

dunSize = 15
# setting = random.choice(["mine", "deep", "caves"])
setting = "caves"

dungeon = makeDungeon(setting,dunSize)

civilize(dungeon)

rampage(dungeon)

graph(dungeon)

