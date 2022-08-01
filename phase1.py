import random
import pprint
from areas import *

### Plan ###
#  The final result might look something like this:
#
#     "entrance": {
#         "name": "entrance",
#         "leadsto": [2],
#         "description": """
# This is where people come in.
#
# Hopefully there will be at least one entrance.
# """,
#     },
#     "alcove": {
#         "name": "alcove",
#         "leadsto": [3,4]
#         "description": """
# A room without a view
# """,
# --------------------
# So we get a series of rooms, and their connections.
# Initial values we take from the areas, then add the key 'leadsto'.
#


def show(x):
    pprint.pprint(x)


def makeDunList(setting):
    dungeon = {}
    dungeon[1] = areas["entrance"]
    oldChoice = "entrance"
    # With 'entrance' as area 1, 'count' starts at 2.
    # The count only increases when we have a non-repeating room, to avoid getting rooms 1,2,4,6.
    count = 2
    while count < 19:
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
    for x in range(2, len(dungeon) + 1):
        if random.randint(1, 3) == 2 and x >= 3:
            dungeon[x]["connections"] = [random.randint(2, x - 1)]
        else:
            dungeon[x]["connections"] = [x - 1]

    return dungeon
