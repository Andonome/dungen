def showDungeon(roomList,map):
    output=''
    for pair in roomList:
        output += '[ ' + str(pair[0]) + ': ' + map[pair[0]] + ' ]' 
        output += ' --> [ ' + str(pair[1]) + ': ' + map[pair[1]] + ' ]' + '\n'
    print(output)

