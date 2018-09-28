import socket
import threading
from Game import Game
from GameMap import GameMap
from Server import Server
import User


class GameRun:

	game = ""
	gameMap = ""
	user = ""
	server = ""
	def __init__(self):
		self.game = Game()
		self.gameMap = GameMap()






tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.bind(("", 1111))
while True:
	tcpsock.listen(10)
	print("En écoute...")
	(clientsocket, (ip, port)) = tcpsock.accept()
	#event = threading.Event()
	#event.clear()
	newthread = Server(clientsocket)
	newthread.start()
	#event.wait()

