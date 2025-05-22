from character import character
from rounds import rounds
import map
from enemie import enemie
from field import field
import grid

def creatList():
    all_rooms = []

    all_rooms.append(map.room(0, [
                [1,1,1,1,2,1,1,1],
                [1,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,2],
                [1,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1]]))

    all_rooms.append(map.room(1, [
                [1,1,1,1,1,1],
                [1,0,0,0,0,1],
                [1,0,0,0,0,1],
                [1,0,[4,1],0,0,1],
                [1,0,0,0,0,1],
                [1,0,0,0,0,1],
                [1,1,2,1,1,1]]))

    all_rooms.append(map.room(2, [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
                [2,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
                [1,0,0,0,0,1,1,1,0,1,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1],
                [1,0,0,0,1,1,0,1,0,1,0,0,0,0,0,1],
                [1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,1],
                [1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1],
                [1,0,0,[4,2],0,0,0,0,0,1,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1,0,[4,1],0,0,0,1],
                [1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]))

    door_list = []

    door_list.append(map.door(0,0,1,1,1))
    door_list.append(map.door(1,1,0,0,2))
    door_list.append(map.door(2,0,3,2,4))
    door_list.append(map.door(3,2,2,0,3))

    return all_rooms, door_list

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
    all_rooms, door_list = creatList()
    roomAkt = 0

    countEnemie = 0

    for i in all_rooms:
        i.startPos(len(i.roomMap[0]), len(i.roomMap), fild_leng, fild_high)
        i.creatRoomFields(door_list, data, level)
        countEnemie += i.countEnemie

    charac = character(18,11)
    charac.setItems(data)

    charac, all_rooms, door_list = loadAllImg(charac, all_rooms, door_list, blockSize)

    rod = rounds(all_rooms[roomAkt].roomFields, fild_leng, fild_high, all_rooms[roomAkt].maxIni, countEnemie, level)

    rod.field_list = all_rooms[roomAkt].roomFields
    rod.maxIni = all_rooms[roomAkt].maxIni

    return rod, charac, door_list, all_rooms