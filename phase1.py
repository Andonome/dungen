import random

from features import primitiveFeatures
from vars import roll_for_tn

#TODO: Replace print statements reporting dead ends and entrances


def get_join_chance(setting : str) -> int:
    """
    Until this is an attribute of an object, separating this out into its own function
    will make it easier to refactor later.  Sets join change to '5' if the setting is not known, as 5
    is a known-good number

    Args:
        setting (string): The dungeon setting, such as 'caves' or 'mine'

    Returns:
        join_chance (int): The join chance, to be rolled against TN

    """

    """ Later, we can create 'settings' objects which can hold these attributes, and we can load them in from
    YAML files.  Might look like this:
    
    dungeon_settings:
        - resource_type: dungeon_setting
          name: mine
          join_chance: 5
        - resource_type: dungeon_setting
          name: caves
          join_chance: 9
        
    Plus any other attributes you'd want in there. Later though.
    
    
    """

    setting_join_chance = {"mine":5,
                           "caves":9}

    return setting_join_chance.get(setting, 5)


def initialize_dungeon(setting: str, dungeon_size: int):
    """
    Initializes a new dungeon by its size, joining rooms based on its settings attribute for join chance.
    A dungeon is a list of rooms that contain attribute dictionaries.

    Args:
        setting (string): The dungeon setting, such as 'caves' or 'mine'
        dungeon_size (int): The size, in rooms, of the dungeon.

    Returns:
        dungeon (list): Returns the dungeon.

    """
    join_chance = get_join_chance(setting)

    dungeon = [
        {
            "connections": [],
            "features": [],
            "creatures": [],
            "type": []
        }
        for _ in range(dungeon_size)
    ]

    for room_index in range(dungeon_size):
        join_chance, dungeon = join_room(dungeon, room_index, join_chance)

    return dungeon

def join_room(dungeon, room_index : int, join_chance : int):
    """
    Joins dungeon pieces, usually straight down (4 -- > 3), but sometimes skips down (7 --> 3).
    Each connection is relative, so 'dungeon[3]["connection"] = -1' means that room 3 is connected to 2 (3-1 = 2), and
    'dungeon[5]["connection"] = -3' means that room 5 is connected to room 2 (5-3 = 2).

    Args:
        dungeon (list): A list of rooms containing a dictionary of room attributes
        room_index (int): The index number of the room in the dungeon
        join_chance (int): The chance for a room to be joined.

    Returns:
        join_chance (int): The updated join chance
        dungeon (list): The updated dungeon

    """


    if room_index == 0:
        dungeon[room_index]["type"].append("entrance")
    # Initial rooms (0 to 4) connect to the room before.  After
    # that, there's a chance they connect straight down.
    elif len(dungeon[room_index]["connections"]) > 1:
        pass
    elif room_index < 3:
        dungeon[room_index]["connections"].append(-1)
    elif roll_for_tn(join_chance):
        join_chance += 2
        if -1 not in dungeon[room_index]["connections"]:
            dungeon[room_index]["connections"].append(-1)
    else:
        join_chance -= 2
        low_point = (room_index - 1) * -1
        join = random.randint(max(low_point, -4), -2)
        if join not in dungeon[room_index]["connections"]:
            dungeon[room_index]["connections"].append(join)
        if roll_for_tn(join_chance + 1):
            join_chance = join_room(dungeon, room_index, join_chance)
    return join_chance, dungeon


# Now the dungeon gets features, like 'chasm', or 'mana
# lakes'.
# These come from the 'primitiveFeatures' list, then each one is checked to see if it fits in the current 'setting' ("mine", or "dungeon").
# If so, it's added to the list.
# We then skip along the dungeon's rooms randomly dropping
# our list-items: 1,3,5,11,13,14.


def giveFeatures(dungeon, setting):
    localFeatures = []
    # n tracks features which have multiple
    n = 0
    while n < 5:
        for f in primitiveFeatures:
            if (
                roll_for_tn(6)
                and setting in primitiveFeatures[f]["settings"]
                and n < primitiveFeatures[f]["number"]
            ):
                localFeatures.append(f)
        n += 1
    x = -1
    for f in localFeatures:
        x += random.randint(1, 6)
        if x < len(dungeon) - 1:
            dungeon[x]["features"].append(f)
            print(f)


def label_rooms(dungeon):
    """
    Labels rooms in a dungeon based on their connections to other rooms.

    Room types:
    - "entrance": The first room in the dungeon
    - "end": The final room in the dungeon
    - "dead end": Room with only one connection (excluding entrance/exit)
    - "split": Room with more than two connections
    - "tunnel": Room with exactly two connections

    Args:
        dungeon (list): List of room dictionaries

    Returns:
        dungeon (list): Returns the dungeon. Not necessary but will make refactoring easier.
    """

    def get_initial_room_type(connections, is_special_room):
        """
        Determines the initial room type based on number of connections.
        Special rooms (entrance/exit) are not marked as dead ends.
        """
        if is_special_room:
            return "tunnel" if len(connections) == 2 else "split"

        num_connections = len(connections)
        if num_connections == 1:
            return "dead end"
        elif num_connections > 2:
            return "split"
        return "tunnel"

    def update_connected_room_type(room):
        """Updates room type based on its role in the dungeon layout. Updates dead ends."""
        if "dead end" in room["type"] and "entrance" not in room["type"] and "end" not in room["type"]:
            room["type"].remove("dead end")

        if "tunnel" in room["type"]:
            room["type"].remove("tunnel")
            if "split" not in room["type"]:
                room["type"].append("split")
        elif "split" not in room["type"]:
            room["type"].append("tunnel")

    # Mark entrance and exit
    dungeon[0]["type"].append("entrance")
    dungeon[-1]["type"].append("end")

    # Initial room type assignment
    for i, room in enumerate(dungeon):
        is_special_room = i == 0 or i == len(dungeon) - 1  # entrance or exit
        room_type = get_initial_room_type(room["connections"], is_special_room)
        room["type"].append(room_type)

    # Update connected rooms' types
    for i, room in enumerate(dungeon):
        for connection in room["connections"]:
            connected_room = dungeon[i + connection]
            update_connected_room_type(connected_room)

    return dungeon

