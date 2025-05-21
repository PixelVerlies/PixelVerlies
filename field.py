import grid
import pygame

class field():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = None

    def loadImg(self, blockSize, path):
        self.img = grid.importImage(path, blockSize)

    def drawField(self, SCREEN, blockSize):
        rec = pygame.Rect((grid.gridCordinat(self.x, self.y, blockSize)), (blockSize, blockSize))
        SCREEN.blit(self.img, rec)