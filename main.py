import pygame
import grid
import textFunctions
import login_screen
import registration_screen
import menu_screen
import sys


pygame.init()
clock = pygame.time.Clock()

WIDTH = 1000
HEIGHT = 600

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.font.init()
ueberschrift = pygame.font.Font("Arcade-Classic-Font/bytebounce.medium.TTF", 45)
textKoerper = pygame.font.Font("Arcade-Classic-Font/bytebounce.medium.TTF", 25)

blockSize = 25
fild_leng = WIDTH / blockSize
fild_high = HEIGHT / blockSize

# 1 = Login, 2 = Registration, 3 = Main Menu
site = 1

run = True

# In der Hauptschleife:
login_data = login_screen.create_login_fields(ueberschrift, textKoerper)
registration_data = registration_screen.create_registration_fields(ueberschrift, textKoerper)
menu_data = menu_screen.create_menu_fields(ueberschrift, textKoerper)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
        
        if site == 1:  # Login screen
            site = login_screen.handle_login_events(event, login_data, site)
        elif site == 2:  # Registration screen
            site = registration_screen.handle_registration_events(event, registration_data, site)
        elif site == 3:  # Main menu
            site = menu_screen.handle_menu_events(event, menu_data, site)
    
    SCREEN.fill(BLACK)
    grid.drawGrid(WIDTH, HEIGHT, blockSize, SCREEN) 

    if site == 1:
        for field in login_data["fields"]:
            field.drawField(blockSize, SCREEN)
    elif site == 2:
        for field in registration_data["fields"]:
            field.drawField(blockSize, SCREEN)
    elif site == 3:
        for field in menu_data["fields"]:
            field.drawField(blockSize, SCREEN)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()