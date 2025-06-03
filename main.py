import pygame
import grid
import sys
from database import database
import dungeonEnd
import map
import createDungeon


data = database()
data.connection()

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
fild_leng = int(WIDTH / blockSize)
fild_high = int(HEIGHT / blockSize)

site = 1

run = True
wall = grid.importImage("Images/Dungeon/wall.png", blockSize)

rod, charac, door_list, all_rooms = createDungeon.create(data, blockSize, fild_leng, fild_high, 1)

counter = 90


while run:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT: 
            run = False

    SCREEN.fill(BLACK)
    grid.drawGrid(WIDTH, HEIGHT, blockSize, SCREEN, wall)

    if rod.end == 0:
        rod.roundRun(events, charac, door_list, all_rooms)
        map.drawGamefild(rod, charac, SCREEN, blockSize, textKoerper)
    else:
        counter, run = dungeonEnd.dungeonEnd(rod, fild_leng, fild_high, SCREEN, blockSize, ueberschrift, counter, data, charac)

    pygame.display.flip()
    clock.tick(60)

data.connClose()
pygame.quit()
sys.exit()