import textFunctions

def dungeonEnd(rod, fild_leng, fild_high, SCREEN, blockSize, ueberschrift, counter):
    run = True
    x = int(fild_leng / 2 - 9)
    y = int(fild_high / 2 - 1)
    if rod.end == 1:
        messeg = textFunctions.textField("Dungeon Gewonnen!", x, y, ueberschrift, 18)
    elif rod.end == 2:
        messeg = textFunctions.textField("Game Over!", x, y, ueberschrift, 18)
    messeg.drawField(blockSize, SCREEN)
    counter -= 1
    if counter == 0:
        run = False
    return counter, run