import sql

class healingPotion():
    def __init__(self, res):
        self.itemId = res[3]
        self.name = res[0]
        self.healing = res[1]
        self.count = res[2]
        self.img = None

    def loadImg(self, img):
        self.img = img