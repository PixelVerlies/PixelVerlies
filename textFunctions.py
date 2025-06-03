import pygame
import grid
class textField():
    def __init__(self, text, x, y, font, leng=0, high=0, rev=0):
        self.text = text.replace("ü", "u").replace("ö", "o").replace("ä", "a").replace("ß", "ss").replace("Ü", "U").replace("Ö", "O").replace("Ä", "A")
        self.x = x
        self.y = y
        self.font = font
        self.leng = leng
        self.high = high
        self.rev = rev
        if self.rev == 1:
            self.color = (255, 255, 255) 
        else:
            self.color = (0, 0, 0)  # Standardfarbe Schwarz


    def drawField(self, blockSize, SCREEN):
        text = self.font.render(self.text, False, self.color)  # Verwende die Farbe
        
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
        if self.rev == 1:
            text_surface.fill((0,0,0))
        else:
            text_surface.fill((255,255,255))
        text_surface.blit(text, ((count_x - text_x) / 2, (count_y - text_y) / 2))
        SCREEN.blit(text_surface, (grid.gridCordinat(self.x, self.y, blockSize)))
        
class textweiß():
    def __init__(self, text, x, y, font, leng=0, high=0):
        self.text = text.replace("ü", "u").replace("ö", "o").replace("ä", "a").replace("ß", "ss").replace("Ü", "U").replace("Ö", "O").replace("Ä", "A")
        self.x = x
        self.y = y
        self.font = font
        self.leng = leng
        self.high = high
        self.color = (255, 255, 255)  # farbe weiß

    def drawField(self, blockSize, SCREEN):
        text = self.font.render(self.text, False, self.color)  # Verwende die Farbe
        
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
        text_surface.fill((0,0,0))#schwarz hintergrund
        text_surface.blit(text, ((count_x - text_x) / 2, (count_y - text_y) / 2))
        SCREEN.blit(text_surface, (grid.gridCordinat(self.x, self.y, blockSize)))


        


class textInput():
    def __init__(self, x, y, font, leng, high):
        self.text = ""
        self.real_text = ""  # Speichert den echten Text für Passwortfelder
        self.x = x
        self.y = y
        self.font = font
        self.leng = leng
        self.high = high
        self.active = False
        self.rec = None
        self.is_password = False
        self.show_password = False
        self.offset = 0
    
    def drawField(self, blockSize, SCREEN):
        if self.is_password:
            display_text = self.real_text if self.show_password else "*" * len(self.real_text)
        else:
            display_text = self.text
        
        display_text = display_text.replace("ü", "u").replace("ö", "o").replace("ä", "a").replace("ß", "ss").replace("Ü", "U").replace("Ö", "O").replace("Ä", "A")
        text = self.font.render(display_text, False, (0,0,0))
        text_width, text_height = text.get_size()
        
        field_width = self.leng * blockSize
        field_height = self.high * blockSize
        self.rec = pygame.Rect((grid.gridCordinat(self.x, self.y, blockSize)), (field_width, field_height))
        
        if text_width > field_width - 4 and self.active:
            self.offset = text_width - (field_width - 4)
        else:
            self.offset = 0
        
        text_surface = pygame.Surface((field_width, field_height))
        text_surface.fill((255,255,255))
        text_surface.blit(text, (2 - self.offset, (field_height - text_height) / 2))
        SCREEN.blit(text_surface, (grid.gridCordinat(self.x, self.y, blockSize)))

class toggleButton():
    def __init__(self, text, x, y, font, leng, high):
        self.text = text.replace("ü", "u").replace("ö", "o").replace("ä", "a").replace("ß", "ss").replace("Ü", "U").replace("Ö", "O").replace("Ä", "A")
        self.x = x
        self.y = y
        self.font = font
        self.leng = leng
        self.high = high
        self.rec = None
    
    def drawField(self, blockSize, SCREEN):
        text = self.font.render(self.text, False, (0,0,0))
        
        width_px = self.leng * blockSize
        height_px = self.high * blockSize
        self.rec = pygame.Rect((grid.gridCordinat(self.x, self.y, blockSize)), (width_px, height_px))
        
        text_surface = pygame.Surface((width_px, height_px))
        text_surface.fill((200,200,200))
        text_surface.blit(text, ((width_px - text.get_width()) / 2, (height_px - text.get_height()) / 2))
        SCREEN.blit(text_surface, (grid.gridCordinat(self.x, self.y, blockSize)))