#!/usr/bin/python

from map1 import *

cause_list = [
    "depths",
    "mine",
    "forest"
]

location = random.choice(cause_list)

#print("Location: " + location)

map1 = []

# now we list which areas  are in our current map

makeMap(map1)

