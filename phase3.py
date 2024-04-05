from features import *
from traps import *
from enemies import *
from vars import *

# A tunnel invasion is when the enemy break into the
# dungeon from some inner room, rather than through the
# entrance. This creates a new entrance, labelled
# 'underdark', where the goblins sneak in.


def tunnelInvasion(dungeon):
    x = len(dungeon)
    dungeon.append({})
    dungeon[x]["connections"] = [-1]
    dungeon[x]["features"] = ["underdark"]
    dungeon[x]["creatures"] = []
    dungeon[x]["type"] = []


# Rampage sets the stage - nura break in from below with a
# tunnelInvasion, others enter through the entrance, place
# their traps/ items/ monsters, and the dungeon's
# complete.


def rampage(dungeon):
    if (
        enemy == "nura"
        and tn(6)
        and "entrance" not in dungeon[len(dungeon) - 1]["type"]
    ):
        tunnelInvasion(dungeon)
    placeContents(
        dungeon,
        enemies,
        contentType="invaders",
        race=enemy,
        TN=7,
    )
    placeContents(
        dungeon,
        traps,
        contentType="invader traps",
        race=enemy,
        TN=7,
    )
