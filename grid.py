import pygame

def drawGrid(WIDTH, HEIGHT, blockSize, SCREEN):
    for i in range(0, WIDTH, blockSize):
        for j in range(0, HEIGHT, blockSize):
            rec = pygame.Rect(i, j, blockSize, blockSize)
            if i == 0 or i == WIDTH - blockSize or j == 0 or j == HEIGHT - blockSize:
                pygame.draw.rect(SCREEN, (255,255,255), rec)

def gridCordinat(x, y, blockSize):
    fild_x = x * blockSize
    fild_y = y * blockSize
    return fild_x, fild_y

def countField(i, blockSize):
    count = int(i / blockSize) + (i % blockSize > 0)
    return count

def importImage(path, blockSize):
    img = pygame.image.load(path)
    return pygame.transform.scale(img, (blockSize, blockSize))