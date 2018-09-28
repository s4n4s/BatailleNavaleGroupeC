import threading
import socket
from GameMap import GameMap

class Server(threading.Thread):

    map = ""
    def __init__(self, clientsocket):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket
        self.map = GameMap()
        #self.event = event

    def run(self):
        while True:
            print(">> ")
            r = self.clientsocket.recv(2048)
            r = r.decode()
            if r == "admin admin":
                self.clientsocket.send("Connecté en tant qu'administrateur"
                                       "\nVeuillez choisir une map"
                                       "\n- Map_1 tapez 1"
                                       "\n- Map_2 tapez 2".encode())

                r = self.clientsocket.recv(2048)
                r = r.decode()
                if r == "1":
                    self.clientsocket.send("map1 chargée".encode())
                    self.map.insertCoord("map_1.txt")
                    print(self.map.showMap())

                elif r == "2":
                    self.map.insertCoord("map_2.txt")
                    self.clientsocket.send("map2 chargée".encode())
                    print(self.map.showMap())
                else:
                    self.clientsocket.send("Erreur de saisie".encode())

                """while r != "1" or r != "2":
                    r = self.clientsocket.recv(2048)
                    r = r.decode()
                    self.clientsocket.send("Veuillez saisir un nombre valide".encode())"""

            else:
                self.clientsocket.send("Echec de l'authentification.".encode())
            #self.clientsocket.send(r.encode())
        #self.event.set()
