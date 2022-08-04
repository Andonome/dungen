# This mega-dictionary containts all the areas,
# with a list of how common they are, a sub-list of where they might occur, and a description.

areas = {
    "entrance": {
        "name": "entrance",
        "number": 2,
        "constructions": [],
        "ecosystems": ["deep", "mine", "caves"],
        "height": 1,
        "description": """
This is where people come in.

Hopefully there will be at least one entrance.
""",
    },
    "tunnel": {
        "name": "tunnel",
        "number": 6,
        "constructions": [],
        "ecosystems": ["deep", "mine", "caves"],
        "description": """
Long tube.

Hopefully doesn't go nowhere.
""",
    },
    "lavapit": {
        "name": "lavapit",
        "number": 2,
        "constructions": [],
        "ecosystems": ["deep"],
        "description": """
Get it while it's hot.
""",
    },
    "manaLake": {
        "name": "mana lake",
        "number": 1,
        "constructions": [],
        "ecosystems": ["deep", "keep"],
        "description": """
This magical area spills out mana constantly.

It probably contains a magical trap, fuelled by the mana.
""",
    },
    "cavern": {
        "name": "cavern",
        "number": 6,
        "constructions": [],
        "ecosystems": ["deep", "caves", "mine"],
        "description": """
It's a big cavern.

With stuff.

    """,
    },
}

# These areas need other variables for later, like 'connections' and

for x in areas:
    areas[x]["connections"] = []
    areas[x]["constructions"] = []
