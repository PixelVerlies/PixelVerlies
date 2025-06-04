import grid
import pygame

class field():
    def __init__(self, x, y):
        #Erzeugt die nötigen Variabeln
        self.x = x
        self.y = y
        self.img = None

    def loadImg(self, img):
        #Setzt das Bild
        self.img = img

    def drawField(self, SCREEN, blockSize):
        #Zeichnet das Feld
        rec = pygame.Rect((grid.gridCordinat(self.x, self.y, blockSize)), (blockSize, blockSize))
        SCREEN.blit(self.img, rec)