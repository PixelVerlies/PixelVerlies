import pygame
from enemie import enemie

class rounds():
    def __init__(self, fields, fild_leng, fild_high, maxIni, countEnemie, level):
        #Erzeugt alle nötigen Variabeln
        self.field_list = fields
        self.fild_leng = fild_leng
        self.fild_high = fild_high
        self.level = level
        self.wait = 0
        self.maxWait = 10
        self.aktWait = 10
        self.aktIni = 1
        self.maxIni = maxIni
        self.countEnemie = countEnemie
        self.end = 0
        self.roundNr = 0
        self.prue = 0
        self.prueIni = []
        self.loot = True

    def roundRun(self, events, charac, door_list, all_rooms):
        doorAkt = None

        #Auswahl wer dran ist
        if self.aktIni == 1:
            #Aktionen durch einen Tastendruck
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if charac.aktBew > 0:
                        #Hilfsvariabeln
                        charac.direction = None
                        charac.aktItem = None

                        #Item auswählen
                        if event.key == pygame.K_1:
                            if len(charac.items) >= 1:
                                charac.aktItem = 1
                        elif event.key == pygame.K_2:
                            if len(charac.items) >= 2:
                                charac.aktItem = 2
                        elif event.key == pygame.K_3:
                            if len(charac.items) >= 3:
                                charac.aktItem = 3
                        #Richtung auswählen
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:
                            charac.direction = 1
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            charac.direction = 2
                        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            charac.direction = 3
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            charac.direction = 4
                        
                        #Item nutzen
                        if charac.aktItem:
                            charac.useItems()
                        #Bewegen
                        elif charac.direction:
                            doorAkt = charac.move(self)                        

                        #Reset der Bewegung der Gegner
                        for fiel in self.field_list:
                            if type(fiel) == enemie:
                                fiel.aktBew = fiel.maxBew

                        #Erhöhunng der Initiative
                        if self.maxIni > 1 and charac.aktBew == 0:
                            self.aktIni += 1
                    else:
                        #Reset der Charakterwerte
                        charac.aktBew = charac.maxBew
                        self.roundNr += 1
                        charac.attacked = 1
                        charac.healed = 1
        else:
            #Wartezeit damit die Bewegung erkennbar ist
            if self.wait == 1:
                self.aktWait -= 1
                if self.aktWait == 0:
                    self.wait = 0
                    self.aktWait = self.maxWait
            else:
                for fiel in self.field_list:
                    if type(fiel) == enemie:
                        #Wenn Gegner dran bewegt er sich
                        if fiel.ini == self.aktIni:
                            self.prue +=1
                            fiel.move(self, charac)

                #Ist das Ende der Initiative erreicht
                if self.aktIni == self.maxIni + 1:
                    self.prueIni.append(1)

                #Ist kein Gegner in der aktuellen Initiative
                if self.prue == 0:
                    self.prueIni.append(1)

            #Reset der Charakterwerte
            if 1 in self.prueIni:
                charac.aktBew = charac.maxBew
                charac.attacked = 1
                charac.healed = 1
                self.aktIni = 1
                self.roundNr += 1
    
        #Reset der Prüfwerte
        self.prue = 0
        self.prueIni = []

        #Nächster Raum wird geladen beim durchqueren einer Tür
        if doorAkt:
            self.maxIni = 1
            roomAkt = doorAkt.nextRoom
            door_list[doorAkt.nextDoor].startDoor(charac)
            self.field_list = all_rooms[roomAkt].roomFields
            self.maxIni = all_rooms[roomAkt].maxIni
            doorAkt = None
