def showDungeon(roomList,map):
    output=''
    # the roomList is a series of room connections, like '[2,5]', meeaniang 'room 3 joins with room 5'.
    # This takes that, and turns it into '[ 2: Alcove ]', then into '[ 2: alcove ] -- > [ 5: river ]'.
    # Graph-easy then deals with the output.
    for pair in roomList:
        output += '[ ' + str(pair[0]) + ': ' + map[pair[0]] + ' ]' 
        output += ' --> [ ' + str(pair[1]) + ': ' + map[pair[1]] + ' ]' + '\n'
    print(output)

