import pygame
import grid
import textFunctions

class itembar():
    def __init__(self, counter):
        self.counter = counter

    def drawItemBar(self, rod, charac, SCREEN, blockSize, textKoerper):
        x = 33
        y = 8
        ab = 2
        
        bew = textFunctions.textField(f"Taste", x - 1, y - 1, textKoerper, rev=1)
        bew.drawField(blockSize, SCREEN)
        bew = textFunctions.textField(f"Anzahl", x - 1 + 3, y - 1, textKoerper, rev=1)
        bew.drawField(blockSize, SCREEN)

        for i in range(self.counter):
            bew = textFunctions.textField(f"{i+1}", x, y + (ab * i), textKoerper, rev=1)
            bew.drawField(blockSize, SCREEN)

            if len(charac.items) - 1 >= i:
                bew = textFunctions.textField(f"{charac.items[i].count}", x + 3, y + (ab * i) + 1, textKoerper, rev=1)
                rec = pygame.Rect((grid.gridCordinat(x + 1, y + (ab * i), blockSize)), (blockSize * 2, blockSize * 2))
                SCREEN.blit(charac.items[i].img, rec)
            else:
                bew = textFunctions.textField(f"0", x + 3, y + (ab * i) + 1, textKoerper, rev=1)
            bew.drawField(blockSize, SCREEN)

            rec = pygame.Rect((grid.gridCordinat(x, y + (ab * i), blockSize)), (blockSize * 4, blockSize * 2))
            pygame.draw.rect(SCREEN, (255,255,255), rec, 4)

            rec = pygame.Rect((grid.gridCordinat(x + 1, y + (ab * i), blockSize)), (blockSize * 2, blockSize * 2))
            pygame.draw.rect(SCREEN, (255,255,255), rec, 4)


        bew = textFunctions.textField(f"Runde", x, y + 8, textKoerper, rev=1)
        bew.drawField(blockSize, SCREEN)
        bew = textFunctions.textField(f"{rod.roundNr}", x + 1, y + 9, textKoerper, rev=1)
        bew.drawField(blockSize, SCREEN)
        rec = pygame.Rect((grid.gridCordinat(x, y + 8, blockSize)), (blockSize * 3, blockSize * 2))
        pygame.draw.rect(SCREEN, (255,255,255), rec, 4)