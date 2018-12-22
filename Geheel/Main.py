import Leerling
import Punt
import Rapport
import stack
import Toets
import Wachtlijst

# Hier geen ADT Tabellen importeren! Dit gebeurt via TabelWrapper
from TabelWrapper import *


class system:
    def __init__(self):
        self.punten = TabelWrapper("234") # dit is de create

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

    def retrievePunt(self):
        self.punten.retrieve(input("ID: "))

    def removeAllPunten(self):
        self.punten.destroy()


geheel = system()
print("Welkom!")
while True:
    temp = input("(1) punt toevoegen, (2) delete, (e)" + '\n')
    if temp == "e":
        break
    if temp == "1":
        geheel.addPunt()
    elif temp == "2":
        geheel.deletePunt()
