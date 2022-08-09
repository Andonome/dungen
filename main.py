#!/usr/bin/python

# phase1 deals with stage 1: making the space
from phase1 import *
from phase2 import *
from phase3 import *
from graph import *

import random
import time

dunSize = 18
setting = random.choice(["mine", "caves"])

dungeon = makeDungeon(setting,dunSize)

graph(setting,dungeon)

#time.sleep(2)

civilize(dungeon)

#rampage(dungeon)

graph(setting,dungeon)

