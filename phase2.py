# Unsure how to do this part.  Some areas get built the
# same way - everyone needs a fungus garden and bridges
# over rivers.  But then some races will need different
# functions for where to build things.

import copy
import random
from features import *
from areas import *

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

wishList = [
    ["cavern", "kitchen", 1],
    ["cavern", "library", 1],
    ["cavern", "forge", 0],
    ["cavern", "musicHall", 0],
    ["cavern", "bedroom", 4],
    ["lake", "boats", 0],
]

# I'm adding a random race, but idk what to do with this
# information yet.  Dwarves, elves, and gnomes all need a
# library, force, et c. Maybe it'll just affect different
# magical items later?

raceList = [
    "elves",
    "dwarves",
    "gnomes",
]

race = random.choice(raceList)

# If the civilizing race doesn't have enough rooms to live, they'll have to make more.



def fixRooms(dungeon):
    for x in range(len(dungeon) - 1, 0, -1):
        for pair in range(len(roomTransformations)):
            if roomTransformations[pair][0] in dungeon[x]["features"]:
                dungeon[x]["features"].append(roomTransformations[pair][1])


def makeRooms(dungeon):
    for x in range(len(dungeon) - 1, 1, -1):
        for pair in range(len(wishList)):
            while (
                wishList[pair][2] >= 0
                and wishList[pair][0] in dungeon[x]["features"]
                and dungeon[x]["features"] == []
            ):
                dungeon[x]["features"].append(wishList[pair][1])
                wishList[pair][2] -= 1
                break


# Elves need to bridge those rivers.
# We need to check for a sequence like [ cavern, river,
# cavern ], because a sequence like [ river, river, cavern ],
# shouldn't receive a bridge - this only works with one room,
# with one river segment.


# This entire bridge-builder function needs redone.
def testWater(dungeon, room):
    if (
        "river" not in dungeon[room]["features"]
        and "lake" not in dungeon[room]["features"]
    ):
        return True


def bridgeBuilder(dungeon):
    for x in range(len(dungeon) - 1, 1, -1):
        if testWater(dungeon, x):
            for y in dungeon[x]["connections"]:
                if not testWater(dungeon, y):
                    for z in dungeon[y]["connections"]:
                        if testWater(dungeon, z):
                            if "bridge" not in dungeon[y]["features"]:
                                dungeon[y]["features"].append("bridge")


def civilize(dungeon):
    fixRooms(dungeon)
    bridgeBuilder(dungeon)
    makeRooms(dungeon)
