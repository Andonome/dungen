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

def roll_for_tn(tn : int) -> bool:
    """The TN function just rolls 2D6 to make choices."""
    roll = random.randint(1, 6) + random.randint(1, 6)

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

    print("== Dungeon parameters set ==")
    print(f"Size: {dungeon_size}")
    print(f"Setting: {setting}")
    print(f"Civilization: {civilization}")
    print(f"Invaders: {invaders}")
    print("="*30)



    return dungeon_parameters

def get_contents(dungeon, room_index):
    """Returns a set of what's in the room. Ignores duplicates."""
    contents = []
    for thing in dungeon[room_index]:
        if type(dungeon[room_index][thing]) == list:
            contents += dungeon[room_index][thing]
    return set(contents)

def place_contents(dungeon, feature_list, content_type, civilization, tn=3):
    """
    Places features from a civilization in valid dungeon rooms.

    Here the elves/dwarves/necromancers leave their stuff in places. Each one checks it's not clashing in some way,
    e.g. a library should not be placed over a river, and a cavern is no place to call home.

    Args:
        dungeon (list): The dungeon to place contents in
        feature_list (dict): Features that can be placed
        content_type (str): Type of content being placed
        civilization (str): Who is placing the contents
        tn (int): Target number for placement rolls, defaults to 3

    Returns:
        list: The modified dungeon
    """
    placed_features = []
    attempts = 0

    while attempts < 5:
        available_rooms = list(range(attempts, len(dungeon)))
        for feature_name in feature_list:
            for room_index in available_rooms:
                room_contents = get_contents(dungeon, room_index)
                feature = feature_list[feature_name]

                if (attempts < feature["number"] and
                        roll_for_tn(tn + attempts) and
                        civilization in feature["races"] and
                        feature["places"].intersection(room_contents) and
                        feature["clashes"].isdisjoint(room_contents) and
                        feature_name not in dungeon[room_index]["features"]):
                    dungeon[room_index]["features"].append(feature_name)
                    dungeon[room_index]["type"].append(content_type)
                    placed_features.append(feature_name)
                    available_rooms.remove(room_index)
                    break
        attempts += 1

    print("=" * 30 + content_type)
    print(placed_features)

    return dungeon
