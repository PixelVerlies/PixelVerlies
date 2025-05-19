import pygame
import grid
import map
import random
import enemie
import textFunctions

class character(map.field):
    def __init__(self, x, y, img, ini):
        self.x = x
        self.y = y
        self.maxBew = 5
        self.aktBew = 5
        self.img = img
        self.ini = ini
        self.attacked = 1
        self.direction = 0
        self.enabel = 1
        self.dmg = 6
        self.health = 10
        self.maxHealth = 10
        self.shield = 2

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
        enem.health -= random.randint(1, self.dmg)
        if enem.health <= 0:
            rod.countEnemie -= 1
            for i in fields:
                if type(i) == enemie.enemie:
                    if i.ini > enem.ini:
                        i.ini -= 1
            fields.remove(enem)
            
        if rod.countEnemie <= 0:
            rod.end = 1