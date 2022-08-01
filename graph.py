def graph(dungeon):
    for x in range(2, len(dungeon)):
        for second in dungeon[x]["connections"]:
            print(
                "[ "
                + str(second)
                + ": "
                + dungeon[second]["name"]
                + " ]"
                + " --> "
                + "[ "
                + str(x)
                + ": "
                + dungeon[x]["name"]
                + " ]"
            )
