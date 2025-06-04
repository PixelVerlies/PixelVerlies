import enemie
from field import field
import itembar

class door(field):
    def __init__(self, doorNr, roomId, nextDoor, nextRoom, site):
        #Erzeugt die nötigen Variabeln
        self.doorId = doorNr
        self.roomId = roomId
        self.nextDoor = nextDoor
        self.nextRoom = nextRoom
        self.site = site
        self.img = None
        self.x = 0
        self.y = 0

    def doorCordinat(self, x, y):
        #Setzt die Kordinaten
        self.x = x
        self.y = y

    def startDoor(self, character):
        #Setzt die Kordinaten des Charakters beim durqueren der Tür
        match character.direction:
            case 1:
                character.x = self.x
                character.y = self.y - 1
            case 2:
                character.x = self.x
                character.y = self.y + 1
            case 3:
                character.x = self.x - 1
                character.y = self.y
            case 4:
                character.x = self.x + 1
                character.y = self.y


class room():
    def __init__(self, roomId, map):
        #Erzeugt die nötigen Variabeln
        self.roomMap = map
        self.roomFields = []
        self.roomId = roomId
        self.countEnemie = 0
        self.maxIni = 1
        self.startX = 0
        self.startY = 0

    def startPos(self, length, heigh, fild_leng, fild_high):
        #Setzt die Startkordinaten
        self.startX = int(fild_leng / 2 - length / 2)
        self.startY = int(fild_high / 2 - heigh / 2)

    def creatRoomFields(self, allDoors, data, level, charac):
        #Geht das Feld systematisch durch
        for i in range(len(self.roomMap)):
            for j in range(len(self.roomMap[i])):
                if type(self.roomMap[i][j]) == list:
                    #Erzeugt die Tür im Spielfeld
                    if self.roomMap[i][j][0] == 2:
                        for doors in allDoors:
                            if doors.doorId == self.roomMap[i][j][1]:
                                self.roomFields.append(doors)
                                doors.doorCordinat(self.startX + j, self.startY + i)
                    #Erzeugt die Gegner
                    if self.roomMap[i][j][0] == 4:
                        self.countEnemie += 1
                        self.maxIni += 1
                        self.roomFields.append(enemie.enemie(self.startX + j, self.startY + i, self.maxIni, self.roomId, j, i, self.roomMap[i][j][1], data, level))
                else:
                    #Erzeugt die Mauern
                    if self.roomMap[i][j] == 1:
                        self.roomFields.append(field(self.startX + j, self.startY + i))
                    #Setzt die Kordinaten des Charakters
                    if self.roomMap[i][j] == 3:
                        charac.setCordinats(self.startX + j, self.startY + i)


def drawGamefild(rod, charac, SCREEN, blockSize, textKoerper):
    #Zeichnet die Felder
    for i in rod.field_list:
        #Zeichnen der Gegner Lebensbalken
        if type(i) == enemie.enemie:
            i.drawHealthbar(SCREEN, blockSize)
        i.drawField(SCREEN, blockSize)

    #Itembar zeichnen
    bar = itembar.itembar(3)
    bar.drawItemBar(rod, charac, SCREEN, blockSize, textKoerper)


    rod.field_list[0].drawField(SCREEN, blockSize)

    #Zeichnet den Charakter
    charac.drawField(SCREEN, blockSize)
    charac.drawHealthbar(SCREEN, blockSize, textKoerper)
