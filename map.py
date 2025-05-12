import pygame
import grid

class field():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def drawField(self, SCREEN, blockSize):
        rec = pygame.Rect((grid.gridCordinat(self.x, self.y)), (blockSize, blockSize))
        SCREEN.blit(self.img, rec)

class door(field):
    def __init__(self, doorNr, roomId, nextDoor, nextRoom, site, img):
        self.doorId = doorNr
        self.roomId = roomId
        self.nextDoor = nextDoor
        self.nextRoom = nextRoom
        self.site = site
        self.img = img
        self.x = 0
        self.y = 0

    def doorCordinat(self, x, y):
        self.x = x
        self.y = y

class room():
    def __init__(self, roomId, fields):
        self.roomFields = fields
        self.roomId = roomId

    def creatRoomFields(self, allDoors, startX, startY, character=None, movement=0, nextDoor=None):
        fields = []
        for i in range(len(self.roomFields)):
            for j in range(len(self.roomFields[i])):
                if self.roomFields[i][j] == 1:
                    fields.append(field(startX + j, startY + i))
                if self.roomFields[i][j] == 2:
                    for doors in allDoors:
                        if doors.roomId == self.roomId:
                            if i == 0 and doors.site == 1:
                                fields.append(doors)
                                doors.doorCordinat(startX + j, startY + i)
                            elif i == len(self.roomFields) - 1 and doors.site == 2:
                                fields.append(doors)
                                doors.doorCordinat(startX + j, startY + i)
                            elif j == 0 and doors.site == 3:
                                fields.append(doors)
                                doors.doorCordinat(startX + j, startY + i)
                            elif j == len(self.roomFields[i]) - 1 and doors.site == 4:
                                fields.append(doors)
                                doors.doorCordinat(startX + j, startY + i)

                        if character:
                            if doors.doorId == nextDoor:
                                match movement:
                                    case 1:
                                        character.x = doors.x
                                        character.y = doors.y - 1
                                    case 2:
                                        character.x = doors.x
                                        character.y = doors.y + 1
                                    case 3:
                                        character.x = doors.x - 1
                                        character.y = doors.y
                                    case 4:
                                        character.x = doors.x + 1
                                        character.y = doors.y

        return fields