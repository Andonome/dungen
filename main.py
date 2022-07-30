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

# now we list which areas  are in our current map

map1 = []

for loc in areas:
    for no in range(areas[loc][0]):
        #if location in areas[loc][1]:
            if random.randint(1,2) == 1:
                map1.append(loc)

random.shuffle(map1)

map1[0] = 'entrance'

def genmap(map):
    for entry in range(len(map)-1):
        current = '[ ' + str(entry) + ': ' + str(map[entry]) + ' ]'
        connector=random.randint(entry,len(map)-1)
        if connector > entry and connector % 2 == 0:
            current += ' --> [ ' + str(connector) + ': ' + map[connector] +' ]'
        else:
            current += ' --> [ ' + str(entry +1) + ': ' + map[entry + 1] +' ]'
        print(current)

genmap(map1)
