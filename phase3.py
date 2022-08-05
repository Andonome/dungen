# Goblins rooms  should include:
#
# - hatchery in
# - traps
# - hobgoblins
# - food storage
# - traps

import random

goblinRampage = [
    ["lake", "ooze"],
    ["kitchen", "foodStore"],
]


def breakRooms(dungeon):
    for x in range(len(dungeon) - 1, 0, -1):
        for pair in range(len(goblinRampage)):
            if goblinRampage[pair][0] in dungeon[x]["features"]:
                dungeon[x]["features"].append(goblinRampage[pair][1])


def makeGoblins(dungeon):
    # First let's see how big the dungeon is - larger dungeons
    # should house most goblins, and having a fungal garden
    # should also increase their number.
    goblinNo = int(len(dungeon) / 3)
    for x in range(1, len(dungeon) - 1):
        gobEnc = random.randint(1, goblinNo)
        if "fungus" in dungeon[x]["features"]:
            goblinNo += 1
            dungeon[x]["creatures"].append("ooze")
        elif "lake" in dungeon[x]["features"]:
            dungeon[x]["creatures"].append("ooze")
        elif "river" in dungeon[x]["features"]:
            pass
        elif gobEnc > 5:
            dungeon[x]["creatures"].append(str(random.randint(1, 4)) + " ogres")
        elif goblinNo > 4:
            dungeon[x]["creatures"].append(
                str(random.randint(1, goblinNo)) + " hobgoblins"
            )
        elif goblinNo > 2:
            dungeon[x]["creatures"].append(
                str(random.randint(1, goblinNo * 2)) + " goblins"
            )
        else:
            pass


def rampage(dungeon):
    breakRooms(dungeon)
    makeGoblins(dungeon)
