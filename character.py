import pygame
import grid
import map

class character():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bew = 5

    def drawField(self, SCREEN, blockSize):
        rec = pygame.Rect((grid.gridCordinat(self.x, self.y)), (blockSize, blockSize))
        pygame.draw.rect(SCREEN, (200,200,200), rec)

    def move(self, direction, fields):
        movement = 0
        if direction == 1:
            for field in fields:
                if (self.x, self.y - 1) == (field.x, field.y):
                    movement = 1
                    if type(field) == map.door:
                        return field
            if movement != 1:
                self.y -= 1
        elif direction == 2:
            for field in fields:
                if (self.x, self.y + 1) == (field.x, field.y):
                    movement = 1
                    if type(field) == map.door:
                        return field
            if movement != 1:
                self.y += 1
        elif direction == 3:
            for field in fields:
                if (self.x - 1, self.y) == (field.x, field.y):
                    movement = 1
                    if type(field) == map.door:
                        return field
            if movement != 1:
                self.x -= 1
        elif direction == 4:
            for field in fields:
                if (self.x + 1, self.y) == (field.x, field.y):
                    movement = 1
                    if type(field) == map.door:
                        return field
            if movement != 1:
                self.x += 1