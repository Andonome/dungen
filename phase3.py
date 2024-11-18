from features import *
from traps import *
from enemies import *
from vars import roll_for_tn

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


def rampage(dungeon, invaders : str):
    if (
        invaders == "nura"
        and roll_for_tn(6)
        and "entrance" not in dungeon[len(dungeon) - 1]["type"]
    ):
        tunnelInvasion(dungeon)
    place_contents(
        dungeon,
        enemies,
        content_type="invaders",
        civilization=invaders,
        tn=7,
    )
    place_contents(
        dungeon,
        traps,
        content_type="invader traps",
        civilization=invaders,
        tn=7,
    )
