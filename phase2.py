import random
import features
import traps
import vars

# We place the elves, dwarves, or whichever race has come
# in to civilize the would-be dingy and boring dungeon.

def get_traps_number(civilization : str):
    """
    Sets the traps number to 7 unless the traps number is set for a civilization.
    Civilizations should be made into objects later, but this works fine for now.
    """
    traps_number_for_civilization = {"gnomes": 3,
                                     "dwarves": 5}

    return traps_number_for_civilization.get(civilization, 7)


def civilize(dungeon, civilization : str):

    traps_number = get_traps_number(civilization)

    vars.placeContents(
        dungeon,
        features.civilFeatures,
        contentType="civilized",
        civilization=civilization,
        TN=5,
    )
    vars.placeContents(dungeon, traps, contentType="traps", race=civilization, TN=traps_number)
    vars.placeContents(
        dungeon,
        features.treasures,
        contentType="treasures",
        civilization=civilization,
        TN=6,
    )
    vars.placeContents(
        dungeon,
        features.mobilityFeatures,
        contentType="mobility",
        civilization=civilization,
        TN=2,
    )
    vars.placeContents(
        dungeon,
        features.specialDoors,
        contentType="doors",
        civilization=civilization,
        TN=8,
    )
