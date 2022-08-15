from vars import *

enemies = {
    "goblin guards": {
        "number": 2,
        "races": {
            "nura",
        },
        "description": "like regular goblins, but sleepier",
        "places": {
            "entrance",
        },
        "clashes": {
            "lake",
            "mana lake",
        },
    },
    "human prisoners": {
        "number": 1,
        "races": {
            "nura",
        },
        "description": "kidnapped people, waiting to be devoured",
        "places": {
            "jail",
            "dead end",
        },
        "clashes": {
            "entrance",
            "sunroof",
        },
    },
    "hobgoblins": {
        "number": 2,
        "races": {
            "nura",
        },
        "description": "big, dwarvish goblins",
        "places": {
            "-2",
            "kitchen",
        },
        "clashes": {
            "lake",
            "mana lake",
        },
    },
    "nuramancer": {
        "number": 2,
        "races": {
            "nura",
        },
        "description": "magic goblin",
        "places": {
            "mana lake",
            "library",
            "vault",
        },
        "clashes": {
            "lake",
            "mana lake",
        },
    },
    "nura spider": {
        "number": 2,
        "races": {
            "nura",
        },
        "description": "big nasty spider",
        "places": {
            "dead end",
            "vault",
        },
        "clashes": {
            "river",
        },
    },
    "x-ghouls": {
        "number": 1,
        "races": {
            "necromancer",
            "nura",
        },
        "description": "ghoul " + civilization,
        "places": {
            "living quarters",
            "servants' quarters",
            "vault",
        },
        "clashes": {
            "mana lake",
            "sunroof",
            "chasm",
            "traps",
        },
    },
    "human ghouls": {
        "number": 2,
        "races": {
            "necromancer",
        },
        "description": "taken as a prize from a nearby raise",
        "places": {
            "living quarters",
            "servants' quarters",
            "vault",
        },
        "clashes": {
            "mana lake",
            "chasm",
            "traps",
            "sunroof",
        },
    },
    "ghouled bear": {
        "number": 1,
        "races": {
            "necromancer",
        },
        "description": "big bear, but slow",
        "places": {
            -2,
        },
        "clashes": {
            "traps",
            "sunroof",
        },
    },
    "ooze": {
        "number": 3,
        "races": {
            "nura",
            "necromancer",
        },
        "description": "unpleasant pudding",
        "places": {
            "garden",
            "fungal garden",
            "river",
            "lake",
        },
        "clashes": {
            "tunnel",
        },
    },
    "dragon": {
        "number": 1,
        "races": {
            "nura",
            "necromancer",
        },
        "description": "Great, red, dragon, allied with the others. Like sleeping and chin-scratches.",
        "places": {
            "queen's room",
            "garden",
            "vault",
        },
        "clashes": {
            -1,
            "worker's quarters",
            "workshop",
            "kitchen",
        },
    },
}
