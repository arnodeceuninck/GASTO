class Rapport:
    # TODO: html bestanden laten genereren met de input
    def __init__(self, list, Zoeksleutel):
        self.list = list
        self.Zoeksleutel = Zoeksleutel

    def getList(self):
        return self.list

    def setList(self, list):
        self.list = list
        return True

    def addList(self, list):
        return self.list.append(list)

    def getZoeksleutel(self):
        return self.Zoeksleutel

    def setZoeksleutel(self, Zoeksteutel):
        self.Zoeksleutel = Zoeksteutel
        return True

    def deletePuntenLijst(self, key):
        for i in range(len(self.list)-1, -1, -1):
            if self.list[i].getID() == key:
                del self.list[i]

def createRapport(list, Zoeksleutel):
    return Rapport(list, Zoeksleutel)
