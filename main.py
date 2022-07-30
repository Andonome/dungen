#!/usr/bin/python

import random
from areas import *

cause_list = [
    "depths",
    "mine",
    "forest"
]

location = random.choice(cause_list)

#print("Location: " + location)

map1 = []

# now we list which areas  are in our current map

def noRepeat(map):
    for entry in range(1,len(map)-2):
        if map[entry] == map[entry - 1]:
            map.remove(map[entry])


def chooseAreas(map):
    for loc in areas:
        for no in range(areas[loc][0]):
            #if location in areas[loc][1]:
                if random.randint(1,2) == 1:
                    map.append(loc)
    random.shuffle(map)

def joinMap(map):
    map[0] = 'entrance'
    noRepeat(map)
    for index, entry in enumerate(map):
        current = '[ ' + str(index) + ': ' + str(entry) + ' ]'
        connector=random.randint(index,len(map)-1)
        if connector > index and connector % 2 == 0:
            current += ' --> [ ' + str(connector) + ': ' + map[connector] +' ]'
        elif index < len(map) -2:
            current += ' --> [ ' + str(index +1) + ': ' + str(map[index + 1]) +' ]'
        print(current)

def makeMap(map):
    chooseAreas(map)
    noRepeat(map)
    joinMap(map)

makeMap(map1)

