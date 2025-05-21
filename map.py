import pygame
import grid
import enemie
from field import field

class door(field):
    def __init__(self, doorNr, roomId, nextDoor, nextRoom, site):
        self.doorId = doorNr
        self.roomId = roomId
        self.nextDoor = nextDoor
        self.nextRoom = nextRoom
        self.site = site
        self.img = None
        self.x = 0
        self.y = 0

    def doorCordinat(self, x, y):
        self.x = x
        self.y = y

    def startDoor(self, character):
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
        self.roomMap = map
        self.roomFields = []
        self.roomId = roomId
        self.countEnemie = 0
        self.maxIni = 1
        self.startX = 0
        self.startY = 0

    def startPos(self, length, heigh, fild_leng, fild_high):
        self.startX = int(fild_leng / 2 - length / 2)
        self.startY = int(fild_high / 2 - heigh / 2)

    def creatRoomFields(self, allDoors, data):
        for i in range(len(self.roomMap)):
            for j in range(len(self.roomMap[i])):
                if type(self.roomMap[i][j]) == list:
                    if self.roomMap[i][j][0] == 4:
                        self.countEnemie += 1
                        self.maxIni += 1
                        self.roomFields.append(enemie.enemie(self.startX + j, self.startY + i, self.maxIni, self.roomId, j, i, self.roomMap[i][j][1], data))
                else:
                    if self.roomMap[i][j] == 1:
                        self.roomFields.append(field(self.startX + j, self.startY + i))
                    if self.roomMap[i][j] == 2:
                        for doors in allDoors:
                            if doors.roomId == self.roomId:
                                if i == 0 and doors.site == 1:
                                    self.roomFields.append(doors)
                                    doors.doorCordinat(self.startX + j, self.startY + i)
                                elif i == len(self.roomMap) - 1 and doors.site == 2:
                                    self.roomFields.append(doors)
                                    doors.doorCordinat(self.startX + j, self.startY + i)
                                elif j == 0 and doors.site == 3:
                                    self.roomFields.append(doors)
                                    doors.doorCordinat(self.startX + j, self.startY + i)
                                elif j == len(self.roomMap[i]) - 1 and doors.site == 4:
                                    self.roomFields.append(doors)
                                    doors.doorCordinat(self.startX + j, self.startY + i)
