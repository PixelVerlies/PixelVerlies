import textFunctions
import sql
import random

def dungeonEnd(rod, fild_leng, fild_high, SCREEN, blockSize, ueberschrift, counter, data, charac):
    run = True
    x = int(fild_leng / 2 - 9)
    y = int(fild_high / 2 - 1)
    if rod.end == 1:
        messeg = textFunctions.textField("Dungeon Gewonnen!", x, y, ueberschrift, 18)
        if rod.loot:
            looten(data, rod, charac)
            expirence(data, rod.level, charac)
            rating(data, rod, charac)
            rod.loot = False
    elif rod.end == 2:
        messeg = textFunctions.textField("Game Over!", x, y, ueberschrift, 18)
    messeg.drawField(blockSize, SCREEN)
    counter -= 1
    if counter == 0:
        run = False
    return counter, run

def looten(data, rod, charac):
    lisItems = sql.loadItems(data, charac)
    lis = sql.loadWinItems(data, rod.level)
    searchLis = lis

    for i in searchLis:
        for j in lisItems:
            if i == j:
                lis.remove(i)

                print(lis)

    if len(lis) > 0:
        win = random.randint(0, len(lis)-1)
        sql.saveWin(data, charac, lis[win])

def expirence(data, level, charac):
    characEp = list(sql.loadExpirence(data, charac))
    ep = list(sql.loadWinExpirence(data, level, characEp))
    characEp[0] += ep[0][0]  

    if characEp[0] >= ep[1][1]:
        characEp[1] += 1
        characEp[2] += random.randint(1, characEp[3])

    sql.saveExpirence(data, charac, characEp)

    
def rating(data, rod, charac):
    sql.saveRating(data, rod, charac)
