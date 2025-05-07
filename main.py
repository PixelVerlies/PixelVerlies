import pygame
import grid
import textFunctions
import sys

pygame.init()
clock = pygame.time.Clock()

WIDTH = 1000
HEIGHT = 600

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.font.init()
ueberschrift = pygame.font.Font("Arcade-Classic-Font/ARCADECLASSIC.TTF", 35)
textKoerper = pygame.font.Font("Arcade-Classic-Font/ARCADECLASSIC.TTF", 20)

blockSize = 25
fild_leng = WIDTH / blockSize
fild_high = HEIGHT / blockSize

site = 1

run = True


texfield_list = []

if site == 1:
    texfield_list.append(textFunctions.textField("Anmeldung", 16, 3, ueberschrift, 8))
    texfield_list.append(textFunctions.textField("Name",15, 7, textKoerper, 4))
    texfield_list.append(textFunctions.textInput(21, 7, textKoerper, 6, 1))
    texfield_list.append(textFunctions.textField("Passwort",15, 9, textKoerper, 4))
    texfield_list.append(textFunctions.textInput(21, 9, textKoerper, 6, 1))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            posx, posy = pygame.mouse.get_pos()

            for i in texfield_list:
                if type(i) is textFunctions.textInput:
                    if i.rec.collidepoint(posx, posy):
                        i.active = True
                    else:
                        i.active = False

        if event.type == pygame.KEYDOWN: 
            for i in texfield_list:
                if type(i) is textFunctions.textInput:
                    if i.active:
                        if event.key == pygame.K_BACKSPACE: 
                            i.text = i.text[:-1] 
                        else: 
                            i.text += event.unicode

            
    
    SCREEN.fill(BLACK)

    grid.drawGrid(WIDTH, HEIGHT, blockSize, SCREEN) 

    for i in texfield_list:
        i.drawField(blockSize, SCREEN)

    pygame.display.flip()
    clock.tick(60)