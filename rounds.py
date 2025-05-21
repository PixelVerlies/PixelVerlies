import pygame
from enemie import enemie

class rounds():
    def __init__(self, fields, fild_leng, fild_high, maxIni, countEnemie):
        self.field_list = fields
        self.fild_leng = fild_leng
        self.fild_high = fild_high
        self.wait = 0
        self.aktWait = 10
        self.maxWait = 10
        self.aktIni = 1
        self.maxIni = maxIni
        self.countEnemie = countEnemie
        self.end = 0
        self.roundNr = 0
        self.prue = 0
        self.prueIni = []

    def roundRun(self, events, charac, door_list, all_rooms):
        doorAkt = None

        if self.aktIni == 1:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if charac.aktBew > 0:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            charac.direction = 1
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            charac.direction = 2
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            charac.direction = 3
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            charac.direction = 4

                        doorAkt = charac.move(self)

                        for fiel in self.field_list:
                            if type(fiel) == enemie:
                                fiel.aktBew = fiel.maxBew

                        if self.maxIni > 1 and charac.aktBew == 0:
                            self.aktIni += 1
                    else:
                        charac.aktBew = charac.maxBew
                        charac.attacked = 1
        else:
            if self.wait == 1:
                self.aktWait -= 1
                if self.aktWait == 0:
                    self.wait = 0
                    self.aktWait = self.maxWait
            else:
                for fiel in self.field_list:
                    if type(fiel) == enemie:
                        if fiel.ini == self.aktIni:
                            self.prue +=1
                            fiel.move(self, charac)

                if self.aktIni == self.maxIni + 1:
                    self.prueIni.append(1)

                if self.prue == 0:
                    self.prueIni.append(1)

            if 1 in self.prueIni:
                charac.aktBew = charac.maxBew
                charac.attacked = 1
                self.aktIni = 1
                self.roundNr += 1
    
        self.prue = 0
        self.prueIni = []

        if doorAkt:
            self.maxIni = 1
            roomAkt = doorAkt.nextRoom
            door_list[doorAkt.nextDoor].startDoor(charac)
            self.field_list = all_rooms[roomAkt].roomFields
            self.maxIni = all_rooms[roomAkt].maxIni
            doorAkt = None
