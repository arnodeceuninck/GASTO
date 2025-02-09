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

    def __str__(self):
        return str(self.type) + str(self.periode) + " - " + \
               str(self.vakcode) + " - " +\
               str(self.klas)

    def addToets(self, toets):
        self.toetsen.append(toets)
        return True

    def deleteToets(self, naam):
        for i in range(len(self.toetsen)-1, -1, -1):
            if self.toetsen[i].naam == naam:
                del self.toetsen[i]

    def deleteNamecodes(self, code):
        for i in range(len(self.namecodes)-1, -1, -1):
            if self.namecodes[i] == code:
                del self.namecodes[i]

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

    def getLeerkrachtenStr(self):
        string = ""
        i = 0
        for leerkracht in self.namecodes:
            i += 1
            string += leerkracht
            if i != len(self.namecodes):
                string += ","
        return string


def createPuntenLijst(id, type, periode, namecodes, vakcode, klas, uren, toetsen):
    return PuntenLijst(id, type, periode, namecodes, vakcode, klas, uren, toetsen)