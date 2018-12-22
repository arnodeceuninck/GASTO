class PuntenLijst:
    def __init__(self, id, type, periode, namecodes, vakcode, klas, uren, toetsen):
        self.id = id
        self.type = type
        self.periode = periode
        self.namecodes = namecodes
        self.vakcode = vakcode
        self.klas = klas
        self.uren = uren
        self.toetsen = toetsen

    def addToets(self, toets):
        self.toetsen.append(toets)
        return True

    def getID(self):
        return self.id

    def setID(self, id):
        self.id = id
        return True

    def getType(self):
        return self.type

    def setType(self, Type):
        self.type = Type
        return True

    def getPeriode(self):
        return self.periode

    def setPeriode(self, periode):
        self.periode = periode
        return True

    def getNameCodes(self):
        return self.namecodes

    def setNameCodes(self, namecodes):
        self.namecodes = namecodes
        return True

    def getVakcode(self):
        return self.vakcode

    def setVakcode(self, vakcode):
        self.vakcode = vakcode
        return True

    def getKlas(self):
        return self.klas

    def setKlas(self, klas):
        self.klas = klas
        return True

    def getUren(self):
        return self.uren

    def setUren(self, uren):
        self.uren = uren
        return True

    def getToetsen(self):
        return self.toetsen

    def setToetsen(self, toetsen):
        self.toetsen = toetsen
        return True


def createPuntenLijst(id, type, periode, namecodes, vakcode, klas, uren, toetsen):
    return PuntenLijst(id, type, periode, namecodes, vakcode, klas, uren, toetsen)