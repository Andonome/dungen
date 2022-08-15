import copy
import random
from features import *
from traps import *
from enemies import *
from vars import *

race = "goblins"

def rampage(dungeon):
    placeContents(
        dungeon,
        enemies,
        contentType = "invaders",
        race = enemy,
        )
    placeContents(
        dungeon,
        traps,
        contentType = "invader traps",
        race = enemy,
        )
        
