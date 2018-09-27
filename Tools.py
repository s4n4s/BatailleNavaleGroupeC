import pickle

class Tools:

    tab = []
    def readFile(self, fileName): #lit un fichier
        f = open(fileName, "r")
        content = f.read();
        f.close()
        return str(content)

    def saveFileBin(self, fileName, data): #Enregistre la map dans un fichier
        with open(fileName, 'wb') as f:
            mon_pickler = pickle.Pickler(f)
            mon_pickler.dump(data)

    def openFileBin(self, fileName): #Ouvrir la map en cours
        with open(fileName, 'rb') as f:
            my_pickler = pickle.Unpickler(f)
            return my_pickler.load()

    def formatCoord(self, fileName): #format les coordnnées pour l'insertion
        txt = self.readFile(fileName)
        txt = txt.strip()
        txt = txt.replace("\n", " ")
        txt = txt.split(" ")
        for i in txt:
            self.tab.append(i.split(","))

        i = 0
        while i < len(self.tab):
            j = 0
            while j < len(self.tab[i]):
                self.tab[i][j] = int(self.tab[i][j])
                j = j + 1
            i = i + 1
        return self.tab

#test = Tools()

#print(len(test.formatCoord("map_1.txt")))