#!/usr/bin/python

from map1 import *
from map2 import *
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

