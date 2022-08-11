# This mega-dictionary containts all the features,
# with a list of how common they are, a sub-list of where they might occur, and a description.

featureList = [
    "chasm",
    "lake",
    "river",
    "mana lake",
    "gas leak",
]

civilFeatures = {
    "bridge": {
        "description": "over troubled water",
        "races": [
            "dwarves",
            "elves",
            "gnomes",
        ],
        "clashes": [
            "alternative",
            "dead end",
        ],
        "places": [
            "chasm",
            "river",
        ],
    },
    "gas patches": {
        "description": "clay patches to stop gass vent",
        "races": [
            "dwarves",
            "elves",
            "gnomes",
        ],
        "clashes": [
            "entrance",
        ],
        "places": [
            "gas leak",
        ],
    },
    "boats": {
        "description": "over troubled water",
        "races": [
            "dwarves",
            "elves",
            "gnomes",
        ],
        "clashes": [
            "alternative",
            "dead end",
        ],
        "places": [
            "lake",
        ],
    },
    "guard post": {
        "description": "OC, don't steal",
        "races": [
            "dwarves",
            "elves",
            "gnomes",
        ],
        "clashes": [
            "alternative",
            "gas leak",
            "dead end",
        ],
        "places": [
            "split",
            "entrance",
        ],
    },
    "living quarters": {
        "description": "many halls, many beds.",
        "races": [
            "dwarves",
            "elves",
            "gnomes",
        ],
        "clashes": [
            "chasm",
            "lake",
            "mana lake",
            "river",
        ],
        "places": [
            "dead end",
            "alternative",
        ],
    },
    "servants' quarters": {
        "description": "",
        "races": [
            "dwarves",
        ],
        "clashes": [
            "chasm",
            "mana lake",
            "fungal garden",
        ],
        "places": [
            "dead end",
        ],
    },
    "kitchen": {
        "description": "",
        "races": [
            "dwarves",
            "elves",
            "gnomes",
        ],
        "clashes": [
            "mana lake",
            "lake",
            "chasm",
        ],
        "places": [
            "dead end",
            "alternative",
        ],
    },
    "fungal garden": {
        "description": "placed by water",
        "races": [
            "dwarves",
            "elves",
            "gnomes",
        ],
        "clashes": [],
        "places": [
            "lake",
            "river",
        ],
    },
    "armoury": {
        "description": "Mostly left arms",
        "races": [
            "dwarves",
            "elves",
            "gnomes",
        ],
        "clashes": [
            "chasm",
            "river",
            "lake",
            "mana lake",
        ],
        "places": [
            "dead end",
            "alternative",
        ],
    },
    "music hall": {
        "description": "hall for music ",
        "races": [
            "elves",
        ],
        "clashes": [],
        "places": [
            "split",
            "alternative",
            "dead end",
        ],
    },
    "art hall": {
        "description": "statues, mostly",
        "races": [
            "elves",
        ],
        "clashes": [],
        "places": [
            "split",
            "tunnel",
            "dead end",
        ],
    },
    "library": {
        "description": "library",
        "races": [
            "dwarves",
            "elves",
            "gnomes",
        ],
        "clashes": [],
        "places": [
            "alternative",
            "dead end",
        ],
    },
    "runemaster's quarters": {
        "description": "Where a runemaster sleeps",
        "races": [
            "dwarves",
        ],
        "clashes": [],
        "places": [
            "dead end",
        ],
    },
    "tomb": {
        "description": "dead people, with writing",
        "races": [
            "dwarves",
            "gnomes",
        ],
        "clashes": [],
        "places": [
            "alternative",
            "dead end",
        ],
    },
    "workshop": {
        "description": "many halls, many beds.",
        "races": [
            "dwarves",
            "gnomes",
        ],
        "clashes": [
            "chasm",
            "lake",
            "river",
        ],
        "places": [
            "dead end",
            "alternative",
        ],
    },
    "jail": {
        "description": "some prisoners did a naghty, and now they're here",
        "races": [
            "dwarves",
        ],
        "clashes": [
            "mana lake",
        ],
        "places": [
            "dead end",
        ],
    },
    "alchemy laboratory": {
        "description": "wizards gonna wizz",
        "races": [
            "gnomes",
        ],
        "clashes": [
            "chasm",
            "river",
            "lake",
        ],
        "places": [
            "dead end",
            "alternative",
        ],
    },
    "feasting hall": {
        "description": "Where everyone eats",
        "races": [
            "dwarves",
            "gnomes",
            "elves",
        ],
        "clashes": [
            "mana lake",
            "entrance",
            "chasm",
            "river",
            "lake",
        ],
        "places": [
            "alternative",
            "split",
        ],
    },
    "queen's room": {
        "description": "Where a king sleeps",
        "races": [
            "dwarves",
        ],
        "clashes": [
            "chasm",
        ],
        "places": [
            "dead end",
        ],
    },
    "vault": {
        "description": "Lots of shiny",
        "races": [
            "dwarves",
            "gnomes",
        ],
        "clashes": [
            "chasm",
            "lake",
        ],
        "places": [
            "dead end",
        ],
    },
    "shrine to Cale": {
        "description": "a large carving of a book, with a riddle written on it",
        "races": [
            "gnomes",
        ],
        "clashes": [],
        "places": [
            "tunnel",
            "dead end",
        ],
    },
    "shrine to Qualme": {
        "description": "a tall stone, with a family tree carved from the bottom, upwards",
        "races": [
            "dwarves",
        ],
        "clashes": [],
        "places": [
            "tunnel",
            "entrance",
            "split",
        ],
    },
}
