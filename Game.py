import Tools

class Game(Tools.Tools):

    coordinates = []

    def __init__(self):
        super().__init__()
        self.coordinates = self.formatCoord("map_1.txt")

    def isHit(self, enteredCoord):
        i = 0
        while i < len(self.coordinates):
            if enteredCoord[0] == self.coordinates[i][0] and enteredCoord[1] == self.coordinates[i][1]:
                return True
            i = i + 1
        return False





gmd = Game()

print(gmd.isHit([10,10]))