# turn one dead end into an entrance
def deadEndsConversion(dungeon):
    endPoints = []
    totalEntrances = 1
    for x in range(len(dungeon)):
        if "dead end" in dungeon[x]["type"]:
            endPoints.append(x)
    maxEnds = int(len(dungeon) / 10)
    for _ in range(maxEnds):
        if roll_for_tn(9 - len(endPoints)) and len(endPoints) > 0:
            newEntrance = random.choice(endPoints)
            endPoints.remove(newEntrance)
            dungeon[newEntrance]["type"].remove("dead end")
            if "end" in dungeon[newEntrance]["type"]:
                dungeon[newEntrance]["type"].remove("end")
            dungeon[newEntrance]["type"].append("entrance")
            totalEntrances += 1
        else:
            break
        break
    for x in endPoints:
        entryway = x + dungeon[x]["connections"][0]
        if roll_for_tn(4 + len(endPoints)) and "split" not in dungeon[entryway]["type"]:
            dungeon[x]["type"].remove("dead end")
            dungeon[x]["type"].append("hidden")
            dungeon[entryway]["type"].append("dead end")
            if "end" in dungeon[x]["type"]:
                dungeon[x]["type"].remove("end")
            print("Hidden room: " + str(x))
    print("Dead ends: " + str(len(endPoints)))
    print("Entrances: " + str(totalEntrances))


def generate_initial_layout(setting : str, dungeon_size : int):
    dungeon = initialize_dungeon(setting, dungeon_size)
    dungeon = label_rooms(dungeon)
    dungeon = label_alternatives(dungeon)
    deadEndsConversion(dungeon)
    giveFeatures(dungeon, setting)
    # makeRiver(dungeon)
    return dungeon


def find_exit(dungeon, start=None):
    """
    Finds a path from a given room to the entrance (room 0).
    Returns the shorter path between:
    - Always taking first available connection
    - Always taking last available connection

    Dungeon not returned as it is not modified.

    Args:
        dungeon (list): List of room dictionaries with connections
        start (int, optional): Starting room number. If None, starts from last room.

    Returns:
        list: Room indexes forming the shorter path to the entrance
    """
    # Use last room as default starting point
    current = len(dungeon) - 1 if start is None else start

    # Try path using first connections
    path1 = [current]
    room = current
    while room > 0:
        room = room + dungeon[room]["connections"][0]
        path1.append(room)

    # Try path using last connections
    path2 = [current]
    room = current
    while room > 0:
        room = room + dungeon[room]["connections"][-1]
        path2.append(room)

    # Return the shorter path
    return path1 if len(path1) <= len(path2) else path2


def label_alternatives(dungeon):
    """
    Labels paths that might be suitable for traps (non-critical paths).
    First marks all non-dead-ends as alternative routes, then removes
    this label from one valid path to the exit.

    Args:
        dungeon (list): List of room dictionaries

    Returns:
        list: The modified dungeon with alternative paths labeled. Not neccesary, but will make refactoring easier later.


    Races can only place an impassable trap (like a swinging sphere of annihilation) in tunnels which form alternative
    routes - not the only route to a place, or nobody would be able to go to the toilet. Therefore, we find and label
    all the alternative passages (which you don't have to go through).

    Actually, we just label everything an 'alternative', then go to every dead-end, and find the route to the exit, and
    remove the label of 'alternative'. Anything which remains with the label must really be an alternative, because
    nobody needs it to reach the exit.

    """
    # Mark all non-dead-ends as potential alternatives
    for room in dungeon:
        if "dead end" not in room["type"]:
            room["type"].append("alternative")

    # Remove alternative label if the room connects to a dead end.
    for i, room in enumerate(dungeon):
        if len(room["connections"]) == 1:
            connected_room = i + room["connections"][0]
            if "alternative" in dungeon[connected_room]["type"]:
                dungeon[connected_room]["type"].remove("alternative")

    # Find a path to the exit, remove alternative label from that path.
    for room_index in find_exit(dungeon):
        if "alternative" in dungeon[room_index]["type"]:
            dungeon[room_index]["type"].remove("alternative")

    return dungeon


# I've never used this function, but I still like it. It
# finds a route from room x to room y.


# def findRoute(dungeon, x, y):
#     x = findExit(dungeon, x)
#     y = findExit(dungeon, y)
#     while x[-1] == y[-1]:
#         join = x[-1]
#         x.remove(x[-1])
#         y.remove(y[-1])
#         if len(x) * len(y) == 0:
#             break
#     x.append(join)
#     y.reverse()
#     x += y
#     return x