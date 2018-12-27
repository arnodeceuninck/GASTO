class Punt:
    #variabelen: id, stamboomnummer, naam test, een waarde (x/10), timestamp, key = id
    def __init__(self, id, stamboomnummer, naam, waarde, timestamp):
        self.id = id
        self.stamboomnummer = stamboomnummer
        self.name = naam
        self.waarde = waarde
        self.timestamp = timestamp

    def __str__(self):
        return str(self.id) + " - " + \
               str(self.stamboomnummer) + " - " + \
               str(self.name) + " - " + \
               str(self.waarde) + " - " + \
               str(self.timestamp)

    def getID(self):
        return self.id

    def getStamboekNummer(self):
        return self.stamboomnummer

    def getNaam(self):
        return self.name

    def getTimestamp(self):
        return self.timestamp

    def getWaarde(self):
        return self.waarde

    def setID(self, id):
        self.id = id
        return True

    def setStamboeknummer(self, nummer):
        self.stamboomnummer = nummer
        return True

    def setName(self, name):
        self.name = name
        return True

    def setTimestamp(self, time):
        self.timestamp = time
        return True


def createPunt(id, stamboeknummer, naam, waarde, timestamp):
    return Punt(id, stamboeknummer, naam, waarde, timestamp)