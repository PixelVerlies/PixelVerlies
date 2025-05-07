import pygame
import grid

class textField():
    def __init__(self, text, x, y, font, leng=0, high=0):
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.leng = leng
        self.high = high

    def drawField(self, blockSize, SCREEN):
        text = self.font.render(self.text, False, (0,0,0))
        text_x, text_y = text.get_size()

        if self.leng == 0:
            count_x = grid.countField(text_x, blockSize)
        else:
            count_x = self.leng

        if self.high == 0:
            count_y = grid.countField(text_y, blockSize)
        else:
            count_y = self.high
        
        count_x *= blockSize
        count_y *= blockSize
        text_surface = pygame.Surface((count_x, count_y))
        text_surface.fill((255,255,255))
        text_surface.blit(text, ((count_x - text_x) / 2, (count_y - text_y) / 2))
        SCREEN.blit(text_surface, (grid.gridCordinat(self.x, self.y, blockSize)))

class textInput():
    def __init__(self, x, y, font, leng, high):
        self.text = ""
        self.x = x
        self.y = y
        self.font = font
        self.leng = leng
        self.high = high
        self.active = None
        self.rec = None
    
    def drawField(self, blockSize, SCREEN):
        text = self.font.render(self.text, False, (0,0,0))

        count_x = self.leng * blockSize
        count_y = self.high * blockSize
        self.rec = pygame.Rect((grid.gridCordinat(self.x, self.y, blockSize)), (count_x, count_y))

        text_surface = pygame.Surface((count_x, count_y))
        text_surface.fill((255,255,255))
        text_surface.blit(text, (2, 0))
        SCREEN.blit(text_surface, (grid.gridCordinat(self.x, self.y, blockSize)))