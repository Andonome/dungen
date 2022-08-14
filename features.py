# This mega-dictionary containts all the features,
# with a list of how common they are, a sub-list of where they might occur, and a description.


primitiveFeatures = {
    "chasm": {
        "number": 2,
        "description": "big hole",
        "settings": [
            "caves",
        ],
    },
    "lake": {
        "number": 2,
        "description": "big hole with water",
        "settings": [
            "caves",
            "mine",
        ],
    },
    "river": {
        "number": 2,
        "description": "big hole with water",
        "settings": [
            "caves",
            "mine",
        ],
    },
    "stallagmites": {
        "number": 2,
        "description": "difficult to walk over",
        "settings": [
            "caves",
        ],
    },
    "mana lake": {
        "number": 1,
        "description": "sparkly magic cave",
        "settings": [
            "caves",
        ],
    },
    "gas leak": {
        "number": 1,
        "description": "fissures of farts",
        "settings": [
            "caves",
            "mine",
        ],
    },
    "gold seam": {
        "number": 1,
        "description": "long squiggly gold lines",
        "settings": [
            "mine",
        ],
    },
    "tin seam": {
        "number": 1,
        "description": "long squiggly tin lines",
        "settings": [
            "mine",
        ],
    },
}


civilFeatures = {
    "stone bridge": {
        "number": 1,
        "description": "over troubled water",
        "races": {
            "dwarves",
            "gnomes",
        },
        "clashes": {
            "alternative",
            "dead end",
        },
        "places": {
            "chasm",
            "river",
        },
    },
    "wooden bridge": {
        "number": 1,
        "description": "over troubled water",
        "races": {
            "dwarves",
            "elves",
            "gnomes",
        },
        "clashes": {
            "alternative",
            "dead end",
        },
        "places": {
            "chasm",
            "river",
        },
    },
    "gas patches": {
        "number": 1,
        "description": "clay patches to stop gass vent",
        "races": {
            "dwarves",
            "elves",
            "gnomes",
        },
        "clashes": {
            "entrance",
        },
        "places": {
            "gas leak",
        },
    },
    "boats": {
        "number": 1,
        "description": "over troubled water",
        "races": {
            "dwarves",
            "elves",
            "gnomes",
        },
        "clashes": {
            "alternative",
            "dead end",
        },
        "places": {
            "lake",
        },
    },
    "guard post": {
        "number": 2,
        "description": "OC, don't steal",
        "races": {
            "dwarves",
            "elves",
            "gnomes",
        },
        "clashes": {
            "alternative",
            "gas leak",
            "dead end",
        },
        "places": {
            "split",
            "entrance",
        },
    },
    "murder holes": {
        "number": 1,
        "description": "a block over a particular wall, peppered with holes to shoot arrows through",
        "races": {
            "dwarves",
            "elves",
            "gnomes",
        },
        "clashes": {
            "alternative",
        },
        "places": {
            "guard post",
        },
    },
    "servants' quarters": {
        "number": 1,
        "description": "",
        "races": {
            "dwarves",
        },
        "clashes": {
            "chasm",
            "mana lake",
            "fungal garden",
        },
        "places": {
            "dead end",
        },
    },
    "living quarters": {
        "number": 2,
        "description": "many halls, many beds.",
        "races": {
            "dwarves",
            "elves",
            "gnomes",
        },
        "clashes": {
            "chasm",
            "lake",
            "mana lake",
            "stallagmites",
            "river",
        },
        "places": {
            "dead end",
            "alternative",
        },
    },
    "fungal garden": {
        "number": 1,
        "description": "placed by water",
        "races": {
            "dwarves",
            "elves",
            "gnomes",
            "stallagmites",
        },
        "clashes": set(),
        "places": {
            "lake",
            "river",
        },
    },
    "kitchen": {
        "number": 1,
        "description": "",
        "races": {
            "dwarves",
            "elves",
            "gnomes",
        },
        "clashes": {
            "mana lake",
            "lake",
            "stallagmites",
            "chasm",
        },
        "places": {
            "dead end",
            "alternative",
        },
    },
    "feasting hall": {
        "number": 1,
        "description": "Where everyone eats",
        "races": {
            "dwarves",
            "gnomes",
            "elves",
        },
        "clashes": {
            "mana lake",
            "entrance",
            "chasm",
            "river",
            "lake",
            "stallagmites",
        },
        "places": {
            "alternative",
        },
    },
    "armoury": {
        "number": 1,
        "description": "Mostly left arms",
        "races": {
            "dwarves",
            "elves",
            "gnomes",
        },
        "clashes": {
            "chasm",
            "river",
            "stallagmites",
            "lake",
            "mana lake",
        },
        "places": {
            "dead end",
            "alternative",
        },
    },
    "music hall": {
        "number": 1,
        "description": "hall for music ",
        "races": {
            "elves",
        },
        "clashes": set(),
        "places": {
            "split",
            "alternative",
            "dead end",
        },
    },
    "art hall": {
        "number": 1,
        "description": "statues, mostly",
        "races": {
            "elves",
        },
        "clashes": set(),
        "places": {
            "split",
            "tunnel",
            "dead end",
        },
    },
    "library": {
        "number": 1,
        "description": "library",
        "races": {
            "dwarves",
            "elves",
            "gnomes",
        },
        "clashes": {
            "stallagmites",
        },
        "places": {
            "alternative",
            "dead end",
        },
    },
    "runemaster's quarters": {
        "number": 1,
        "description": "Where a runemaster sleeps",
        "races": {
            "dwarves",
        },
        "clashes": set(),
        "places": {
            "dead end",
        },
    },
    "tomb": {
        "number": 1,
        "description": "dead people, with writing",
        "races": {
            "dwarves",
            "gnomes",
        },
        "clashes": {
            "stallagmites",
        },
        "places": {
            "alternative",
            "dead end",
        },
    },
    "workshop": {
        "number": 1,
        "description": "many halls, many beds.",
        "races": {
            "dwarves",
            "gnomes",
        },
        "clashes": {
            "chasm",
            "lake",
            "river",
            "stallagmites",
        },
        "places": {
            "dead end",
            "alternative",
        },
    },
    "jail": {
        "number": 1,
        "description": "some prisoners did a naghty, and now they're here",
        "races": {
            "dwarves",
        },
        "clashes": {
            "mana lake",
        },
        "places": {
            "dead end",
        },
    },
    "alchemy laboratory": {
        "number": 1,
        "description": "wizards gonna wizz",
        "races": {
            "gnomes",
        },
        "clashes": {
            "chasm",
            "river",
            "lake",
            "stallagmites",
        },
        "places": {
            "dead end",
            "alternative",
        },
    },
    "queen's room": {
        "number": 1,
        "description": "Where a king sleeps",
        "races": {
            "dwarves",
        },
        "clashes": {
            "chasm",
            "stallagmites",
            "river",
        },
        "places": {
            "dead end",
        },
    },
    "vault": {
        "number": 1,
        "description": "Lots of shiny",
        "races": {
            "dwarves",
            "gnomes",
        },
        "clashes": {
            "chasm",
            "lake",
        },
        "places": {
            "dead end",
        },
    },
    "shrine to Cale": {
        "number": 1,
        "description": "a large carving of a book, with a riddle written on it",
        "races": {
            "gnomes",
        },
        "clashes": set(),
        "places": {
            "tunnel",
            "dead end",
        },
    },
    "shrine to Qualme": {
        "number": 1,
        "description": "a tall stone, with a family tree carved from the bottom, upwards",
        "races": {
            "dwarves",
        },
        "clashes": set(),
        "places": {
            "tunnel",
            "entrance",
            "split",
        },
    },
}
