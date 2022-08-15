from features import *
from traps import *
from enemies import *
from vars import *

def tunnelInvasion(dungeon):
    x = len(dungeon)
    dungeon.append({})
    dungeon[x]["connections"] = [-1]
    dungeon[x]["features"] = ["underdark"]
    dungeon[x]["creatures"] = []
    dungeon[x]["height"] = 1
    dungeon[x]["type"] = []

def rampage(dungeon):
    if (
    enemy == "nura"
    and tn(6)
    and "entrance" not in dungeon[len(dungeon)-1]["type"]
    ):
        tunnelInvasion(dungeon)
    placeContents(
        dungeon,
        enemies,
        contentType = "invaders",
        race = enemy,
        TN = 6,
        )
    placeContents(
        dungeon,
        traps,
        contentType = "invader traps",
        race = enemy,
        )
