def makeDisplay(dungeon, x):
    square = "[ " + str(x) + ": " + ", ".join(dungeon[x]["features"])
    if "creatures" in dungeon[x]:
        square += r"\n" + ", ".join(dungeon[x]["creatures"])
    square += " ]"
    if dungeon[x]["height"] == 2:
        square += " { border-style: bold ;}"
    elif dungeon[x]["height"] == 0:
        square += " { border-style: dotted ;}"
    return square


def graph(dungeon):
    relations = []
    for x in range(2, len(dungeon)):
        for second in dungeon[x]["connections"]:
            leftName = makeDisplay(dungeon, x)
            rightName = makeDisplay(dungeon, second)
            relations.append(rightName + " <--> " + leftName)
    relations = list(set(relations))
    return relations
