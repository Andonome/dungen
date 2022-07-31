import random
from areas import *

# Remove sequential repeats, e.g. 'entrance, entrance'
def noRepeat(map):
    for entry in range(0,len(map)-2):
        try:
            if map[entry] == map[entry+1]:
                map.remove(map[entry])
        except:
            pass

# Take all possible locations in 'areas.py' and construct a random 
# room list.
def chooseAreas(map):
    while len(map) < 10:
        for loc in areas:
            for no in range(areas[loc][0]):
                #if location in areas[loc][1]:
                    if random.randint(1,2) == 1 and len(map) < 18:
                        map.append(loc)
    random.shuffle(map)
    map.insert(0,'entrance')

# Create a list of which room connects to which, e.g.
# [[1,2],[2,5],[3,6]].
def joinMap(map):
    current = []
    for index in range(0,len(map)-1):
        connector=random.randint(index,len(map)-1)
        if connector > index and map[index] != map[connector]:
                current.insert(-1,[index,connector])
        elif index < len(map)-1 and map[index] != map[connector]:
            current.insert(-1,[index,index+1])
    return(current)

# Super-function
def makeMap(map):
    chooseAreas(map)
    noRepeat(map)
    roomList = joinMap(map)
    return roomList

