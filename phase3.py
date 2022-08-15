import copy
import random
from features import *
from traps import *
from enemies import *
from vars import *

def rampage(dungeon):
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
        
