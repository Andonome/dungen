import graphviz

def graph(dungeon):
    dunMap = graphviz.Digraph(comment='Test Map')
    for x in range(1,len(dungeon)):
        contents = str(x) + ": \n" + '\n '.join(dungeon[x]['features'])
        if len(dungeon[x]['creatures']) > 0:
            contents += '\n' + '\n'.join(dungeon[x]['creatures'])
        dunMap.node(str(x), contents)
        for connection in dungeon[x]["connections"]:
            dunMap.edge(str(x),str(connection))
    print(dunMap.source)
    dunMap.render('Test Map.gv')



