class Toets:
    def __init__(self, puntenlijst, naam, maximum, verzamelingVanPunten):
        self.puntenlijst = puntenlijst
        self.naam = naam
        self.maximum = maximum
        self.verzamelingVanPunten = verzamelingVanPunten

    def __str__(self):
        return str(self.naam) + " - " + \
               str(self.maximum) + " punten max "+ " - " + \
               str(len(self.verzamelingVanPunten)) + " punten ingegeven"

    def getNaam(self):
        return self.naam

    def setNaam(self, naam):
        self.naam = naam
        return True

    def getMaximum(self):
        return self.maximum

    def setMaximum(self, maximum):
        self.maximum = maximum
        return True

    def getVerzamelingVanPunten(self):
        return self.verzamelingVanPunten

    def setVerzamelingVanPunten(self, verzameling):
        self.verzamelingVanPunten = verzameling
        return True

    def addPunt(self, punt):
        if int(punt.waarde) >= 0 and int(punt.waarde) <= int(self.maximum):
            self.verzamelingVanPunten.append(punt)
            return True
        else:
            print("De waarde van het punt in ongeldig")
            return False

    def removePunt(self, ID):
        for i in range(len(self.verzamelingVanPunten)-1, -1, -1):
            if self.verzamelingVanPunten[i].id == ID:
                del self.verzamelingVanPunten[i]


def createToets(puntenlijst, naam, maximum, verzamelingVanPunten):
    return Toets(puntenlijst, naam, maximum, verzamelingVanPunten)
