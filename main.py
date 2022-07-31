#!/usr/bin/python

# map1 deals with stage 1: making the space
from map1 import *
# map2 deals with civilizing the area, transforming alcoves into rooms
from map2 import *
# the printing function just shows the result
from printer import *

cause_list = [
    "depths",
    "mine",
    "forest"
]

location = random.choice(cause_list)
race = random.choice(races_list)

#print("Location: " + location)

map1 = []
roomList = []

# now we list which areas  are in our current map

roomList = makeMap(map1)
map2 = civilization(map1)

showDungeon(roomList,map2)

roomList

