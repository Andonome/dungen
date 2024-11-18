import random

CIVILIZATIONS = [
    "elves",
    "dwarves",
    "gnomes"
]

DUNGEON_SETTINGS = [
    "mine",
    "caves"
]

INVADERS = [
    "nura",
    "necromancer"
]

RANDOM_DUNGEON_MIN_DEFAULT = 8
RANDOM_DUNGEON_MAX_DEFAULT = 30

#TODO replace print statements that showed randomly selected dungeon parameters

def roll_for_tn(tn : int) -> bool:
    print('roll_for_tn')
    """The TN function just rolls 2D6 to make choices."""
    roll = random.randint(1, 6) + random.randint(1, 6)
    print(f"tn: {type(tn)}")
    if roll >= tn:
        return True
    else:
        return False

def generate_dungeon_size(size_min : int = RANDOM_DUNGEON_MIN_DEFAULT, size_max : int = RANDOM_DUNGEON_MAX_DEFAULT):
    return random.randint(size_min, size_max)

def generate_dungeon_parameters(dungeon_size : int = None,
                                setting : str = None,
                                civilization : str = None,
                                invaders : str = None) -> dict:
    """ Generates dungeon parameters. Picks parameters at random from constants for parameters not given.
    Currently does not validate selections. """

    dungeon_parameters = {}

    if not dungeon_size:
        dungeon_size = generate_dungeon_size()
    if not setting:
        setting = random.choice(DUNGEON_SETTINGS)
    if not civilization:
        civilization = random.choice(CIVILIZATIONS)
    if not invaders:
        invaders = random.choice(INVADERS)

    dungeon_parameters["dungeon_size"] = dungeon_size
    dungeon_parameters["setting"] = setting
    dungeon_parameters["civilization"] = civilization
    dungeon_parameters["invaders"] = invaders

    return dungeon_parameters

def get_contents(dungeon, room_index):
    """Returns a set of what's in the room. Ignores duplicates."""
    contents = []
    for thing in dungeon[room_index]:
        if type(dungeon[room_index][thing]) == list:
            contents += dungeon[room_index][thing]
    return set(contents)


# Here the elves/dwarves/necromancers leave their stuff in
# places. Each one checks it's not classhing in some way,
# e.g. a library should not be placed over a river, and a
# cavern is no place to call home.


def placeContents(dungeon, featureList, contentType, civilization, tn=3):
    contentList = []
    n = 0
    while n < 5:
        totalRooms = list(range(n, len(dungeon)))
        for f in featureList:
            for x in totalRooms:
                contents = get_contents(dungeon, x)
                if (
                    n < featureList[f]["number"]
                    and roll_for_tn(tn + n)
                    and civilization in featureList[f]["races"]
                    and featureList[f]["places"].intersection(contents)
                    and featureList[f]["clashes"].isdisjoint(contents)
                    and f not in dungeon[x]["features"]
                ):
                    dungeon[x]["features"].append(f)
                    dungeon[x]["type"].append(contentType)
                    contentList.append(f)
                    totalRooms.remove(x)
                    break
        n += 1
    print(30 * "=" + contentType)
    print(contentList)
