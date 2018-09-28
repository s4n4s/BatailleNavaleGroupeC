import threading, time, socket
from GameMap import GameMap
from Tools import Tools
adminOnline = False
map = GameMap()
nbPlayers = 4
class Server(threading.Thread):


    ver = threading.RLock()


    def __init__(self, clientsocket):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket
        self.tool = Tools()

    def run(self):

        global adminOnline
        global map
        global nbPlayers

        nbPlayers = nbPlayers - 1
        while True:
            print(">> ")
            r = self.clientsocket.recv(2048)
            r = r.decode()


            print(nbPlayers)
            if nbPlayers > 0:

                users = self.tool.readFile("users.txt")
                users = users.split("\n")
                result = r in users


                if r == "admin admin":
                    if not adminOnline:
                        adminOnline = True

                        self.clientsocket.send("Connecté en tant qu'administrateur"
                                                   "\nVeuillez choisir une map"
                                                   "\n- Map_1 tapez 1"
                                                   "\n- Map_2 tapez 2".encode())

                        r = self.clientsocket.recv(2048)
                        r = r.decode()
                        if r == "1":
                            map.insertCoord("map_1.txt")
                            self.clientsocket.send("map1 chargée".encode())
                            print(map.showMap())

                        elif r == "2":
                            map.insertCoord("map_2.txt")
                            self.clientsocket.send("map2 chargée".encode())
                            print(map.showMap())
                        else:

                            self.clientsocket.send("Erreur de saisie".encode())

                            """while r != "1" or r != "2":
                                r = self.clientsocket.recv(2048)
                                r = r.decode()
                                self.clientsocket.send("Veuillez saisir un nombre valide".encode())"""

                    else:

                        self.clientsocket.send(
                                "L'administrateur est en ligne\nVeuillez saisir vos identifiants utilisateur".encode())

                elif result:
                    self.clientsocket.send("Vous êtes connectés en attente d'autres joueurs".encode())
                    while map.
                else:
                    self.clientsocket.send("Echec de l'authentification".encode())
            else:
                self.clientsocket.send("Le nombre de joueurs maximum a été atteint".encode())
            #self.event.set()
