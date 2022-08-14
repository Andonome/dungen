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

roomTransformations = [
    ["entrance", "trap"],
    ["mana lake", "magic room"],
]

# Sometimes you just want a big list  of what's in a room,
# e.g. ["river", "stone bridge", "tunnel"].
def getContents(dungeon, x):
    contents = []
    for thing in dungeon[x]:
        if type(dungeon[x][thing]) == list:
            contents += dungeon[x][thing]
    return set(contents)


# This ordered wish list makes the elves make one cavern into a kitchen,
# then one cavern into a library.

# A rating of 0 means the rooms will exist if we have a spare place for it.
# A rating of > 0 means that many rooms must exist.


def makeRooms(dungeon, civilization):
    print(30 * "=" + "\nCivilizing Features: ")
    finishedRooms = []
    for f in civilFeatures:
        for x in range(len(dungeon)):
            # we get all contents as a set, then use these sets to test
            # something is in the right place, and doesn't have anything
            # from the feature's clash set.
            contents = getContents(dungeon, x)
            if (
                civilization in civilFeatures[f]["races"]
                and civilFeatures[f]["places"].intersection(contents)
                and civilFeatures[f]["clashes"].isdisjoint(contents)
                and x not in finishedRooms
            ):
                dungeon[x]["features"].append(f)
                print(f)
                finishedRooms.append(x)
                break


def makeTrapList(race, trapList):
    localTrapList = []
    for x in trapList:
        if race in trapList[x]["races"]:
            localTrapList.append(x)
    return localTrapList


def placeBlockTraps(dungeon,civilization):
    print(30 * "=" + "\nTraps: ")
    trapList = makeTrapList(civilization, blockingTraps)
    roomList = []
    for x in range(len(dungeon)):
        if (
        len(dungeon[x]["features"]) == 0
        and set(dungeon[x]["type"]).intersection({"entrance", "alternative"})
        ):
            roomList.append(x)
    while len(roomList) * len(trapList) > 0:
        dungeon[roomList[-1]]["features"].append(trapList[0])
        print(trapList[0])
        del trapList[0]
        del roomList[-1]

def placeTunnelTraps(dungeon,civilization):
    trapList = makeTrapList(civilization, passableTraps)
    roomList = []
    for x in range(len(dungeon)):
        if (
        len(dungeon[x]["features"]) == 0
        and set(dungeon[x]["type"]).intersection({"split", "tunnel"})
        ):
            roomList.append(x)
    while len(roomList) * len(trapList) > 0:
        dungeon[roomList[-1]]["features"].append(trapList[0])
        print(trapList[0])
        del trapList[0]
        del roomList[-1]

def civilize(dungeon):
    makeRooms(dungeon, civilization)
    placeBlockTraps(dungeon,civilization)
    placeTunnelTraps(dungeon,civilization)
