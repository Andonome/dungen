import random
from vars import *
from features import *


def newDungeon(setting, dunSize):
    dungeon = []
    # 'x' always refers to the dungeon area number, so x=3
    # means 'area 3'.
    x = 1
    join = False
    if setting == "mine":
        joinChance = 5
    elif setting == "caves":
        joinChance = 9
    for x in range(dunSize):
        dungeon.append({})
        dungeon[x]["connections"] = []
        dungeon[x]["features"] = []
        dungeon[x]["creatures"] = []
        dungeon[x]["type"] = []
        joinChance = dunJoin(dungeon, x, joinChance)
    return dungeon


# dunJoin joins dungeon pieces, usually straight down (4 -- > 3), but
# sometimes skips down (7 --> 3).
# Each connection is relative, so 'dungeon[3]["connection"] = -1'
# means that room 3 is connected to 2 (3-1 = 2), and
# 'dungeon[5]["connection"] = -3' means that room 5 is
# connected to room 2 (5-3 = 2).


def dunJoin(dungeon, x, joinChance):
    if x == 0:
        dungeon[x]["type"].append("entrance")
    # Initial rooms (0 to 4) connect to the room before.  After
    # that, there's a chance they connect straight down.
    elif len(dungeon[x]["connections"]) > 1:
        pass
    elif x < 3:
        dungeon[x]["connections"].append(-1)
    elif tn(joinChance):
        joinChance += 2
        if -1 not in dungeon[x]["connections"]:
            dungeon[x]["connections"].append(-1)
    else:
        joinChance -= 2
        lowPoint = (x - 1) * -1
        join = random.randint(max(lowPoint, -4), -2)
        if join not in dungeon[x]["connections"]:
            dungeon[x]["connections"].append(join)
        if tn(joinChance + 1):
            joinChance = dunJoin(dungeon, x, joinChance)
    return joinChance


# Now the dungeon gets features, like 'chasm', or 'mana
# lakes'.
# These come from the 'primitiveFeatures' list, then each one is checked to see if it fits in the current 'setting' ("mine", or "dungeon").
# If so, it's added to the list.
# We then skip along the dungeon's rooms randomly dropping
# our list-items: 1,3,5,11,13,14.


def giveFeatures(dungeon, setting):
    localFeatures = []
    # n tracks features which have multiple
    n = 0
    while n < 5:
        for f in primitiveFeatures:
            if (
                tn(6)
                and setting in primitiveFeatures[f]["settings"]
                and n < primitiveFeatures[f]["number"]
            ):
                localFeatures.append(f)
        n += 1
    x = -1
    for f in localFeatures:
        x += random.randint(1, 6)
        if x < len(dungeon) - 1:
            dungeon[x]["features"].append(f)
            print(f)


# Room types show relations between rooms, such as 'the
# entrance', or a simple tunnel - a room which goes to
# another room.


def labelType(dungeon):
    dungeon[len(dungeon) - 1]["type"].append("end")
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
        for connection in dungeon[x]["connections"]:
            c = x + connection
            if "dead end" in dungeon[c]["type"]:
                dungeon[c]["type"].remove("dead end")
            if "tunnel" in dungeon[c]["type"]:
                dungeon[c]["type"].remove("tunnel")
                if "split" not in dungeon[c]["type"]:
                    dungeon[c]["type"].append("split")
            elif "split" not in dungeon[c]["type"]:
                dungeon[c]["type"].append("tunnel")


# This function literally just finds an exit. Give it a room
# number, and it return a list of the rooms to move through
# to get to the entrance.


def findExit(dungeon, c=""):
    if c == "":
        # start at the highest room
        c = len(dungeon) - 1
    # start mapping the root,  from e.g. room 25
    choice = c
    route1 = [c]
    route2 = [c]
    while c > 0:
        c = c + dungeon[c]["connections"][0]
        route1.append(c)
    c = choice
    while c > 0:
        c = c + dungeon[c]["connections"][-1]
        route2.append(c)
    if len(route1) <= len(route2):
        return route1
    else:
        return route2


# I've never used this function, but I still like it. It
# finds a route from room x to room y.


def findRoute(dungeon, x, y):
    x = findExit(dungeon, x)
    y = findExit(dungeon, y)
    while x[-1] == y[-1]:
        join = x[-1]
        x.remove(x[-1])
        y.remove(y[-1])
        if len(x) * len(y) == 0:
            break
    x.append(join)
    y.reverse()
    x += y
    return x


# Races can only place an impassable trap (like a swinging
# sphere of anihilation) in tunnels which form alternative
# routes - not the only route to a place, or nobody would be
# able to go to the toilet. Therefore, we find and label
# all the alternative passages (which you don't have to go
# through).
# Actually, we just lavel everythign an 'alternative', then
# go to every dead-end, and find the route to the exit, and
# remove the label of 'alternative'. Anything which remains
# with the label must really be an alternative, because
# nobody needs it to reach the exit.


def labelAlternatives(dungeon):
    for x in range(len(dungeon)):
        if "dead end" not in dungeon[x]["type"]:
            dungeon[x]["type"].append("alternative")
        if len(dungeon[x]["connections"]) == 1:
            c = x + dungeon[x]["connections"][0]
            if "alternative" in dungeon[c]["type"]:
                dungeon[c]["type"].remove("alternative")
        for x in findExit(dungeon):
            if "alternative" in dungeon[x]["type"]:
                dungeon[x]["type"].remove("alternative")


# turn one dead end into an entrance
def deadEndsConversion(dungeon):
    endPoints = []
    totalEntrances = 1
    for x in range(len(dungeon)):
        if "dead end" in dungeon[x]["type"]:
            endPoints.append(x)
    maxEnds = int(len(dungeon) / 10)
    for _ in range(maxEnds):
        if tn(9 - len(endPoints)) and len(endPoints) > 0:
            newEntrance = random.choice(endPoints)
            endPoints.remove(newEntrance)
            dungeon[newEntrance]["type"].remove("dead end")
            if "end" in dungeon[newEntrance]["type"]:
                dungeon[newEntrance]["type"].remove("end")
            dungeon[newEntrance]["type"].append("entrance")
            totalEntrances += 1
        else:
            break
        break
    for x in endPoints:
        entryway = x + dungeon[x]["connections"][0]
        if tn(4 + len(endPoints)) and "split" not in dungeon[entryway]["type"]:
            dungeon[x]["type"].remove("dead end")
            dungeon[x]["type"].append("hidden")
            dungeon[entryway]["type"].append("dead end")
            if "end" in dungeon[x]["type"]:
                dungeon[x]["type"].remove("end")
            print("Hidden room: " + str(x))
    print("Dead ends: " + str(len(endPoints)))
    print("Entrances: " + str(totalEntrances))


def makeDungeon(setting, dunSize):
    dungeon = newDungeon(setting, dunSize)
    labelType(dungeon)
    labelAlternatives(dungeon)
    deadEndsConversion(dungeon)
    giveFeatures(dungeon, setting)
    # makeRiver(dungeon)
    return dungeon
