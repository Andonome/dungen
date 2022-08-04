import random
import copy
import pprint
from areas import *


def show(x):
    pprint.pprint(x)


def dun(dungeon):
    for x in range(len(dungeon)):
        if x in dungeon:
            print(str(x) + ": " + dungeon[x]["name"])


def makeDunList(setting):
    maxDungeonSize = 13
    dungeon = {}
    dungeon[1] = copy.deepcopy(areas["entrance"])
    oldChoice = "entrance"
    # With 'entrance' as area 1, 'count' starts at 2.
    # The count only increases when we have a non-repeating room, to avoid getting rooms 1,2,4,6.
    count = 2
    while count < maxDungeonSize:
        areaChoice = random.choice(list(areas.keys()))
        if (
            setting in areas[areaChoice]["ecosystems"]
            and areaChoice != oldChoice
            and areas[areaChoice]["name"] != "entrance"
        ):
            # The original piece of code was this:
            # dungeon[count] = areas[areaChoice]
            # Which lost me an three hours, as this make a reference point,
            # and all refence points change together, so all 'tunnel'
            # rooms would be the same forever.
            dungeon[count] = copy.deepcopy(areas[areaChoice])
            count += 1
        oldChoice = areaChoice
    return dungeon


def joinDun(dungeon):
    joins = 5
    nexus = 4
    for x in range(2, len(dungeon) + 1):
        dungeon[x]["connections"] = []
        while random.randint(1, joins) > 5 and x >= 3:
            newConnection = random.randint(2, x - 1)
            if dungeon[newConnection]["name"] != "entrance":
                dungeon[x]["connections"].append(newConnection)
                nexus = newConnection
            joins -= 2
        else:
            if dungeon[x - 1]["name"] == "entrance":
                dungeon[x]["connections"].append(x - 1)
                joins += 1
            else:
                dungeon[x]["connections"].append(x - 1)
                joins += 1
        if random.randint(0, 5) == 1:
            dungeon[x]["height"] = random.randint(0, 2)
        else:
            dungeon[x]["height"] = dungeon[x - 1]["height"]
    # Finally, maybe add another entrance, but only connect it in one
    # place.
    if random.randint(1, 2) == 1:
        dungeon[len(dungeon) - 1] = areas["entrance"].copy()
        dungeon[len(dungeon) - 1]["connections"] = []
        dungeon[len(dungeon) - 1]["connections"].append(
            random.randint(len(dungeon) / 2, len(dungeon) - 2)
        )


def riverFlow(river, dungeon):
    for newRiver in dungeon[river]["connections"]:
        if dungeon[river]["height"] >= dungeon[newRiver]["height"]:
            if (
                "river" not in dungeon[river]["features"]
                and random.randint(1, 4) != 4
            ):
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


def makeDungeon(setting):
    dungeon = makeDunList(setting)
    joinDun(dungeon)
    makeRiver(dungeon)
    makeFungi(dungeon)
    return dungeon
