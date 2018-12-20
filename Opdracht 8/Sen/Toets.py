class Toets:
    def __init__(self, naam, maximum, verzamelingVanPunten):
        self.naam = naam
        self.maximum = maximum
        self.verzamelingVanPunten = verzamelingVanPunten

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