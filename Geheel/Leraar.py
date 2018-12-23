class Leraar:
    def __init__(self, afkorting, naam, achternaam):
        self.afkorting = afkorting
        self.naam = naam
        self.achternaam = achternaam

    def __str__(self):
        return self.afkorting + " - " + self.naam + " - " + self.achternaam

    def getAfkorting(self):
        return self.afkorting

    def setAfkorting(self, afkorting):
        self.afkorting = afkorting
        return True

    def getNaam(self):
        return self.naam

    def setNaam(self, naam):
        self.naam = naam
        return True

    def getAchternaam(self):
        return self.achternaam

    def setAchternaam(self, achternaam):
        self.achternaam = achternaam
        return True


def createLeraar(afkorting, naam, achternaam):
    return Leraar(afkorting, naam, achternaam)