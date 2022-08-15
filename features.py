# This mega-dictionary containts all the features,
# with a list of how common they are, a sub-list of where they might occur, and a description.


primitiveFeatures = {
    "stallagmites": {
        "number": 2,
        "description": "difficult to walk over",
        "places": {
            "tunnel",
            "split",
            "dead end",
        },
        "clashes": set(),
        "settings": [
            "caves",
        ],
    },
    "chasm": {
        "number": 3,
        "description": "big hole",
        "places": {
            "tunnel",
            "split",
        },
        "clashes": {
            "entrance",
            "dead end",
        },
        "settings": [
            "caves",
        ],
    },
    "lake": {
        "number": 2,
        "description": "big hole with water",
        "places": {
            "tunnel",
            "split",
            "dead end",
        },
        "clashes": set(),
        "settings": [
            "caves",
            "mine",
        ],
    },
    "sunroof": {
        "number": 3,
        "description": "This area of the cave opens upwards, to the sunlight",
        "places": {
            "tunnel",
            "split",
            "dead end",
        },
        "clashes": {
            "entrance",
        },
        "settings": [
            "caves",
        ],
    },
    "river": {
        "number": 4,
        "description": "big hole with water",
        "places": {
            "tunnel",
            "split",
        },
        "clashes": {
            "dead end",
        },
        "settings": [
            "caves",
            "mine",
        ],
    },
    "mana lake": {
        "number": 1,
        "description": "sparkly magic cave",
        "places": {
            "split",
            "dead end",
        },
        "clashes": set(),
        "settings": [
            "caves",
        ],
    },
    "gas leak": {
        "number": 1,
        "description": "fissures of farts",
        "places": {
            "dead end",
            "end",
        },
        "clashes": {
            "entrance",
        },
        "settings": [
            "caves",
            "mine",
        ],
    },
    "tin seam": {
        "number": 1,
        "description": "long squiggly tin lines",
        "places": {
            "tunnel",
            "split",
            "dead end",
        },
        "clashes": {
            "entrance",
        },
        "settings": [
            "mine",
        ],
    },
    "silver seam": {
        "number": 1,
        "description": "long squiggly silver lines",
        "places": {
            "tunnel",
            "dead end",
        },
        "clashes": {
            "entrance",
        },
        "settings": [
            "mine",
        ],
    },
    "gold seam": {
        "number": 1,
        "description": "long squiggly gold lines",
        "places": {
            "dead end",
        },
        "clashes": {
            "entrance",
        },
        "settings": [
            "mine",
        ],
    },
    "platinum seam": {
        "number": 1,
        "description": "long squiggly platinum lines",
        "platinum seam": {
            "tunnel",
        },
        "clashes": {
            "entrance",
        },
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
        "number": 3,
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
        "number": 3,
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
        "number": 3,
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
            "sunroof",
            "dead end",
        },
        "places": {
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
    "worker's quarters": {
        "number": 1,
        "description": "",
        "races": {
            "dwarves",
        },
        "clashes": {
            "chasm",
            "mana lake",
            "fungal garden",
            "sunroof",
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
            "sunroof",
        },
        "places": {
            "alternative",
            "dead end",
            "end",
        },
    },
    "garden": {
        "number": 3,
        "description": "normal sunlit garden",
        "races": {
            "elves",
            "gnomes",
        },
        "clashes": set(),
        "places": {
            "entrance",
            "sunroof",
        },
    },
    "fungal garden": {
        "number": 2,
        "description": "placed by water",
        "races": {
            "dwarves",
            "elves",
            "gnomes",
        },
        "clashes": {
            "stallagmites",
        },
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
            "sunroof",
        },
        "places": {
            "alternative",
            "dead end",
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
            "sunroof",
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
        "number": 4,
        "description": "statues, mostly",
        "races": {
            "elves",
        },
        "clashes": {
            "sunroof",
        },
        "places": {
            "split",
            "end",
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
            "lake",
            "river",
            "sunroof",
        },
        "places": {
            "alternative",
            "dead end",
            "end",
        },
    },
    "runemaster's quarters": {
        "number": 1,
        "description": "Where a runemaster sleeps",
        "races": {
            "dwarves",
        },
        "clashes": {
            "sunroof",
        },
        "places": {
            "dead end",
            "end",
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
            "lake",
            "river",
        },
        "places": {
            "alternative",
            "dead end",
            "end",
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
            "sunroof",
        },
        "places": {
            "dead end",
            "alternative",
            "end",
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
            "lake",
            "river",
        },
        "places": {
            "alternative",
            "dead end",
            "end",
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
            "sunroof",
        },
        "places": {
            "dead end",
            "alternative",
            "end",
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
            "sunroof",
        },
        "places": {
            "dead end",
            "end",
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
            "sunroof",
        },
        "places": {
            "dead end",
        },
    },
    "shrine to Cale": {
        "number": 2,
        "description": "a large carving of a book, with a riddle written on it",
        "races": {
            "gnomes",
        },
        "clashes": {
            "stallagmites",
        },
        "places": {
            "tunnel",
            "dead end",
        },
    },
    "ancestors' shrine": {
        "number": 4,
        "description": "a tall stone, with a family tree carved from the bottom, upwards",
        "races": {
            "dwarves",
        },
        "clashes": {
            "stallagmites",
        },
        "places": {
            "tunnel",
            "entrance",
            "split",
        },
    },
}

