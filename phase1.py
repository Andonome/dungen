"""
Dungeon Generation Module

This module handles the generation and modification of dungeon layouts, including:
- Room connections and structure
- Room type labeling (dead ends, tunnels, etc.)
- Feature placement
- Entrance/exit handling
- Alternative path marking

A dungeon is represented as a list of room dictionaries, where each room has:
- connections: List of relative offsets to connected rooms
- features: List of environmental features
- creatures: List of creatures in the room
- type: List of room type labels

Future Development Notes:
    Settings and configuration could be moved to YAML files, for example:

    dungeon_settings:
        - resource_type: dungeon_setting
          name: mine
          join_chance: 5
        - resource_type: dungeon_setting
          name: caves
          join_chance: 9

    This will allow for easier configuration of dungeon attributes without
    code changes. With all resources set up like this, we can even later convert stat blocks and other things like that
    into YAML files, making production even faster.  Imagine just... importing the player handbook or additional books.

"""


import random
from features import primative_features
from vars import roll_for_tn

def report_dungeon_stats(dungeon):
    """
    Generates a summary report of dungeon statistics.

    Args:
        dungeon (list): The complete dungeon structure

    Returns:
        dict: Statistics about the dungeon
    """
    stats = {
        "total_rooms": len(dungeon),
        "entrances": sum(1 for room in dungeon if "entrance" in room["type"]),
        "dead_ends": sum(1 for room in dungeon if "dead end" in room["type"]),
        "hidden_rooms": sum(1 for room in dungeon if "hidden" in room["type"]),
        "features": {
            room_index: room["features"]
            for room_index, room in enumerate(dungeon)
            if room["features"]
        }
    }

    # Print the report
    print("\nDungeon Generation Report:")
    print(f"Total Rooms: {stats['total_rooms']}")
    print(f"Entrances: {stats['entrances']}")
    print(f"Dead Ends: {stats['dead_ends']}")
    print(f"Hidden Rooms: {stats['hidden_rooms']}")

    if stats['features']:
        print("\nFeatures by Room:")
        for room_index, features in stats['features'].items():
            print(f"Room {room_index}: {', '.join(features)}")

    return stats


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
    print(f"join_chance: {type(join_chance)}")

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
    print("join_room")
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
            # Unpacking and catching the dungeon that we're not using to prevent catching both as a tuple
            join_chance, _ = join_room(dungeon, room_index, join_chance)
    return join_chance, dungeon

def add_features(dungeon, setting):
    """
    Adds environmental features (like chasms or mana lakes) to dungeon rooms.

    Algorithm:
    1. First collects potential features that:
       - Pass a difficulty 6 roll
       - Are valid for the given setting
       - Haven't exceeded their maximum instances
    2. Then distributes these features randomly through the dungeon,
       spacing them out by 1-6 rooms each time

    Args:
        dungeon (list): List of room dictionaries containing features lists
        setting (str): Dungeon setting (e.g., "mine", "dungeon") to filter valid features

    Returns:
        list: The dungeon with added features
    """

    def collect_valid_features():
        """Gathers features valid for this setting, limited by their max instances."""
        valid_features = []
        feature_counts = {feature: 0 for feature in primative_features}

        for _ in range(5):  # Try to add up to 5 features
            for feature_name in primative_features:
                feature = primative_features[feature_name]
                if (roll_for_tn(6) and
                        setting in feature["settings"] and
                        feature_counts[feature_name] < feature["number"]):
                    valid_features.append(feature_name)
                    feature_counts[feature_name] += 1

        return valid_features

    def distribute_features(features):
        """Places features in dungeon rooms with random spacing."""
        current_room = -1

        for feature in features:
            # Skip ahead 1-6 rooms
            current_room += random.randint(1, 6)

            # If we're still in the dungeon, add the feature
            if current_room < len(dungeon) - 1:
                dungeon[current_room]["features"].append(feature)
                print(f"Added {feature} to room {current_room}")

    selected_features = collect_valid_features()
    distribute_features(selected_features)

    return dungeon

