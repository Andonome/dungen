# Unsure how to do this part.  Some areas get built the
# same way - everyone needs a fungus garden and bridges
# over rivers.  But then some races will need different
# functions for where to build things.

import copy
import random
from features import *
from traps import *
from areas import *
from vars import *

# This list shows what places gain which features.
# A chasm would require a bridge over it to be liveable.

global roomTransformations
roomTransformations = [
    ["entrance", "trap"],
    ["mana lake", "magic room"],
]

# This ordered wish list makes the elves make one cavern into a kitchen,
# then one cavern into a library.

# A rating of 0 means the rooms will exist if we have a spare place for it.
# A rating of > 0 means that many rooms must exist.



def makeRooms(dungeon,civilization):
    wishList = []
    for f in civilFeatures:
        if civilization in civilFeatures[f]["races"]:
            wishList.append(f)
    for x in range(len(dungeon)-1,3,-1):
        for f in wishList:
            if (
            not set.isdisjoint(set.union(set((dungeon[x]["type"])),set(dungeon[x]["features"])),set(civilFeatures[f]["places"]))
            and len(dungeon[x]["features"]) < 2
            ):
                dungeon[x]["features"].append(f)
                wishList.remove(f)
                break

def makeBlockTraps(race):
    list = []
    for x in blockingTraps:
        if race in blockingTraps[x]["races"]:
            list.append(x)
    return list

def trapEntrance(dungeon):
    trapBlockList = makeBlockTraps(civilization)
    entranceList = []
    alternativeList = []
    for x in range(len(dungeon)):
        if "entrance" in dungeon[x]["type"]:
            entranceList.append(x)
    while len(trapBlockList) > 0 and len(entranceList) > 1:
        dungeon[entranceList[-1]]["features"].append(trapBlockList[0])
        del trapBlockList[0]
        del entranceList[-1]


def civilize(dungeon):
    trapEntrance(dungeon)
    makeRooms(dungeon,civilization)
