import pygame
import grid
import map
import random
import enemie
import textFunctions
from field import field
import healingpotion
import sql

class character(field):
    def __init__(self, data, id):
        #Erzeugt die benötigten Variabeln
        self.x = 0
        self.y = 0
        self.id = id
        self.img = None
        self.ini = 1
        self.attacked = 1
        self.direction = None
        self.healed = 1
        self.items = []
        self.aktItem = None

        #Läd alle benötigten Werte aus der Datenbank
        db = sql.loadCharacter(data, self.id)

        #Speichert die geladenen Werte
        self.classId = db[0][3]
        self.maxBew = db[0][0]
        self.aktBew = self.maxBew
        self.level = db[0][1]
        self.dmg = db[1][1]
        self.maxHealth = db[0][2]
        self.health = self.maxHealth
        self.shield = db[2][1]

    def loadImg(self, blockSize):
        #Passender Pfad für das Bild wird gesetzt
        path = ""
        match self.classId:
            case 1:
                path = "Images/Character/warrior.png"
            case 2:
                path = "Images/Character/ranger.png"
            
        #Bild für den Heiltrank wird geladen
        self.img = grid.importImage(path, blockSize)

    def setItems(self, data):
        #Läd alle Heiltränke aus der Datenbank
        res = sql.loadHealingPotion(data, self)

        #Alle Heiltränke werden gespeichert
        for i in res:
            self.items.append(healingpotion.healingPotion(i))

    def setCordinats(self, x, y):
        #Kordinaten werden gesetzt
        self.x = x
        self.y = y

    def useItems(self):
        #Sorgt für 1 -> 0 ausgleich für die Liste
        self.aktItem -= 1

        #Heitrank nur nutzbar wenn vorhanden und Schaden existiert
        if self.items[self.aktItem].count > 0 and self.health < self.maxHealth and self.healed == 1:
            #Erhöht das Leben
            res = self.health + self.items[self.aktItem].healing

            #Sorgt dafür dass nicht mehr Leben als max
            if res < self.maxHealth:
                self.health = res
            else:
                self.health = self.maxHealth

            #Verbrauch des Heiltrankes
            self.items[self.aktItem].count -= 1 

            #Verbraucht eine Bewegung
            self.aktBew -= 1 

            #Sorgt dafür dass nur ein mal pro Runde
            self.healed = 0
        self.aktItem = None  

    def move(self, rod):
        movement = 0

        #Anzahl Bewegungen verringern
        self.aktBew -= 1

        #Entscheidung der Richtung
        match self.direction:
            case 1:
                for field in rod.field_list:
                    #Prüfung ob die Bewegung Möglich ist
                    if (self.x, self.y - 1) == (field.x, field.y):
                        movement = 1

                        #Tür oder Gegner
                        doorAkt = self.moveAttack(field, rod)

                        #Prüfung ob eine Tür durchquert wird
                        if doorAkt == 1:
                            return field
                        
                #Bewegung ausführen
                if movement != 1:
                    self.y -= 1
            case 2:
                for field in rod.field_list:
                    if (self.x, self.y + 1) == (field.x, field.y):
                        
                        
                        movement = 1

                        #Tür oder Gegner
                        doorAkt = self.moveAttack(field, rod)

                        #Prüfung ob eine Tür durchquert wird
                        if doorAkt == 1:
                            return field
                        
                #Bewegung ausführen
                if movement != 1:
                    self.y += 1
            case 3:
                for field in rod.field_list:
                    if (self.x - 1, self.y) == (field.x, field.y):
                        movement = 1

                        #Tür oder Gegner
                        doorAkt = self.moveAttack(field, rod)

                        #Prüfung ob eine Tür durchquert wird
                        if doorAkt == 1:
                            return field
                        
                #Bewegung ausführen
                if movement != 1:
                    self.x -= 1
            case 4:
                for field in rod.field_list:
                    if (self.x + 1, self.y) == (field.x, field.y):
                        movement = 1

                        #Tür oder Gegner
                        doorAkt = self.moveAttack(field, rod)

                        #Prüfung ob eine Tür durchquert wird
                        if doorAkt == 1:
                            return field
                        
                #Bewegung ausführen
                if movement != 1:
                    self.x += 1
            

    def moveAttack(self, field, rod):
        doorAkt = 0

        #Ist nächstes Feld eine Tür
        if type(field) == map.door:
            doorAkt = 1
        
        #Ist nächstes Feld ein Gegner dann angeifen
        if type(field) == enemie.enemie and self.attacked == 1:
            self.attack(field, rod.field_list, rod)
        
        return doorAkt


    def drawHealthbar(self, SCREEN, blockSize, textKoerper):
        #Erzeugt den Hintergund der Lebensanzeige
        rec = pygame.Rect((grid.gridCordinat(2, 2, blockSize)), (blockSize  * 8, blockSize))
        pygame.draw.rect(SCREEN, (255,255,255), rec)

        #Ereugt das Leben in der Lebensanzeige
        recHealth = pygame.Rect((grid.gridCordinat(2, 2, blockSize)), (blockSize  * 8 - 8, blockSize - 8))
        recHealth.x = rec.x + 4
        recHealth.y = rec.y + 4
        recHealth.width = recHealth.width / self.maxHealth * self.health
        pygame.draw.rect(SCREEN, (0,0,0,), recHealth)
        bew = textFunctions.textField(f"{self.aktBew}", 11, 2, textKoerper)
        bew.drawField(blockSize, SCREEN)


    def attack(self, enem, fields, rod):
        #Generiert Schaden am Gegner
        enem.health -= (random.randint(1, self.dmg) + self.level)

        #Wenn Gegner Tod
        if enem.health <= 0:
            #Gegneranzahl minus eins
            rod.countEnemie -= 1

            #Gegner wird nicht mehr gezeichnet
            for i in fields:
                if type(i) == enemie.enemie:
                    if i.ini > enem.ini:
                        i.ini -= 1
            fields.remove(enem)
            
        #Wenn alle Gegner tod für den Gewinn
        if rod.countEnemie <= 0:
            rod.end = 1

        #Sorgt für nur einen Angriff pro Runde
        self.attacked = 0