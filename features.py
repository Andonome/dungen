# This mega-dictionary containts all the features,
# with a list of how common they are, a sub-list of where they might occur, and a description.

featureList = [
    "chasm",
    "lake",
    "river",
    "mana lake",
    "gas leak",
    "drop",
    "steep",
]

civilFeatures = {
    "barracks": {
        "description": "",
        "races": [
            "dwarves",
            "elves",
        ],
        "places": [
            "split",
            "tunnel",
        ],
    },
    "kitchen": {
        "description": "",
        "races": [
            "dwarves",
            "elves",
            "gnomes",
        ],
        "places": [
            "split",
            "tunnel",
        ],
    },
    "library": {
        "description": "library",
        "races": [
            "dwarves",
            "elves",
            "gnomes",
        ],
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
        "places": [
            "split",
            "tunnel",
            "dead end",
        ],
    },
    "fungal garden": {
        "description": "placed by water",
        "races": [
            "dwarves",
            "elves",
            "gnomes",
        ],
        "places": [],
    },
}
