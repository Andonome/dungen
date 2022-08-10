import random
import copy
import pprint
from areas import *
from features import *

# The TN function just rolls 2D6 to make choices.
def tn(tn):
    roll = random.randint(1,6) + random.randint(1,6)
    if roll >= tn:
        return True
    else:
        return False

# Just for debugging.
def show(x):
    pprint.pprint(x)

# junJoin joins dungeon pieces, usually straight down (4 -- > 3), but
# sometimes skips down (7 --> 3).
def dunJoin(dungeon,x):
    if x == 0:
        dungeon[x]["type"].append("entrance")
    # Initial rooms (0 to 4) connect to the room before.  After
    # that, there's a chance they connect straight down.
    elif x < 5 or tn(7):
        if x-1 not in dungeon[x]["connections"]:
            dungeon[x]["connections"].append(x-1)
    elif x < 7:
        dungeon[x]["connections"].append(random.randint(x-3,x-1))
    else:
        joinPlace = random.randint(x-5,x-1)
        if joinPlace not in dungeon[x]["connections"]:
            dungeon[x]["connections"].append(joinPlace)
        if tn(9):
            dunJoin(dungeon,x)

def newDungeon(setting,dunSize):
    dungeon = []
    # 'x' always refers to the dungeon area number, so x=3
    # means 'area 3'.
    x = 1
    join = False
    for x in range(dunSize):
        dungeon.append({})
        dungeon[x]["connections"] = []
        dungeon[x]["features"] = []
        dungeon[x]["creatures"] = []
        dungeon[x]["height"] = 1
        dungeon[x]["type"] = []
        dunJoin(dungeon,x)
    return dungeon

# Now the dungeon gets features, like 'chasm', or 'mana
# lakes'.
def giveFeatures(dungeon):
    random.shuffle(featureList)
    localFeatures = []
    noFeatures = int(len(dungeon) / 4)
    for f in range(noFeatures):
        localFeatures.append(featureList[f])
    for x in range(len(dungeon)):
        if tn(len(dungeon) +4 - len(localFeatures) - x) and len(localFeatures) > 0:
            dungeon[x]["features"].append(localFeatures[0])
            del localFeatures[0]

# Room types show relations between rooms, such as 'the
# entrance', or a simple tunnel - a room which goes to
# another room.

def labelType(dungeon):
    for x in range(len(dungeon)):
        if len(dungeon[x]["connections"]) == 1:
            dungeon[x]["type"].append("dead end")
        elif len(dungeon[x]["connections"]) > 2:
            dungeon[x]["type"].append("split")
        else:
            dungeon[x]["type"].append("tunnel")
        # We start by labelling every part as a dead end, then if
        # something connects to it, that part is no longer a dead
        # end.
        for c in dungeon[x]["connections"]:
            if "dead end" in dungeon[c]["type"]:
                dungeon[c]["type"].remove("dead end")
            if "tunnel" in dungeon[c]["type"]:
                dungeon[c]["type"].remove("tunnel")
                if "split" not in dungeon[c]["type"]:
                    dungeon[c]["type"].append("split")
            elif "split" not in dungeon[c]["type"]:
                dungeon[c]["type"].append("tunnel")

def findExit(dungeon,x):
    c = x
    route = [c]
    while c > 1:
        c = dungeon[c]["connections"][0]
        route.append(c)
    return route
        

def labelRoutes(dungeon):
    paths = []
    for x in range(len(dungeon)-1,1,-1):
        if len(dungeon[x]["connections"]) > 1:
            for _ in dungeon[x]["connections"]:
                paths.append(findExit(dungeon,x))
    return(paths)

# Races can only place an impassable trap (like a swinging
# sphere of anihilation) in tunnels which form alternative
# routes - not the only  route to a place.

c = 1

def labelAlternatives(dungeon):
    for x in range(len(dungeon)):
        if "dead end" not in dungeon[x]["type"]:
            dungeon[x]["type"].append("alternative")
        if len(dungeon[x]["connections"]) == 1:
            c = dungeon[x]["connections"][0]
            if "alternative" in dungeon[c]["type"]:
                dungeon[c]["type"].remove("alternative")


def makeDungeon(setting,dunSize):
    dungeon = newDungeon(setting,dunSize)
    giveFeatures(dungeon)
    labelType(dungeon)
    labelAlternatives(dungeon)
    #labelRoutes(dungeon)
    #makeRiver(dungeon)
    #makeFungi(dungeon)
    return dungeon
