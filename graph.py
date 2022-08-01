def graph(dungeon):
    for x in range(2,len(dungeon)):
        second = dungeon[x]["connections"]
        print(
            '[ ' + str(second)
            + ': ' + dungeon[second]['name']
            + ' ]' + ' --> ' + '[ '
            + str(x) + ': '
            + dungeon[x]['name'] + ' ]'
        )
        #print('[ ' + str(x) + ': ' + dungeon[x]['name']
        #+ ' --> ' + str(dungeon[x]['name']))


