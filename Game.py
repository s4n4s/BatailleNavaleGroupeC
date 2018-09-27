import Tools

class Game(Tools.Tools):

    coordinates = []

    def __init__(self):
        super().__init__()
        self.coordinates = self.formatCoord()

    def isHit(self):
