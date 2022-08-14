import random

# The TN function just rolls 2D6 to make choices.
def tn(tn):
    roll = random.randint(1, 6) + random.randint(1, 6)
    if roll >= tn:
        return True
    else:
        return False


# Just for debugging.
def show(x):
    pprint.pprint(x)


dunSize = random.randint(8, 30)
print("Size: " + str(dunSize))
setting = random.choice(["mine", "caves"])
print("Setting: " + setting)

civilizations = [
    "elves",
    "dwarves",
    "gnomes",
]

civilization = random.choice(civilizations)

race = civilization

print("Race: " + civilization)

# Sometimes you just want a big list  of what's in a room,
# e.g. ["river", "stone bridge", "tunnel"].
def getContents(dungeon, x):
    contents = []
    for thing in dungeon[x]:
        if type(dungeon[x][thing]) == list:
            contents += dungeon[x][thing]
    return set(contents)


def placeContents(dungeon, featureList, race=civilization):
    print(30 * "=")
    totalRooms = list(range(len(dungeon)))
    for f in featureList:
        for x in totalRooms:
            contents = getContents(dungeon, x)
            if (
                civilization in featureList[f]["races"]
                and featureList[f]["places"].intersection(contents)
                and featureList[f]["clashes"].isdisjoint(contents)
            ):
                dungeon[x]["features"].append(f)
                print(f)
                totalRooms.remove(x)
                break
