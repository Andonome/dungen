import random
import features
import traps
import vars

if civilization == "gnomes":
    trapsNo = 3
elif civilization == "dwarves":
    trapsNo = 5
else:
    trapsNo = 7


# We place the elves, dwarves, or whichever race has come
# in to civilize the would-be dingy and boring dungeon.


def civilize(dungeon):
    vars.placeContents(
        dungeon,
        features.civilFeatures,
        contentType="civilized",
        race=civilization,
        TN=5,
    )
    vars.placeContents(dungeon, traps, contentType="traps", race=civilization, TN=trapsNo)
    vars.placeContents(
        dungeon,
        traps.treasures,
        contentType="treasures",
        race=civilization,
        TN=6,
    )
    vars.placeContents(
        dungeon,
        features.mobilityFeatures,
        contentType="mobility",
        race=civilization,
        TN=2,
    )
    vars.placeContents(
        dungeon,
        features.specialDoors,
        contentType="doors",
        race=civilization,
        TN=8,
    )
