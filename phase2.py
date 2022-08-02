from constructions import *

def civilize(dungeon):
    for x in range(1, len(dungeon)): 
        if dungeon[x]["name"] == "chasm":
            dungeon[x]["constructions"] = "bridge"
    return(dungeon)

