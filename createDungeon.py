from character import character
from rounds import rounds
from enemie import enemie
from field import field
import grid
import dungeons

def loadAllImg(data, charac, all_rooms, door_list, blockSize):
    #Speicherung des Bildes für den Charakter
    charac.loadImg(blockSize)

    #Bild für die Tür wird geladen
    doorImg = grid.importImage("Images/Dungeon/door.png", blockSize)
    for i in door_list:
        i.loadImg(doorImg)

    #Bild für die Mauern wird geladen
    fieldImg = grid.importImage("Images/Dungeon/wall.png", blockSize)

    #Unterschied zwischen Mauern und Gegnern
    for i in all_rooms:
        for j in i.roomFields:
            if type(j) == enemie:
                j.loadImg(blockSize)
            elif type(j) == field:
                j.loadImg(fieldImg)

    #Bilder für die Heiltränke wird gespeichert
    for i in range(len(charac.items)):
        charac.items[i].loadImg(blockSize)

    return charac, all_rooms, door_list

def create(data, blockSize, fild_leng, fild_high, level, id):
    #Dungeon wird genereiert
    all_rooms, door_list = dungeons.dungeonOne()

    #Startraum wird gesetzt
    roomAkt = 0

    #Speicherung der Anzahl der Gegner
    countEnemie = 0

    #Charakter wird dem Dungeon hinzugefügt
    charac = character(data, id)
    charac.setItems(data)

    #Alle einzelnen Räume werden generriert
    for i in all_rooms:
        i.startPos(len(i.roomMap[0]), len(i.roomMap), fild_leng, fild_high)
        i.creatRoomFields(door_list, data, level, charac)
        countEnemie += i.countEnemie

    #Alle Bilder werden geladen und gespeichert
    charac, all_rooms, door_list = loadAllImg(data, charac, all_rooms, door_list, blockSize)

    #Der aktuelle Durchlauf wird generiert
    rod = rounds(all_rooms[roomAkt].roomFields, fild_leng, fild_high, all_rooms[roomAkt].maxIni, countEnemie, level)

    #Der Erste Raum wird in den aktuellen Durchlauf gespeichert
    rod.field_list = all_rooms[roomAkt].roomFields
    rod.maxIni = all_rooms[roomAkt].maxIni

    return rod, charac, door_list, all_rooms