import pygame
import grid
import textFunctions

class itembar():
    def __init__(self, counter):
        #Erzeugt die nötigen Variablen
        self.counter = counter
        self.x = 33
        self.y = 8
        self.ab = 2

    def drawItemBar(self, rod, charac, SCREEN, blockSize, textKoerper):
        #Generiert die Überschriften
        bew = textFunctions.textField(f"Taste", self.x - 1, self.y - 1, textKoerper, rev=1)
        bew.drawField(blockSize, SCREEN)
        bew = textFunctions.textField(f"Anzahl", self.x - 1 + 3, self.y - 1, textKoerper, rev=1)
        bew.drawField(blockSize, SCREEN)

        #Erzeugt die Felder
        for i in range(self.counter):
            #Zeichnet das aktuelle Feld
            bew = textFunctions.textField(f"{i+1}", self.x, self.y + (self.ab * i), textKoerper, rev=1)
            bew.drawField(blockSize, SCREEN)

            #Generiert alles für das passende Item
            if len(charac.items) - 1 >= i:
                #Schreibt die anzahl der Items
                bew = textFunctions.textField(f"{charac.items[i].count}", self.x + 3, self.y + (self.ab * i) + 1, textKoerper, rev=1)
                #Zeichnet das Item
                rec = pygame.Rect((grid.gridCordinat(self.x + 1, self.y + (self.ab * i), blockSize)), (blockSize * 2, blockSize * 2))
                SCREEN.blit(charac.items[i].img, rec)
            else:
                #Schreibt eine 0 wenn kein Item vorhanden
                bew = textFunctions.textField(f"0", self.x + 3, self.y + (self.ab * i) + 1, textKoerper, rev=1)
            #Zeuchnet die anzahl
            bew.drawField(blockSize, SCREEN)

            #Zeichnet die nötigen Rahmen
            rec = pygame.Rect((grid.gridCordinat(self.x, self.y + (self.ab * i), blockSize)), (blockSize * 4, blockSize * 2))
            pygame.draw.rect(SCREEN, (255,255,255), rec, 4)
            rec = pygame.Rect((grid.gridCordinat(self.x + 1, self.y + (self.ab * i), blockSize)), (blockSize * 2, blockSize * 2))
            pygame.draw.rect(SCREEN, (255,255,255), rec, 4)

        #Zeichnet die Ausgabe der Rundenanzahl
        bew = textFunctions.textField(f"Runde", self.x, self.y + 8, textKoerper, rev=1)
        bew.drawField(blockSize, SCREEN)
        bew = textFunctions.textField(f"{rod.roundNr}", self.x + 1, self.y + 9, textKoerper, rev=1)
        bew.drawField(blockSize, SCREEN)
        rec = pygame.Rect((grid.gridCordinat(self.x, self.y + 8, blockSize)), (blockSize * 3, blockSize * 2))
        pygame.draw.rect(SCREEN, (255,255,255), rec, 4)