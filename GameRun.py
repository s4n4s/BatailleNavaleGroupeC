import Game
import GameMap
import User


class GameRun:

	game = ""
	gameMap = ""
	user = ""

	def __init__(self):
		game = Game()
		gameMap = GameMap()


	def typeOfCla(self):
		type(self.game)
		type(self.gameMap)

test = GameRun()
test.typeOfCla()

