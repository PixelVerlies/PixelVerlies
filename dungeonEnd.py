import textFunctions
import sql
import random

def dungeonEnd(rod, fild_leng, fild_high, SCREEN, blockSize, ueberschrift, counter, data, charac, current_site):
    #Setzt die Kordinaten für die Nachricht
    x = int(fild_leng / 2 - 9)
    y = int(fild_high / 2 - 1)

    #Entscheidung ob gewonnen oder verloren
    if rod.end == 1:
        #Erzeugt die gewonnen Nachricht
        messeg = textFunctions.textField("Dungeon Gewonnen!", x, y, ueberschrift, 18)

        #Sorgt dafür dass nur ein Gewinn generiert wird
        if rod.loot:
            #Generiert das Gewinnitem
            looten(data, rod, charac)

            #Generiert die Gewinn EP
            expirence(data, rod.level, charac)

            #Speichert den gewonnen Dungeon
            rating(data, rod, charac)
            rod.loot = False
    elif rod.end == 2:
        #Erzeugt die verloren Nachricht
        messeg = textFunctions.textField("Game Over!", x, y, ueberschrift, 18)

    #Zeichnet die Nachricht
    messeg.drawField(blockSize, SCREEN)

    #Zählt Anzeigedauer runter
    counter -= 1
    if counter == 0:
        current_site = 3
    
    return counter, current_site

def looten(data, rod, charac):
    #Läd alle Items des Charakters
    lisItems = sql.loadItems(data, charac)

    #Läd mögliche Gewinnitems 
    lis = sql.loadWinItems(data, rod.level)
    searchLis = lis

    #Verhindert dopplungen 
    for i in lisItems:
        if i in searchLis:
            lis.remove(i)

    if len(lis) > 0:
        #Würfelt den Gewinn aus
        win = random.randint(0, len(lis)-1)

        #Speichert den Gewinn
        sql.saveWin(data, charac, lis[win])

def expirence(data, level, charac):
    #Läd aktuelle Daten vom Charakter
    characEp = list(sql.loadExpirence(data, charac))

    #Lad Daten für den aktuelle Dungeon
    ep = list(sql.loadWinExpirence(data, level, characEp))

    #Erhöhung der EP
    characEp[0] += ep[0][0]  

    #Charakter Levelaufstieg 
    if characEp[0] >= ep[1][1]:
        characEp[1] += 1
        characEp[2] += random.randint(1, characEp[3])

    #Speichert die neuen EP
    sql.saveExpirence(data, charac, characEp)

    
def rating(data, rod, charac):
    #Speichert den abgeschlossenen Dungeon
    sql.saveRating(data, rod, charac)
