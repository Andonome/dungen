import copy
from constructions import *
from areas import *

# This list shows what places gain which features.
# A chasm would require a bridge over it to be liveable.

global roomTransformations
roomTransformations = [
    ["entrance", "trap"],
    ["lavapit", "bridge"],
    ["chasm", "bridge"],
    ["mana lake", "magic room"],
    ["river", "bridge"],
    ["lake", "boats"],
]

# This ordered wish list makes the elves make one alcove into a kitchen,
# then one cavern into a library.

# A rating of 0 means the rooms will exist if we have a spare place for it.
# A rating of > 0 means that many rooms must exist.

wishList = [
    ["alcove", "kitchen", 1],
    ["cavern", "library", 1],
    ["alcove", "forge", 0],
    ["fungus", "garden", 1],
    ["cavern", "musicHall", 0],
    ["alcove", "bedroom", 4],
    ["lake", "boats", 0],
]

# If the civilizing race doesn't have enough rooms to live, they'll have to make more.
def addRooms(dungeon):
    # first make a connection somewhere (not the entrances)
    for splitChoice in range(len(dungeon)-2, 3, -1):
        if dungeon[splitChoice]["name"] == "tunnel":
            break
        elif dungeon[splitChoice]["name"] == "cavern":
            break
        else:
            splitChoice = len(dungeon) -3
    lastRoom = len(dungeon)
    for newRoom in range(len(wishList)):
        for x in range(wishList[newRoom][2]):
            dungeon[lastRoom] = copy.deepcopy(areas[wishList[newRoom][0]])
            dungeon[lastRoom]["connections"].append(splitChoice)
            lastRoom  += 1
            #print("Needed: " + wishList[newRoom][1])

def fixRooms(dungeon):
    for x in range(len(dungeon) - 1, 0, -1):
        for pair in range(len(roomTransformations)):
            if dungeon[x]["name"] == roomTransformations[pair][0]:
                dungeon[x]["constructions"].append(roomTransformations[pair][1])

def makeRooms(dungeon):
    for x in range(len(dungeon) - 1, 1, -1):
        for pair in range(len(wishList)):
            while wishList[pair][2] >= 0 and dungeon[x]["name"] == wishList[pair][0] and dungeon[x]["constructions"] == []:
                dungeon[x]["constructions"].append(wishList[pair][1])
                wishList[pair][2] -= 1
                break

        
