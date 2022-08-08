import graphviz


def graph(dungeon):
    dunMap = graphviz.Digraph(
        engine="dot",
        comment="Test Map",
    )
    dunMap.attr("node", shape='egg',overlap='false')
    for x in range(len(dungeon)):
        roomShape = 'ellipse'
        contents = str(x) + ": \n" + "\n ".join(dungeon[x]["features"])
        if len(dungeon[x]["creatures"]) > 0:
            contents += "\n" + "\n".join(dungeon[x]["creatures"])
        if len(dungeon[x]["type"]) > 0:
            contents += "(" + ", ".join(dungeon[x]["type"]) + ")"
        if "mana lake" in dungeon[x]["features"]:
            roomShape = "star"
        elif "entrance" in dungeon[x]["type"]:
            roomShape = "doublecircle"
        elif "split" in dungeon[x]["type"]:
            roomShape = "hexagon"
        elif "dead end" in dungeon[x]["type"]:
            roomShape = "invhouse"
        dunMap.node(str(x), contents,shape=roomShape)
        for connection in dungeon[x]["connections"]:
            dunMap.edge(str(x), str(connection))
    dunMap.render("Test Map.gv")
