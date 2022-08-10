# Some traps can be passed by the inhabitant (e.g. a scary
# illusion), while others cannot.  Some operate inside a
# room, others only in a doorway.

from vars import *

passableTraps = {
    "ricketyFloor": {
        "name": "rickety-floor trap",
        "atDoor": False,
        "races": [
            "dwarves",
            "goblins",
        ],
        "description": """a great hole in the ground has been covered by some wooden planks. It feels obviously wrong just walking across it, but by then it may be too late.  Anyone with Strength +2 or greater will collapse the entire floor, falling into the pit, five squares deep.

Spotting the trap requires a Wits + Vigilance check.  Larger characters destroy the ground faster, so the TN is 6 plus double the character's Strength score.

Anyone calling into the pit receives 2D6 Damage.
        """,
    },
    "prisonDoor": {
        "name": "prisoner's door",
        "atDoor": True,
        "races": [
            "dwarves",
            "gnomes",
        ],
        "description": """This open passageway has little downward-facing spikes at the side, with a heavy door, hanging above, ready to slide downn.  Once someone steps on a loose stone on the other side, it spreads the door's sides a modicum, letting the door slide down with a crash.

The moment someone steps off the loose stone, the spiked doorward stops spreading out, and clamps the heavy door shut.

In this way, the {} once traped intruders.""",
    },
    "ghoulRaiser": {
        "name": "the singing skull",
        "atDoor": False,
        "races": [
            "dwarves",
        ],
        "description": "This skull once belonged to a priest of the {}, and now stands to guard their halls.  It will animate from the dead, any dead creature, within the area, or any nearby areas. When the {} still lived here, it also stood as a reminder that no two {} should ever fight each other, or the Skull would punish them",
    },
}

blockingTraps = {

    "slide": {
        "name": "slime slide",
        "atDoor": True,
        "races": [
            "goblins",
            "gnomes",
        ],
        "description": """This long passage slopes gently down, then less gently, and once the slimy floor gets under-foot, it whisks the walker down-hill, and into a nasty barricade of metal a spikes.""",
    },
    "mushroomSpores": {
        "name": "mushroom spores",
        "atDoor": False,
        "races": [
            "dwarves",
            "goblins",
            "gnomes",
        ],
        "description": """These carefully tended mushrooms emit noxious spores into the air. Anyone not Keeping Edgy must make a Wits + Survival check at TN 8.  Those failing the roll receive 4 Fatigue Points, plus one for every Failure Margin.  They also begin coughing profusely, and must make a Strength + Survival check, TN 10, to act for a round.  This effect lasts for the remainder of the scene.

Anyone wishing to sneak past the mushrooms without disturbing them can make a Dexterity + Survival check, TN 9. Once one goes off, the rest emit more spores, like a chain of dominoes.
""",
    },
    "rocksFall": {
        "name": "balanced rocks",
        "atDoor": False,
        "races": [
            "dwarves",
            "goblins",
        ],
        "description": "Rocks fall. Everyone dies",
    },
}
