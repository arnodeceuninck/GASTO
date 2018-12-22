import Leerling
import Punt
import Rapport
import stack
import Toets
import Wachtlijst
import _234T
import Dubbelgelinktelijst


class system:
    def __init__(self):
        self.punten = _234T.createSearchTree()


    def addPunt(self):
        ID = input("ID: ")
        self.punten._234TInsert(_234T.TreeItem(Punt.createPunt(ID, input("Stamboomnummer: "), input("Naam: "),
                                                                    input("Waarde: "), input("Timestamp: ")), ID))
        return True

    def deletePunt(self):
        self.punten._234TDelete(input("ID: "))
        return True

    def retrievePunt(self):
        self.punten.retrieve(input("ID: "))

    def removeAllPunten(self):
        self.punten.destroyList()



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

