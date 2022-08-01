import random
import pprint
from areas import *


def show(x):
    pprint.pprint(x)


def makeDunList(setting):
    dungeon = {}
    dungeon[1] = areas["entrance"]
    oldChoice = "entrance"
    # With 'entrance' as area 1, 'count' starts at 2.
    # The count only increases when we have a non-repeating room, to avoid getting rooms 1,2,4,6.
    count = 2
    while count < 15:
        areaChoice = random.choice(list(areas.keys()))
        if setting in areas[areaChoice]["ecosystems"] and areaChoice != oldChoice:
            # The original piece of code was this:
            # dungeon[count] = areas[areaChoice]
            # Which lost me an two hours, as this make a reference point,
            # and all refence points change together, so all 'tunnel'
            # rooms would be the same forever.
            dungeon[count] = areas[areaChoice].copy()
            count += 1
        oldChoice = areaChoice
    return dungeon


def joinDun(dungeon):
    joins = 2
    for x in range(2, len(dungeon) + 1):
        dungeon[x]["connections"] = []
        while random.randint(1, joins) == 1 and x >= 3:
            dungeon[x]["connections"].append(random.randint(2, x - 1))
            joins += 1
        else:
            dungeon[x]["connections"].append(x - 1)
    return dungeon
