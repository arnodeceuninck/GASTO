class Rapport:
    def __init__(self, list, Zoeksleutel):
        self.list = list
        self.Zoeksleutel = Zoeksleutel

    def getList(self):
        return self.list

    def setList(self, list):
        self.list = list
        return True

    def getZoeksleutel(self):
        return self.Zoeksleutel

    def setZoeksleutel(self, Zoeksteutel):
        self.Zoeksleutel = Zoeksteutel
        return True


def createRapport(list, Zoeksleutel):
    return Rapport(list, Zoeksleutel)
