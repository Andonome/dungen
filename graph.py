# This function uses graphviz to output the map to a pdf file.
import graphviz


def graph(dungeon, setting, civilization):
    dunMap = graphviz.Digraph(
        engine="dot",
        comment="Test Map",
    )
    dunMap.attr(
        "node",
        # shape="record",
        overlap="scale",
        rotate="90",
        splines="polyline",
        penwidth="10",
    )

    dunMap.attr(
        "edge",
        penwidth="10",
        overlap="false",
        arrowhead="none",
    )
    title = setting + r"\n of the something\n something " + civilization
    dunMap.node(title, shape="tripleoctagon", fontsize="30")
    for x in range(len(dungeon)):
        roomShape = "ellipse"
        contents = str(x) + r": \n" + r"\n ".join(dungeon[x]["features"])
        if len(dungeon[x]["creatures"]) > 0:
            contents += r"\n" + r"\n".join(dungeon[x]["creatures"])
        #        if len(dungeon[x]["type"]) > 0:
        #            contents += "(" + ", ".join(dungeon[x]["type"]) + ")"
        if "mana lake" in dungeon[x]["features"]:
            shape = "Mdiamond"
        elif "entrance" in dungeon[x]["type"]:
            roomShape = "doublecircle"
            contents += r"\n(entrance)"
        elif "split" in dungeon[x]["type"]:
            roomShape = "hexagon"
        elif "dead end" in dungeon[x]["type"]:
            roomShape = "invhouse"
        if "living quarters" in dungeon[x]["features"]:
            roomShape = "record"
            contents = (
                " { Room | Room | Room | Room } |"
                + str(x)
                + ": "
                + "living'&#92;nquarters"
                + "| { Room | Room | Room | Room }"
            )
        elif "servants' quarters" in dungeon[x]["features"]:
            roomShape = "record"
            contents = (
                " { Room | Room | Room | Room } |"
                + str(x)
                + ": "
                + "servants'&#92;nquarters"
                + "| { Room | Room | Room | Room }"
            )
        dunMap.node(str(x), contents, shape=roomShape)
        for connection in dungeon[x]["connections"]:
            dunMap.edge(
                str(x),
                str(x + connection),
            )
    dunMap.render("Test Map.gv")
