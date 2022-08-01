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


def makedun():
    dungeon = {}
    dungeon[1] = areas["entrance"]
    oldChoice = "entrance"
    count = 2
    while count < 7:
        areaChoice = random.choice(list(areas.keys()))
        if areaChoice != oldChoice:
            dungeon[count] = areas[areaChoice]
            count += 1
        oldChoice = areaChoice
    return dungeon


