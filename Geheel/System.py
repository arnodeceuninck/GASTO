import Leerling
import Punt
import Rapport
import Stack
import Toets
import Queue
import Puntenlijst

# Hier geen ADT Tabellen importeren! Dit gebeurt via TabelWrapper
from TabelWrapper import *

#Todo: retrieve info over de testen geven


class system:
    def __init__(self):
        self.punten = TabelWrapper("ll") # dit is de create
        self.toetsen = TabelWrapper("cl")
        self.puntenlijst = TabelWrapper("bst")

    def addPunt(self):
        ID = input("ID: ")
        self.punten.insert(Punt.createPunt(ID, input("Stamboomnummer: "),  # Value
                                           input("Naam: "),
                                           input("Waarde: "),
                                           input("Timestamp: ")),
                           ID)  # Key
        return True

    def deletePunt(self):
        self.punten.delete(input("ID: "))
        return True

    def retrievePunt(self, key):
        return self.punten.retrieve(key)

    def removeAllPunten(self):
        self.punten.destroy()

    def addToets(self):
        ID = input("Naam: ")
        puntenlist = []
        while True:
            IDtest = input("ID test: ")
            if IDtest == "":
                break
            else:
                puntenlist.append(IDtest)
        for i in range(len(puntenlist)-1):
            if self.retrievePunt(puntenlist[i]) is not None:
                puntenlist[i] = self.retrievePunt(puntenlist[i])
            else:
                print("ID van punt bestaat niet")

        idascii = int(''.join(str(ord(c)) for c in ID))
        #idascii = idascii[1:(len(idascii)-1)]

        self.toetsen.insert(Toets.createToets(ID,
                                              input("Maximum: "),
                                              puntenlist), int(idascii))

    def retrieveToets(self):
        return self.toetsen.retrieve(input("Naam toets: "))
