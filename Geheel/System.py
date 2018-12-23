import Leerling
import Punt
import Leraar
import Rapport
import Stack
import Toets
import ADTQueue
import Puntenlijst

# Hier geen ADT Tabellen importeren! Dit gebeurt via TabelWrapper
from TabelWrapper import *


# Todo: retrieve info over de testen geven


class system:
    def __init__(self):
        # TODO: De klassen toets, rapport, puntenlijst moeten ontworpen zoals de ADT tabel.
        #  Deze klassen zijn dus een verzameling van als ik het goed begrijp
        # TODO: Fix error: alle elementen met zelfde datastructuur komen samen in eenzelfde datastructuur
        self.punten = TabelWrapper("ll")  # dit is de create # puntenlijst nog nodig om punten aan te passen
        self.toetsen = TabelWrapper("cl")  # TODO: verander dit terug naar cl
        self.puntenlijst = TabelWrapper("234")  # TODO: verander terug naar bst als er een bst in Geheel zit
        # self.puntenlijst = TabelWrapper("bst")  # Is dus eigenlijk een verzameling van alle puntenlijsten
        self.vakken = TabelWrapper("ll")  # Key = afkorting, Value = volledige naam
        self.klassen = TabelWrapper("ll")
        self.leraars = TabelWrapper("ll")
        self.leerlingen = TabelWrapper("ll")

    def addVak(self, afkorting, naam):
        return self.vakken.insert(naam, afkorting)

    def addKlas(self, naam):
        return self.klassen.insert(naam)

    def addLeraar(self, afkorting, naam, achternaam):
        return self.leraars.insert(Leraar.Leraar(afkorting, naam, achternaam), afkorting)

    def addLeerling(self, naam, voornaam, klas, klasnummer, studentennummer):
        # TODO: test for unique studentnumber

        # Kijk of de klas al is aangemaakt
        if self.klassen.retrieve(klas) is None:
            print("ERROR: De klas waar je de leerling wil insteken (" + klas + "), bestaat nog niet. "
                                                                               "Gelieve deze eerst aan te maken.")
            return False

        return self.leerlingen.insert(Leerling.Leerling(naam, voornaam, klas, klasnummer, studentennummer),
                                          studentennummer)

    def addPunt(self, ID, stamboeknummer_leerling, naam_toets, Waarde, Timestamp):
        # maakt een nieuw punt aan met een uniek ID, Stamboomnummer, Naam, Waarde en Timestamp
        toets = self.toetsen.retrieve(naam_toets)
        if toets is None:
            print("ERROR: De toets " + naam_toets + " werd niet teruggevonden in het systeem. "
                  "Gelieve deze eerst aan te maken.")
            return False
        if self.leerlingen.retrieve(stamboeknummer_leerling) is None:
            print("ERROR: Het studentennummer " + stamboeknummer_leerling + " werd niet teruggevonden in het systeem. "
                  "Gelieve deze eerst aan te maken.")
            return False
        punt = Punt.createPunt(ID, stamboeknummer_leerling, naam_toets, Waarde, Timestamp)
        self.punten.insert(punt, ID)  # Key
        toets.addPunt(punt)
        return True

    def addPuntenLijst(self, ID, type, periode, namecodes, vak_afkorting, klas, uren):
        if self.klassen.retrieve(klas) is None:
            print("ERROR: De klas waaraan je wil dat de leeraar les geeft (" + klas + "), bestaat nog niet. "
                  "Gelieve deze eerst aan te maken.")
            return False

        leraren = namecodes.split(',')
        for leraar in leraren:
            if self.leraars.retrieve(leraar) is None:
                print("ERROR: De leraar " + leraar + " werd niet teruggevonden in het systeem. "
                      "Gelieve deze eerst aan te maken")
                return False

        return self.puntenlijst.insert(Puntenlijst.createPuntenLijst(ID, type, periode, namecodes, vak_afkorting,
                                                                     klas, uren, []),
                                       ID)  # Dit kan niet, want ID is meegegeven: Zoeksleutel is bv "M" + "3" = "M3"

    def addToets(self, puntenlijst_id, titel, maxscore):
        puntenlijst = self.puntenlijst.retrieve(puntenlijst_id)
        if puntenlijst is None:
            print("ERROR: De puntenlijst met id " + puntenlijst_id + " werd niet teruggevonden in het systeem. "
                                                 "Gelieve deze eerst aan te maken")
            return False
        toets = Toets.createToets(puntenlijst, titel, maxscore, [])
        self.toetsen.insert(toets, titel)
        puntenlijst.addToets(toets)

    def deletePunt(self, ID):
        # verwijdert een eerder aangemaakt punt
        self.punten.delete(ID)
        return True

    def retrievePunt(self, key):
        # Vraag een specifiek punt op
        return self.punten.retrieve(key)

    def removeAllPunten(self):
        # Verwijdert alle punten in het systeem (in theorie nooit nodig)
        self.punten.destroy()

    # def addToets(self):
    #     # Maakt toetsen aan bij puntenlijst 'ID'
    #     # TODO: Verplaats alles van input naar main, dat maakt het makkelijker om achteraf een GUI te maken
    #
    #     ID = input("Naam: ")  # De titel van de toets
    #     puntenlist = []  # !!! Is een verzameling van punten, geen puntenlijst !!! # TODO: change name?
    #
    #     while True:
    #         # Blijf punten toevoegen aan de lijst tot je geen ID meegeeft
    #         IDPunt = input("ID Punt: ")
    #
    #         if IDPunt == "":
    #             break
    #         else:
    #             punt = self.retrievePunt(IDPunt)
    #             if punt is not None:
    #                 puntenlist.append(punt)
    #             else:
    #                 print("ID van punt bestaat niet")
    #
    #     # idascii = int(''.join(str(ord(c)) for c in ID))
    #     # idascii = idascii[1:(len(idascii)-1)]
    #
    #     self.toetsen.insert(Toets.createToets(ID, input("Maximum: "), puntenlist),  # Value
    #                         ID)  # Key

    def retrieveToets(self, naam_toets):
        return self.toetsen.retrieve(naam_toets)

    def retrieveKlas(self, naam):
        return self.klassen.retrieve(naam)

    def retrievePuntenlijst(self, ID):
        return self.puntenlijst.retrieve(ID)

    def retrieveLeerling(self, studentennr):
        return self.leerlingen.retrieve(studentennr)

    def retrieveLeeraar(self, afkorting):
        return self.leraars.retrieve(afkorting)

    def retrieveKlas(self, naam):
        return naam

    def retrieveVak(self, afkorting):
        return self.vakken.retrieve(afkorting)
