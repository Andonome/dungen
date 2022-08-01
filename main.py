#!/usr/bin/python

# phase1 deals with stage 1: making the space
from phase1 import *
from graph import *

setting = random.choice(["mine", "deep"])

dungeon = makeDunList(setting)

dungeon = joinDun(dungeon)

#print("Setting: " + setting)

#for x in list(dungeon.keys()):
#    output = str(x) + ": " + dungeon[x]["name"]
#    if "connections" in dungeon[x]:
#        output += " --> " + str(dungeon[x]["connections"])
#    print(output)

graph(dungeon)
