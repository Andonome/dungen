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
    "guard post": {
        "number": 3,
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
    "workers' quarters": {
        "number": 1,
        "description": "",
        "races": {
            "dwarves",
        },
        "clashes": {
            "chasm",
            "lake",
            "river",
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
        "clashes": {
            "chasm",
        },
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
            "alternative",
            "dead end",
            "end",
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
            "lake",
            "river",
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
        "description": "Where a queen sleeps",
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
    "throne room": {
        "number": 1,
        "description": "Where a monarch sits",
        "races": {
            "dwarves",
        },
        "clashes": {
            "river",
            "sunroof",
        },
        "places": {
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
        "number": 2,
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
    "blessings of the rocks": {
        "number": 1,
        "description": "Magical slab. Blesses the onlooker with the additional Crafts abilities.",
        "races": {
            "dwarves",
        },
        "clashes": {
            "river",
        },
        "places": {
            "mana lake",
        },
    },
}

for f in civilFeatures:
    civilFeatures[f]["clashes"].add("civilized")

mobilityFeatures = {
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
            "stone bridge",
        },
        "places": {
            "chasm",
            "river",
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
}

treasures = {
    "alchemical book": {
        "number": 2,
        "description": "don't ruin the ending",
        "races": {
            "gnomes",
        },
        "places": {
            "library",
        },
        "clashes": {
            "hobgoblins",
        },
    },
    "saphire crown": {
        "number": 1,
        "description": "big shiny",
        "races": {
            "dwarves",
        },
        "places": {
            "queen's room",
        },
        "clashes": {
            -4,
        },
    },
    "dragon statue": {
        "number": 1,
        "description": "Great big dragon statue. Gemstones for eyes. Weight Rating 12.",
        "races": {
            "dwarves",
        },
        "places": {
            "runemaster's quarters",
        },
        "clashes": {
            -4,
        },
    },
    "poetry book": {
        "number": 4,
        "description": "Famous author. Hates himself.",
        "races": {
            "dwarves",
            "elves",
        },
        "places": {
            "living quarters",
            "library",
            "music hall",
        },
        "clashes": {
            "gas patch",
        },
    },
    "portrait": {
        "number": 3,
        "description": "Famous elf, killing a dragon.",
        "races": {
            "elves",
            "gnomes",
        },
        "places": {
            "living quarters",
            "library",
            "tunnel",
        },
        "clashes": {
            "gas patch",
            "lake",
            "river",
        },
    },
    "fancy dagger": {
        "number": 3,
        "description": "Shiny and practical",
        "races": {
            "elves",
            "gnomes",
        },
        "places": {
            "living quarters",
            "library",
            "kitchen",
        },
        "clashes": {
            "gas patch",
        },
    },
    "illusion play altar": {
        "number": 1,
        "description": "Magical altar. Give it a book, it recrats the contents with illusions.",
        "races": {
            "gnomes",
        },
        "clashes": {
            "stallagmites",
        },
        "places": {
            "mana lake",
        },
    },
}

specialDoors = {
    "real fake door": {
        "number": 1,
        "description": "This ornate stone carving of a door looks very convincing, but it does nothing.  The real door lies to the side, disguised by shadows, ivy, and assumptions.",
        "races": {
            "elves",
        },
        "clashes": {
            "living quarters",
            "alternative",
        },
        "places": {
            "civilized",
        },
    },
    "teamwork door": {
        "number": 1,
        "description": "This heavy door has three handles which must be turned at once, all in different locations.",
        "races": {
            "gnomes",
        },
        "clashes": {
            "lake",
            "alternative",
        },
        "places": {
            -1,
        },
    },
    "rune door": {
        "number": 1,
        "description": "Speak the password in dwarvish to enter.",
        "races": {
            "dwarves",
        },
        "clashes": {
            "lake",
            "alternative",
        },
        "places": {
            "mana lake",
        },
    },
}
