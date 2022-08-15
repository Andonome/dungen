import random
from features import *
from traps import *
from vars import *

if civilization == "gnomes":
    trapsNo = 3
elif civilization == "dwarves":
    trapsNo = 5
else:
    trapsNo = 7


def civilize(dungeon):
    placeContents(
        dungeon,
        civilFeatures,
        contentType="civilized",
        race=civilization,
        TN=7,
    )
    placeContents(dungeon, traps, contentType="traps", race=civilization, TN=trapsNo)
    placeContents(
        dungeon,
        treasures,
        contentType="treasures",
        race=civilization,
        TN=6,
    )
