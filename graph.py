def graph(dungeon):
    relations = []
    for x in range(2, len(dungeon)):
        for second in dungeon[x]["connections"]:
            relations.append(
                "[ "
                + str(second)
                + ": "
                + dungeon[second]["name"]
                + " ]"
                + " <--> "
                + "[ "
                + str(x)
                + ": "
                + dungeon[x]["name"]
                + " ]"
            )
    relations = list(set(relations))
    return relations
