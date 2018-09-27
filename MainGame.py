import Tools


class MainGame(Tools.Tools):

    WIDTH = 10
    map = []


    def __init__(self):
        super().__init__()
        self.createMap();

    def createMap(self):
        i = 0
        while( i < self.WIDTH):
            self.map.append(["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"])
            i = i + 1


    def isOvertaking(self, coordinate):  # depassement
        if coordinate[0] >= self.WIDTH or coordinate[1] >= self.WIDTH:
            print("Veuillez saisir des coordonnées valides")
            return False
        else:
            return True


    def isOverlaping(self, coordinate):  # chevauchement
        if self.map[coordinate[0]][coordinate[1]] == "0":
            return True
        else:
            print("Cet emplacement est reservé")
            return False

    def insertCoord(self):
        coordinate = self.formatCoord("map_1.txt")
        i = 0
        while(i < len(coordinate)):
            if not self.isOvertaking(coordinate[i]):
                return "Veuillez prendre un coordonnées inferieur a 10"
            elif not self.isOverlaping(coordinate[i]):
                return "Cette case est reservée"
            else:
                self.map[coordinate[i][0]][coordinate[i][1]] = "+"
            i = i + 1





    def showMap(self):
        self.saveFileBin("map_bin",self.map)
        return self.map


    def openMap(self):
        return self.openFileBin("map_bin")


mg = MainGame()
mg.insertCoord()

i = 0
while i < 10:
    j = 0
    print("\n", end="")
    while j < 10:
        #print(mg.showMap()[i][j], end=" ")
        print(mg.openMap()[i][j], end=" ")
        j = j + 1
    i = i + 1
