import textFunctions

def dungeonEnd(rod, SCREEN, blockSize, ueberschrift, counter):
    run = True
    if rod.end == 1:
        messeg = textFunctions.textField("Dungeon Gewonnen!", 20, 10, ueberschrift)
    elif rod.end == 2:
        messeg = textFunctions.textField("Game Over!", 20, 10, ueberschrift)
    messeg.drawField(blockSize, SCREEN)
    counter -= 1
    if counter == 0:
        run = False
    return counter, run