def label_rooms(dungeon):
    """
    Labels rooms based on their connections to other rooms.

    Room types:
    - "dead end": Room with only one connection
    - "split": Room with more than two connections
    - "tunnel": Room with exactly two connections
    - "end": The final room in the dungeon

    Args:
        dungeon (list): List of room dictionaries containing connections and types

    Returns:
        list: The modified dungeon. Not necessary but will make refactoring easier.
    """
    # Mark the last room as the end
    dungeon[-1]["type"].append("end")

    # Initial room type assignment based on connections
    for room in dungeon:
        if len(room["connections"]) == 1:
            room["type"].append("dead end")
        elif len(room["connections"]) > 2:
            room["type"].append("split")
        else:
            room["type"].append("tunnel")

    # Update connected rooms' types
    for i, room in enumerate(dungeon):
        for connection in room["connections"]:
            connected_room = dungeon[i + connection]

            # Remove dead end status if room is connected to
            if "dead end" in connected_room["type"]:
                connected_room["type"].remove("dead end")

            # Update tunnel/split status
            if "tunnel" in connected_room["type"]:
                connected_room["type"].remove("tunnel")
                if "split" not in connected_room["type"]:
                    connected_room["type"].append("split")
            elif "split" not in connected_room["type"]:
                connected_room["type"].append("tunnel")

    return dungeon

def convert_dead_ends(dungeon):
    """
    Converts some dead ends into entrances or hidden rooms.
    Ensures at least one entrance exists, then may add more.

    Algorithm:
    1. Ensures at least one entrance exists by converting a dead end if needed
    2. May convert one more dead end to a new entrance (with probability based on remaining dead ends)
    3. Then tries to convert remaining dead ends into hidden rooms

    Hidden rooms:
    - Are former dead ends
    - Their entry point becomes marked as a dead end instead
    - Only created if the entry point isn't already a split

    Args:
        dungeon (list): List of room dictionaries containing types and connections

    Returns:
        list: The modified dungeon with converted dead ends
    """

    def convert_to_entrance(room):
        """Converts a dead end room into an entrance."""
        room["type"].remove("dead end")
        if "end" in room["type"]:
            room["type"].remove("end")
        room["type"].append("entrance")
        return room

    def convert_to_hidden(dead_end_index, entry_room):
        """Converts a dead end into a hidden room and marks its entry point."""
        room = dungeon[dead_end_index]
        room["type"].remove("dead end")
        if "end" in room["type"]:
            room["type"].remove("end")
        room["type"].append("hidden")
        entry_room["type"].append("dead end")
        print(f"Hidden room: {dead_end_index}")

    def has_entrance():
        """Check if dungeon has at least one entrance."""
        return any("entrance" in room["type"] for room in dungeon)

    # Find all dead ends
    dead_end_indices = [
        i for i, room in enumerate(dungeon)
        if "dead end" in room["type"]
    ]

    # Ensure at least one entrance exists
    entrance_count = 0
    if not has_entrance() and dead_end_indices:
        new_entrance_index = random.choice(dead_end_indices)
        dead_end_indices.remove(new_entrance_index)
        dungeon[new_entrance_index] = convert_to_entrance(
            dungeon[new_entrance_index]
        )
        entrance_count = 1
    else:
        entrance_count = sum(1 for room in dungeon if "entrance" in room["type"])

    # Maybe add one more entrance
    if roll_for_tn(9 - len(dead_end_indices)) and dead_end_indices:
        new_entrance_index = random.choice(dead_end_indices)
        dead_end_indices.remove(new_entrance_index)
        dungeon[new_entrance_index] = convert_to_entrance(
            dungeon[new_entrance_index]
        )
        entrance_count += 1

    # Try to convert remaining dead ends to hidden rooms
    for dead_end_index in dead_end_indices:
        entry_index = dead_end_index + dungeon[dead_end_index]["connections"][0]
        entry_room = dungeon[entry_index]

        if roll_for_tn(4 + len(dead_end_indices)) and "split" not in entry_room["type"]:
            convert_to_hidden(dead_end_index, entry_room)

    # Status report
    print(f"Dead ends: {len(dead_end_indices)}")
    print(f"Entrances: {entrance_count}")

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

def generate_initial_layout(setting : str, dungeon_size : int):
    dungeon = initialize_dungeon(setting, dungeon_size)
    dungeon = label_rooms(dungeon)
    dungeon = label_alternatives(dungeon)
    dungeon = convert_dead_ends(dungeon)
    dungeon = add_features(dungeon, setting)
    report_dungeon_stats(dungeon)
    # makeRiver(dungeon)
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