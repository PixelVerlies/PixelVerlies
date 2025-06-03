from character import character
from rounds import rounds
import map
from enemie import enemie
from field import field
import grid
import dungeons



def loadAllImg(charac, all_rooms, door_list, blockSize):

    characterImg = grid.importImage("Images/Character/warrior.png", blockSize)
    charac.loadImg(characterImg)

    doorImg = grid.importImage("Images/Dungeon/door.png", blockSize)
    for i in door_list:
        i.loadImg(doorImg)

    fieldImg = grid.importImage("Images/Dungeon/wall.png", blockSize)
    for i in all_rooms:
        for j in i.roomFields:
            if type(j) == enemie:
                j.loadImg(blockSize)
            elif type(j) == field:
                j.loadImg(fieldImg)

    healingImg = grid.importImage("Images/Dungeon/wall.png", blockSize * 2)

    for i in range(len(charac.items)):
        charac.items[i].loadImg(healingImg)


    return charac, all_rooms, door_list

def create(data, blockSize, fild_leng, fild_high, level):
    all_rooms, door_list = dungeons.dungeonOne()
    roomAkt = 0

    countEnemie = 0

    charac = character()
    charac.setItems(data)

    for i in all_rooms:
        i.startPos(len(i.roomMap[0]), len(i.roomMap), fild_leng, fild_high)
        i.creatRoomFields(door_list, data, level, charac)
        countEnemie += i.countEnemie

    charac, all_rooms, door_list = loadAllImg(charac, all_rooms, door_list, blockSize)

    rod = rounds(all_rooms[roomAkt].roomFields, fild_leng, fild_high, all_rooms[roomAkt].maxIni, countEnemie, level)

    rod.field_list = all_rooms[roomAkt].roomFields
    rod.maxIni = all_rooms[roomAkt].maxIni

    return rod, charac, door_list, all_rooms