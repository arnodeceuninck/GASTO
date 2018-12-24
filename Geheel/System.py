import Leerling
import Punt
import Leraar
import Rapport
import Stack
import Toets
import ADTQueue
import Puntenlijst

import HtmlMaker

# Hier geen ADT Tabellen importeren! Dit gebeurt via TabelWrapper
from TabelWrapper import *


# Todo: retrieve info over de testen geven


class system:
    def __init__(self):
        # TODO: De klassen toets, rapport, puntenlijst moeten ontworpen zoals de ADT tabel.
        #  Deze klassen zijn dus een verzameling van als ik het goed begrijp
        # TODO: Fix error: alle elementen met zelfde datastructuur komen samen in eenzelfde datastructuur
        self.punten = TabelWrapper("23")  # dit is de create # puntenlijst nog nodig om punten aan te passen
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
        if self.retrieveLeerling(studentennummer) is not False:
            print("De gegeven studenten nummer is al in gebruik")
            return False
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
        #TODO: alle toetsen overlopen en de punten uit de toetsen halen
        self.punten.delete(ID)
        return True

    def deleteVak(self, afkorting):
        if self.vakken.delete(afkorting):
            print("Vak succesvol verwijderd")
            return True
        else:
            print("ERROR: Vak" + afkorting + "Zit niet in het systeem")
            return False

    def deleteKlas(self, naam):
        if self.klassen.delete(naam):
            print("Klas succesvol verwijderd")
            return True
        else:
            print("ERROR: Klas" + naam + "Zit niet in het systeem")

    def deleteLeerling(self, key):
        #TODO: elke datastructuur toevoegen aan de delete

        #de punten die gelinkt zijn aan het stamboom nummer verwijderen

        if self.punten.type == "cl":
            node = self.punten.dataStructure.head.next
            for x in range(self.toetsen.dataStructure.count):
                if node.value.getStamboekNummer == key:
                    nextnode = node.next
                    self.deletePunt(node.value.getID())
                    node = nextnode
                else:
                    node = node.next
        elif self.punten.type == "ll":
            node = self.punten.dataStructure.dummy.next
            while node is not None:
                if node.value.getStamboekNummer == key:
                    nextnode = node.next
                    self.deletePunt(node.value.getID())
                else:
                    nextnode = node.next
                node = nextnode
        elif self.punten.type == "234":
            self.punten.dataStructure.traverse(self.collector, key)
        elif self.punten.type == "23":
            self.punten.dataStructure.traverse(self.collector, key)

        #alle punten uit de testen verwijderen
        if self.toetsen.type == "cl":
            node = self.toetsen.dataStructure.head.next
            for x in range(self.toetsen.dataStructure.count):
                for i in range(len(node.value.verzamelingVanPunten)-1):
                    if node.value.verzamelingVanPunten[i].getStamboekNummer == key:
                        del node.value.verzamelingVanPunten[i]
                node = node.next
        elif self.toetsen.type == "ll":
            node = self.toetsen.dataStructure.dummy.next
            while node is not None:
                for i in range(len(node.value.verzamelingVanPunten)-1):
                    if node.value.getStamboekNummer[i].getStamboekNummer == key:
                        del node.verzamelingVanPunten[i]
                node = node.next

        self.leerlingen.delete(key)

    def deletePuntenlijst(self, key):
        puntenlijst = self.puntenlijst.retrieve(key)
        for i in range(len(puntenlijst.toetsen)-1, -1, -1):
            self.deleteToets(puntenlijst.toetsen[i].getNaam())
            del puntenlijst.toetsen[i]
        self.puntenlijst.delete(key)

    def deleteToets(self, naam):
        toets = self.retrieveToets(naam)
        for i in range(len(toets.verzamelingVanPunten)-1, -1, -1):
            self.deletePunt(toets.verzamelingVanPunten[i].getID())
            del toets.verzamelingVanPunten[i]
        #TODO: Als het een cl is dan is dit het speciaal geval, controleren hoe te werk gaan bij andere datastructuren # Hoezo een speciaal geval? # Omda ge eerst de index moet vinden en bij de andere niet
        self.toetsen.delete(self.toetsen.dataStructure.findIndexValue(naam))

    def retrievePunt(self, key):
        # Vraag een specifiek punt op
        return self.punten.retrieve(key)

    def removeAllPunten(self):
        # Verwijdert alle punten in het systeem (in theorie nooit nodig)
        self.punten.destroy()

    def collector(self, item, key):
        #TODO: veel efficienter maken
        if item.getStamboekNummer() == key:
            self.deletePunt(item.getID())
            self.punten.dataStructure.traverse(self.collector, key)
            return True
        else:
            return False


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

    def buildRapport(self):

        # TODO: Maak hier nu een echt rapport van

        rapport = HtmlMaker.HtmlRapport("Rapport.html")
        rapport.addStructure(HtmlMaker.HtmlTitle("Rapport: eigenlijk gewoon een overzicht van alle punten"))

        puntentabel = []
        puntentabel.append(["ID", "Student", "Toets", "Score", "Maxscore", "Timestamp"])
        for punt in self.punten:
            punt_value = punt[1]
            puntentabel.append([punt_value.id,
                                punt_value.stamboomnummer,
                                punt_value.name,
                                punt_value.waarde,
                                self.toetsen.retrieve(punt_value.name).maximum,
                                punt_value.timestamp])

        rapport.addStructure(HtmlMaker.HtmlTable(puntentabel))

        rapport.buildfile()


