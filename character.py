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

    def move(self, direction, wall):
        movement = 0
        if direction == 1:
            for i in wall:
                if (self.x, self.y - 1) == (i.x, i.y):
                    movement = 1
                    if type(i) == map.door:
                        return i
            if movement != 1:
                self.y -= 1
        elif direction == 2:
            for i in wall:
                if (self.x, self.y + 1) == (i.x, i.y):
                    movement = 1
                    if type(i) == map.door:
                        return i
            if movement != 1:
                self.y += 1
        elif direction == 3:
            for i in wall:
                if (self.x - 1, self.y) == (i.x, i.y):
                    movement = 1
                    if type(i) == map.door:
                        return i
            if movement != 1:
                self.x -= 1
        elif direction == 4:
            for i in wall:
                if (self.x + 1, self.y) == (i.x, i.y):
                    movement = 1
                    if type(i) == map.door:
                        return i
            if movement != 1:
                self.x += 1