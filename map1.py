import random
from areas import *

def noRepeat(map):
    for entry in range(0,len(map)-2):
        try:
            if map[entry] == map[entry+1]:
                map.remove(map[entry])
        except:
            pass

def chooseAreas(map):
    while len(map) < 10:
        for loc in areas:
            for no in range(areas[loc][0]):
                #if location in areas[loc][1]:
                    if random.randint(1,2) == 1 and len(map) < 18:
                        map.append(loc)
    random.shuffle(map)

def joinMap(map):
    map.insert(0,'entrance')
    noRepeat(map)
    for index, entry in enumerate(map):
        current = '[ ' + str(index) + ': ' + str(entry) + ' ]'
        connector=random.randint(index,len(map)-1)
        if connector > index and connector % 2 == 0:
            current += ' --> [ ' + str(connector) + ': ' + map[connector] +' ]'
        elif index < len(map) -1:
            current += ' --> [ ' + str(index +1) + ': ' + str(map[index + 1]) +' ]'
        print(current)

def makeMap(map):
    chooseAreas(map)
    noRepeat(map)
    joinMap(map)

