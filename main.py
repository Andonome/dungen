#!/usr/bin/python

# phase1 deals with stage 1: making the space
from phase1 import *
from phase2 import *
from phase3 import *
from graph import *
from vars import *

import random
import time


dungeon = makeDungeon(setting, dunSize)

# time.sleep(2)

civilize(dungeon)

rampage(dungeon)

graph(dungeon, setting, civilization)
