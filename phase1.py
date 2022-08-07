import random
import copy
import pprint
from areas import *

def tn(tn):
    x = random.randint(1,6) + random.randint(1,6)
    if x >= tn:
        return True
    else:
        return False


def show(x):
    pprint.pprint(x)

def dunJoin(dungeon,x):
    if x == 1:
        pass
    elif x < 5 or tn(7):
        if x-1 not in dungeon[x]["connections"]:
            dungeon[x]["connections"].append(x-1)
    elif x < 7:
        dungeon[x]["connections"].append(random.randint(x-3,x-1))
    else:
        joinPlace = random.randint(x-6,x-1)
        if joinPlace not in dungeon[x]["connections"]:
            dungeon[x]["connections"].append(joinPlace)
        if tn(9):
            dunJoin(dungeon,x)

def newDungeon(setting,dunSize):
    dungeon = {}
    # 'x' always refers to the dungeon area number, so x=3 means 'area 3'.
    x = 1
    join = False
    while x < dunSize:
        dungeon[x] = {}
        dungeon[x]["connections"] = []
        dungeon[x]["features"] = []
        dungeon[x]["creatures"] = []
        dungeon[x]["height"] = 1
        dunJoin(dungeon,x)
        x += 1
    return dungeon


def riverFlow(river, dungeon):
    for newRiver in dungeon[river]["connections"]:
        if dungeon[river]["height"] >= dungeon[newRiver]["height"]:
            if "river" not in dungeon[river]["features"] and random.randint(1, 4) != 4:
                dungeon[river]["features"].append("river")
            riverFlow(newRiver, dungeon)
        else:
            if (
                "lake" not in dungeon[river]["features"]
                and "river" not in dungeon[river]["features"]
            ):
                dungeon[river]["features"].append("lake")


def makeRiver(dungeon):
    river = random.randint(3, len(dungeon) - 2)
    if river % 2 == 0:
        riverFlow(river, dungeon)


def makeFungi(dungeon):
    for x in range(1, len(dungeon)):
        if "lake" in dungeon[x]["features"]:
            target = x
            for y in range(1, len(dungeon)):
                if target in dungeon[y]["connections"]:
                    dungeon[y]["features"].append("fungus")


def makeDungeon(setting,dunSize):
    dungeon = newDungeon(setting,dunSize)
    makeRiver(dungeon)
    makeFungi(dungeon)
    return dungeon
