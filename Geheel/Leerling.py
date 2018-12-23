class Leerling:
    def __init__(self, Naam, Voornaam, Klas, KlasNummer, nummer):
        self.Naam = Naam
        self.Voornaam = Voornaam
        self.Klas = Klas
        self.KlasNummer = KlasNummer
        self.nummer = nummer

    def __str__(self):
        return self.Naam + " - " + self.Voornaam + " - " + self.Klas + " - " + self.KlasNummer + " - " + self. nummer

    def getNummer(self):
        return self.nummer

    def setNummer(self, nummer):
        self.nummer = nummer
        return True

    def getVoornaam(self):
        return self.Voornaam

    def setVoornaam(self, voornaam):
        self.Voornaam = voornaam
        return True

    def getNaam(self):
        return self.Naam

    def setNaam(self, naam):
        self.Naam = naam
        return True

    def getKlas(self):
        return self.Klas

    def setKlas(self, klas):
        self.Klas = klas
        return True

    def getKlasNummer(self):
        return self.KlasNummer

    def setKlasNummer(self, klasnummer):
        self.KlasNummer = klasnummer
        return True

