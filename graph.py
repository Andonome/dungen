def graph(dungeon):
    relations = []
    for x in range(2, len(dungeon)):
        for second in dungeon[x]["connections"]:
            leftName = "[ " + str(x) + ": " + dungeon[x]["name"]
            if "constructions" in dungeon[x]:
                leftName += " (" + ", ".join(dungeon[x]["constructions"]) + ")"
            leftName += " ]"
            rightName = "[ " + str(second) + ": " + dungeon[second]["name"]
            if "constructions" in dungeon[second]:
                rightName += " (" + ", ".join(dungeon[second]["constructions"]) + ")"
            rightName += " ]"
            if dungeon[x]["height"] == 2:
                rightName += " { border: bold; } "
            elif dungeon[x]["height"] == 0:
                rightName += " { border: dotted; } "
            relations.append(rightName + " <--> " + leftName)
    relations = list(set(relations))
    return relations
