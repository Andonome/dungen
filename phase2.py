import random
import features
from traps import traps
import vars



def get_traps_number(civilization : str):
    """
    Sets the traps number to 7 unless the traps number is set for a civilization.
    Civilizations should be made into objects later, but this works fine for now.
    """
    traps_number_for_civilization = {"gnomes": 3,
                                     "dwarves": 5}

    return traps_number_for_civilization.get(civilization, 7)


def civilize(dungeon, civilization: str):
    """
    Adds civilization-specific features to a dungeon in order:
    - Basic civilization features (living spaces, workshops, etc.)
    - Traps with civilization-specific difficulty
    - Treasures
    - Mobility features (bridges, boats)
    - Special doors

    'We place the elves, dwarves, or whichever race has come
    in to civilize the would-be dingy and boring dungeon.'

    Args:
        dungeon (list): The dungeon to civilize
        civilization (str): The civilization adding features (e.g., "dwarves", "elves")

    Returns:
        list: The modified dungeon
    """
    traps_number = get_traps_number(civilization)

    # Add features in order of likelihood/importance
    vars.place_contents(dungeon,
                        features.civilFeatures,
                        content_type="civilized",
                        civilization=civilization,
                        tn=5)

    vars.place_contents(dungeon,
                        traps,
                        content_type="traps",
                        civilization=civilization,
                        tn=traps_number)

    vars.place_contents(dungeon,
                        features.treasures,
                        content_type="treasures",
                        civilization=civilization,
                        tn=6)

    vars.place_contents(dungeon,
                        features.mobilityFeatures,
                        content_type="mobility",
                        civilization=civilization,
                        tn=2)

    vars.place_contents(dungeon,
                        features.specialDoors,
                        content_type="doors",
                        civilization=civilization,
                        tn=8)

    return dungeon