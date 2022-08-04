#Goblins rooms  should include: 
#
#- hatchery in 
#- traps
#- hobgoblins
#- food storage
#- traps

goblinRampage = [
    ["lake", "ooze"],
    ["kitchen", "foodStore"],
]


def breakRooms(dungeon):
    for x in range(len(dungeon) - 1, 0, -1):
        for pair in range(len(goblinRampage)):
            if goblinRampage[pair][0] in dungeon[x]["features"]:
                dungeon[x]["features"].append(goblinRampage[pair][1])


def rampage(dungeon):
    breakRooms(dungeon)

