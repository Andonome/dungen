from rooms import *
import random

races_list = ["elves", "dwarves", "gnomes"]

# now we civilize the areas by making them real rooms.

replacement = [
    ["alcove", "bedroom"],
    ["chasm", "bridge"],
    ["lavapit", "bridge"],
    ["cavern", "hall"],
    ["river", "bridge"],
]


def civilization(map):
    for area in range(len(map)):
        for swap in range(len(replacement)):
            if map[area] == replacement[swap][0]:
                map[area] += ": " + replacement[swap][1]
    return map
