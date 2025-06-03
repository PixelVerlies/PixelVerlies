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
        self.x = 0
        self.y = 0
        self.id = id

        db = sql.loadCharacter(data, self.id)

        self.maxBew = db[0][0]
        self.aktBew = self.maxBew
        self.img = None
        self.ini = 1
        self.level = db[0][1]
        self.attacked = 1
        self.direction = None
        self.dmg = db[1][1]
        self.maxHealth = db[0][2]
        self.health = self.maxHealth
        self.healed = 1
        self.shield = db[2][1]
        self.items = []
        self.aktItem = None

    def setItems(self, data):
        res = sql.loadHealingPotion(data, self)
        for i in res:
            self.items.append(healingpotion.healingPotion(i))
        #self.items.append(healingpotion.healingPotion(1))

    def setCordinats(self, x, y):
        self.x = x
        self.y = y

    def useItems(self):
        self.aktItem -= 1
        if self.items[self.aktItem].count > 0 and self.health < self.maxHealth and self.healed == 1:
            res = self.health + self.items[self.aktItem].healing
            if res < self.maxHealth:
                self.health = res
            else:
                self.health = self.maxHealth
            self.items[self.aktItem].count -= 1 
            self.aktBew -= 1 
            self.healed = 0
        self.aktItem = None  

    def move(self, rod):
        movement = 0
        self.aktBew -= 1
        match self.direction:
            case 1:
                for field in rod.field_list:
                    if (self.x, self.y - 1) == (field.x, field.y):
                        movement, doorAkt = self.moveAttack(field, rod)
                        if doorAkt == 1:
                            return field
                if movement != 1:
                    self.y -= 1
            case 2:
                for field in rod.field_list:
                    if (self.x, self.y + 1) == (field.x, field.y):
                        movement, doorAkt = self.moveAttack(field, rod)
                        if doorAkt == 1:
                            return field
                if movement != 1:
                    self.y += 1
            case 3:
                for field in rod.field_list:
                    if (self.x - 1, self.y) == (field.x, field.y):
                        movement, doorAkt = self.moveAttack(field, rod)
                        if doorAkt == 1:
                            return field
                if movement != 1:
                    self.x -= 1
            case 4:
                for field in rod.field_list:
                    if (self.x + 1, self.y) == (field.x, field.y):
                        movement, doorAkt = self.moveAttack(field, rod)
                        if doorAkt == 1:
                            return field
                if movement != 1:
                    self.x += 1
            

    def moveAttack(self, field, rod):
        movement = 1
        doorAkt = 0
        if type(field) == map.door:
            doorAkt = 1
        if type(field) == enemie.enemie and self.attacked == 1:
            self.attack(field, rod.field_list, rod)
        return movement, doorAkt


    def drawHealthbar(self, SCREEN, blockSize, textKoerper):
        rec = pygame.Rect((grid.gridCordinat(2, 2, blockSize)), (blockSize  * 8, blockSize))
        pygame.draw.rect(SCREEN, (255,255,255), rec)

        recHealth = pygame.Rect((grid.gridCordinat(2, 2, blockSize)), (blockSize  * 8 - 8, blockSize - 8))
        recHealth.x = rec.x + 4
        recHealth.y = rec.y + 4
        recHealth.width = recHealth.width / self.maxHealth * self.health
        pygame.draw.rect(SCREEN, (0,0,0,), recHealth)

        bew = textFunctions.textField(f"{self.aktBew}", 11, 2, textKoerper)
        bew.drawField(blockSize, SCREEN)


    def attack(self, enem, fields, rod):
        self.attacked = 0
        enem.health -= (random.randint(1, self.dmg) + self.level)
        if enem.health <= 0:
            rod.countEnemie -= 1
            for i in fields:
                if type(i) == enemie.enemie:
                    if i.ini > enem.ini:
                        i.ini -= 1
            fields.remove(enem)
            
        if rod.countEnemie <= 0:
            rod.end = 1