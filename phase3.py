
from traps import traps
from enemies import enemies
from vars import roll_for_tn, place_contents

def tunnel_invasion(dungeon):
    """
    Creates a tunnel invasion, adding a new room on the end and connecting it to the end room.

    A tunnel invasion is when the enemy break into the
    dungeon from some inner room, rather than through the
    entrance. This creates a new entrance, labelled
    'underdark', where the goblins sneak in.
    """

    dungeon.append({})
    dungeon[-1]["connections"] = [-1]
    dungeon[-1]["features"] = ["underdark"]
    dungeon[-1]["creatures"] = []
    dungeon[-1]["type"] = []

    return dungeon

def rampage(dungeon, invaders : str):
    """
    Rampage sets the stage - nura break in from below with a tunnelInvasion, others enter through the entrance,
    place their traps/ items/ monsters, and the dungeon's complete.
    """

    if (
        invaders == "nura"
        and roll_for_tn(6)
        and "entrance" not in dungeon[-1]["type"]
    ):
        dungeon = tunnel_invasion(dungeon)

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

    return dungeon