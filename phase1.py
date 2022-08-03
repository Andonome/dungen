import random
import copy
import pprint
from areas import *


def show(x):
    pprint.pprint(x)


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
        if setting in areas[areaChoice]["ecosystems"] and areaChoice != oldChoice and areas[areaChoice]["name"] != "entrance":
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
            if dungeon[newConnection]["name"] != 'entrance':
                dungeon[x]["connections"].append(newConnection)
                nexus = newConnection
            joins -= 2
        else:
            if dungeon[x-1]["name"] == "entrance":
                dungeon[x]["connections"].append(x-1)
                joins +=1
            else:
                dungeon[x]["connections"].append(x - 1)
                joins +=1
    # Finally, maybe add another entrance, but only connect it in one
    # place.
    if random.randint(1,1) == 1:
        dungeon[len(dungeon)-1] = areas["entrance"].copy()
        dungeon[len(dungeon)-1]["connections"] = []
        dungeon[len(dungeon)-1]["connections"].append(random.randint(len(dungeon)/2,len(dungeon)-2))
    return dungeon
