import Tools

class Game(Tools.Tools):

    coordinates = []
    map = []

    def __init__(self):
        super().__init__()
        self.coordinates = self.formatCoord("map_1.txt")
        self.map = self.openFileBin("map_bin")

    def isHit(self, enteredCoord):
        i = 0
        while i < len(self.coordinates):
            if enteredCoord[0] == self.coordinates[i][0] \
                and enteredCoord[1] == self.coordinates[i][1] \
                and self.coordinates[i][1] != "T" :
                return True
            i = i + 1
        return False

    def saveStatus(self, enteredCoord):
        if self.isHit(enteredCoord):
            self.map[enteredCoord[0]][enteredCoord[1]] = "T"
            self.saveFileBin("map_bin", self.map)
        return self.map