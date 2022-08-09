from phase2 import *

traps = {
    "rocksFall": {
        "name": "balanced rocks",
        "races": [
            "dwarves",
            "goblins",
        ],
        "passable": False,
        "description": "Rocks fall. Everyone dies",
    },
    "ricketyFloor": {
        "name": "rickety-floor trap",
        "races": [
            "dwarves",
            "goblins",
        ],
        "passable": True,
        "description": """a great hole in the ground has been covered by some wooden planks. It feels obviously wrong just walking across it, but by then it may be too late.  Anyone with Strength +2 or greater will collapse the entire floor, falling into the pit, five squares deep.

Spotting the trap requires a Wits + Vigilance check.  Larger characters destroy the ground faster, so the TN is 6 plus double the character's Strength score.

Anyone calling into the pit receives 2D6 Damage.
        """,
    },
    "mushroomSpores": {
        "name": "mushroom spores",
        "races": [
            "dwarves",
            "goblins",
            "gnomes",
        ],
        "passable": False,
        "description": """These carefully tended mushrooms emit noxious spores into the air. Anyone not Keeping Edgy must make a Wits + Survival check at TN 8.  Those failing the roll receive 4 Fatigue Points, plus one for every Failure Margin.  They also begin coughing profusely, and must make a Strength + Survival check, TN 10, to act for a round.  This effect lasts for the remainder of the scene.

Anyone wishing to sneak past the mushrooms without disturbing them can make a Dexterity + Survival check, TN 9. Once one goes off, the rest emit more spores, like a chain of dominoes.
""",
    },
    "prisonDoor": {
        "name": "prisoner's door",
        "races": [
            "dwarves",
            "gnomes",
        ],
        "passable": True,
        "description": """This open passageway has little downward-facing spikes at the side, with a heavy door, hanging above, ready to slide downn.  Once someone steps on a loose stone on the other side, it spreads the door's sides a modicum, letting the door slide down with a crash.

The moment someone steps off the loose stone, the spiked doorward stops spreading out, and clamps the heavy door shut.

In this way, the """ + race + " once traped intruders.",
    },
    "ghoulRaiser": {
        "name": "the singing skull",
        "races": [
            "dwarves",
        ],
        "passable": True,
        "description": "This skull once belonged to a priest of the " + race + ", and now stands to guard their halls.  It will animate from the dead, any dead creature, within the area, or any nearby areas. When the " + race + " still lived here, it also stood as a reminder that no two " + race + " should ever fight each other, or the Skull would punish them",
    },
    "slide": {
        "name": "slime slide",
        "races": [
            "goblins",
            "gnomes",
        ],
        "passable": False,
        "description": """This long passage slopes gently down, then less gently, and once the slimy floor gets under-foot, it whisks the walker down-hill, and into a nasty barricade of metal a spikes.""",
    },
}
