import threading, time, socket
from GameMap import GameMap
adminOnline = False
map = GameMap()
nbPlayers = 4
class Server(threading.Thread):


    ver = threading.RLock()


    def __init__(self, clientsocket):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket
        #self.event = event

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

                if not adminOnline:
                    if r == "admin admin":
                        adminOnline = True

                        self.clientsocket.send("Connecté en tant qu'administrateur"
                                               "\nVeuillez choisir une map"
                                               "\n- Map_1 tapez 1"
                                               "\n- Map_2 tapez 2".encode())

                        r = self.clientsocket.recv(2048)
                        r = r.decode()
                        if r == "1":
                            self.map.insertCoord("map_1.txt")
                            self.clientsocket.send("map1 chargée".encode())
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
                else:
                    self.clientsocket.send("L'administrateur est en ligne\nVeuillez saisir vos identifiants utilisateur".encode())
                #self.clientsocket.send(r.encode())
            else:
                self.clientsocket.send("Le nombre de joueurs maximum a été atteint".encode())
        #self.event.set()
