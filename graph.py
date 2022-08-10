# This function uses graphviz to output the map to a pdf file.
import graphviz


def graph(setting,dungeon):
    dunMap = graphviz.Digraph(
        engine="dot",
        comment="Test Map",
    )
    dunMap.attr("node",
    shape='egg',
    penwidth="10",
    overlap='false',
    ranksep="1 equally",)
        
    dunMap.node('areaType',setting,shape='tripleoctagon',fontsize='60')
    for x in range(len(dungeon)):
        fontsize = 10
        roomShape = 'ellipse'
        contents = str(x) + ": \n" + "\n ".join(dungeon[x]["features"])
        if len(dungeon[x]["creatures"]) > 0:
            contents += "\n" + "\n".join(dungeon[x]["creatures"])
        if len(dungeon[x]["type"]) > 0:
            contents += "(" + ", ".join(dungeon[x]["type"]) + ")"
        if "mana lake" in dungeon[x]["features"]:
            roomShape = "Mdiamond"
        elif "entrance" in dungeon[x]["type"]:
            roomShape = "doublecircle"
            fontsize = 15
        elif "split" in dungeon[x]["type"]:
            roomShape = "hexagon"
            fontsize = 15
        elif "dead end" in dungeon[x]["type"]:
            roomShape = "invhouse"
        dunMap.node(
        str(x),
        contents,shape=roomShape,
        fontsize=str(fontsize),
        )
        for connection in dungeon[x]["connections"]:
            dunMap.edge(str(x), str(connection),weight="1.1",arrowhead="none",penwidth="10.5",maxlen="0.1")
    dunMap.render("Test Map.gv")
