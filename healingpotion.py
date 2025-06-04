#import sql
import grid

class healingPotion():
    def __init__(self, res):
        #Anlage der Variablen des Heiltrankes
        self.itemId = res[3]
        self.name = res[0]
        self.healing = res[1]
        self.count = res[2]
        self.img = None

    def loadImg(self, blockSize):
        #Passender Pfad für das Bild wird gesetzt
        path = ""
        match self.itemId:
            case 1:
                path = "Images/Items/small.png"
            case 2:
                path = "Images/Items/medium.png"
            case 3:
                path = "Images/Items/big.png"
            
        #Bild für den Heiltrank wird geladen
        self.img = grid.importImage(path, blockSize * 2)