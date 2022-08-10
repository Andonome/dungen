# This function uses graphviz to output the map to a pdf file.
import graphviz


def graph(setting,dungeon):
    dunMap = graphviz.Digraph(
        engine="dot",
        comment="Test Map",
    )
    dunMap.attr(
    "node",
    shape="ellipse",
    overlap="scale",
    rotate="90",
    splines="polyline",
    penwidth="10",
    )
        
    dunMap.attr(
    "edge",
    penwidth="10",
    overlap='false',
    arrowhead="none",
    )
    dunMap.node(setting,shape='tripleoctagon',fontsize="80")
    for x in range(len(dungeon)):
        roomShape = 'ellipse'
        contents = str(x) + r": \n" + r"\n ".join(dungeon[x]["features"])
        if len(dungeon[x]["creatures"]) > 0:
            contents += r"\n" + r"\n".join(dungeon[x]["creatures"])
        if len(dungeon[x]["type"]) > 0:
            contents += "(" + ", ".join(dungeon[x]["type"]) + ")"
        if "mana lake" in dungeon[x]["features"]:
            roomShape = "Mdiamond"
        elif "entrance" in dungeon[x]["type"]:
            roomShape = "doublecircle"
        elif "split" in dungeon[x]["type"]:
            roomShape = "hexagon"
        elif "dead end" in dungeon[x]["type"]:
            roomShape = "invhouse"
        dunMap.node(
        str(x),
        contents
        )
        for connection in dungeon[x]["connections"]:
            dunMap.edge(str(x), str(connection),)
    dunMap.render("Test Map.gv")
