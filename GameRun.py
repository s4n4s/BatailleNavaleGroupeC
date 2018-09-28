from Game import Game
from GameMap import GameMap
from Server import Server
import User


class GameRun:

	game = ""
	gameMap = ""
	user = ""
	server = ""
	def __init__(self, clientSocket):
		self.game = Game()
		self.gameMap = GameMap()
		self.server = Server(clientSocket)

	def GameExec(self):
		self.server.initConn()


test = GameRun()
print(test.typeOfCla())

