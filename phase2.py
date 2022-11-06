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


# We place the elves, dwarves, or whichever race has come
# in to civilize the would-be dingy and boring dungeon.

def civilize(dungeon):
    placeContents(
        dungeon,
        civilFeatures,
        contentType="civilized",
        race=civilization,
        TN=5,
    )
    placeContents(dungeon, traps, contentType="traps", race=civilization, TN=trapsNo)
    placeContents(
        dungeon,
        treasures,
        contentType="treasures",
        race=civilization,
        TN=6,
    )
    placeContents(
        dungeon,
        mobilityFeatures,
        contentType="mobility",
        race=civilization,
        TN=2,
    )
    placeContents(
        dungeon,
        specialDoors,
        contentType="doors",
        race=civilization,
        TN=8,
    )
