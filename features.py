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
            "split",
            "alternative",
            "river",
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
            "chasm",
            "river",
            "lake",
        ],
        "places": [
            "alternative",
            "split",
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
    "tomb": {
        "description": "dead people, with writing",
        "races": [
            "dwarves",
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
            "tunnel",
            "dead end",
        ],
    },
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
    "living quarters": {
        "description": "many halls, many beds.",
        "races": [
            "dwarves",
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
    "guard post": {
        "description": "OC, don't steal",
        "races": [
            "dwarves",
            "elves",
            "gnomes",
        ],
        "clashes": [
            "alternative",
        ],
        "places": [
            "split",
            "entrance",
        ],
    },
}
