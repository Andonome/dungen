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
    "barracks": {
        "description": "",
        "races": [
            "dwarves",
            "elves",
        ],
        "clashes": ["tunnel"],
        "places": [
            "split",
            "tunnel",
        ],
    },
    "jail": {
        "description": "some prisoners did a naghty, and now they're here",
        "races": [
            "dwarves",
        ],
        "clashes": [],
        "places": [
            "dead end",
        ],
    },
    "queen's room": {
        "description": "Where a king sleeps",
        "races": [
            "dwarves",
        ],
        "clashes": [],
        "places": [
            "dead end",
        ],
    },
    "feast hall": {
        "description": "Where everyone eats",
        "races": [
            "dwarves",
            "gnomes",
            "elves",
        ],
        "clashes": [],
        "places": [
            "alternative",
        ],
    },
    "servants' quarters": {
        "description": "",
        "races": [
            "dwarves",
        ],
        "clashes": [],
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
        ],
        "places": [
            "split",
            "tunnel",
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
            "split",
            "tunnel",
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
            "tunnel",
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
            "tunnel",
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
        "clashes": [],
        "places": [
            "tunnel",
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
        "clashes": [],
        "places": [
            "tunnel",
            "entrance",
        ],
    },
}
