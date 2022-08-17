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
    "x-prisoners": {
        "number": 2,
        "races": {
            "nura",
        },
        "description": "kidnapped {}, waiting to be devoured",
        "places": {
            "jail",
            "dead end",
        },
        "clashes": {
            "entrance",
            "sunroof",
            "invaders",
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
            "invaders",
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
            "human prisoners",
            "x-prisoners",
        },
    },
    "ogres": {
        "number": 2,
        "races": {
            "nura",
        },
        "description": "big, dwarvish goblins",
        "places": {
            "-2",
            "stone bridge",
            "end",
        },
        "clashes": {
            "sunroof",
        },
    },
    "woodspy": {
        "number": 2,
        "races": {
            "nura",
            "necromancer",
        },
        "description": "big nasty octopus",
        "places": {
            "lake",
        },
        "clashes": {
            "invaders",
        },
    },
    "umber hulk": {
        "number": 1,
        "races": {
            "nura",
        },
        "description": "big nasty bug",
        "places": {
            "kitchen",
            "feasting hall",
            "underdark",
        },
        "clashes": {
            "invaders",
            "human prisoners",
            "x-prisoners",
        },
    },
    "watcher": {
        "number": 1,
        "races": {
            "nura",
        },
        "description": "slow monster, lets out noxious fumes",
        "places": {
            "tunnel",
        },
        "clashes": {
            "invaders",
            "river",
            "lake",
            "sunroof",
        },
    },
    "demilich": {
        "number": 1,
        "races": {
            "necromancer",
        },
        "description": "Lich-lite, half the calories.",
        "places": {
            "x-ghouls",
            "library",
            "mana lake",
        },
        "clashes": {
            "sunroof",
            "chasm",
            "lake",
        },
    },
    "necromancer": {
        "number": 3,
        "races": {
            "necromancer",
        },
        "description": "Trainee - still mostly-living.",
        "places": {
            "x-ghouls",
            "library",
            "demilich",
        },
        "clashes": {
            -1,
            "sunroof",
            "chasm",
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
            "workers' quarters",
            "vault",
            "feasting hall",
        },
        "clashes": {
            "mana lake",
            "chasm",
            "traps",
            "sunroof",
        },
    },
    "undead ogre": {
        "number": 3,
        "races": {
            "necromancer",
        },
        "description": "big, dead, smelly thing",
        "places": {
            "split",
            "tunnel",
        },
        "clashes": {
            "mana lake",
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
            "tunnel",
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
            "workers' quarters",
            "workshop",
            "kitchen",
        },
    },
    "x-ghouls": {
        "number": 4,
        "races": {
            "necromancer",
            "nura",
        },
        "description": "ghoul " + civilization,
        "places": {
            "living quarters",
            "workers' quarters",
            "vault",
        },
        "clashes": {
            "mana lake",
            "sunroof",
            "chasm",
            "traps",
        },
    },
    "sleeping goblin": {
        "number": 1,
        "races": {
            "nura",
        },
        "description": "standard, snotty goblin",
        "places": {
            "tunnel",
            "split",
        },
        "clashes": {
            "sunroof",
            "traps",
        },
    },
}
