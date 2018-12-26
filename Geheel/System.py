import Leerling
import Punt
import Leraar
import Rapport
import Stack
import Toets
import ADTQueue
import Puntenlijst

import datetime

import HtmlMaker

# Hier geen ADT Tabellen importeren! Dit gebeurt via TabelWrapper
from TabelWrapper import *


# Todo: retrieve info over de testen geven


class system:
    def __init__(self):
        # TODO: De klassen toets, rapport, puntenlijst moeten ontworpen zoals de ADT tabel.
        #  Deze klassen zijn dus een verzameling van als ik het goed begrijp
        # TODO: Fix error: alle elementen met zelfde datastructuur komen samen in eenzelfde datastructuur
        self.punten = TabelWrapper("rb")  # dit is de create # puntenlijst nog nodig om punten aan te passen
        self.toetsen = TabelWrapper("cl")  # TODO: verander dit terug naar cl
        self.puntenlijst = TabelWrapper("ll")  # TODO: verander terug naar bst als er een bst in Geheel zit
        # self.puntenlijst = TabelWrapper("bst")  # Is dus eigenlijk een verzameling van alle puntenlijsten
        self.vakken = TabelWrapper("ll")  # Key = afkorting, Value = volledige naam
        self.klassen = TabelWrapper("ll")
        self.leraars = TabelWrapper("ll")
        self.leerlingen = TabelWrapper("ll")
        self.rapporten = TabelWrapper("ll")
        self.instructies = TabelWrapper("stack")  # NOTE: Don't change this ADT

    def addVak(self, afkorting, naam):
        self.instructies.insert("vak " + str(afkorting) + " " + str(naam))
        return self.vakken.insert(naam, afkorting)

    def addKlas(self, naam):
        self.instructies.insert("klas " + str(naam))
        return self.klassen.insert(naam)

    def addLeraar(self, afkorting, naam, achternaam):
        self.instructies.insert("leraar " + str(naam) + " " + str(achternaam) + " " + str(afkorting))
        return self.leraars.insert(Leraar.Leraar(afkorting, naam, achternaam), afkorting)

    def addLeerling(self, naam, voornaam, klas, klasnummer, studentennummer):
        self.instructies.insert("leeling " + str(voornaam) + " " + str(naam) + " " + str(klas) + " " +
                                str(klasnummer) + " " + str(studentennummer))
        if self.leerlingen.retrieve(studentennummer)[0] is not False:
            print("De gegeven studenten nummer is al in gebruik")
            return False
        # Kijk of de klas al is aangemaakt
        if self.klassen.retrieve(klas) is None:
            print("ERROR: De klas waar je de leerling wil insteken (" + klas + "), bestaat nog niet. "
                                                                               "Gelieve deze eerst aan te maken.")
            return False

        return self.leerlingen.insert(Leerling.Leerling(naam, voornaam, klas, klasnummer, studentennummer),
                                          studentennummer)

    def addPunt(self, stamboeknummer_leerling, naam_toets, Waarde, leerkracht):
        ID = self.punten.getLength()
        self.instructies.insert("punt " + str(leerkracht) + " " + str(naam_toets) + " " +
                                str(stamboeknummer_leerling) + " " + str(Waarde) + " " + str(ID))
        # TODO: controleren of leerkracht bevoegd is om aan deze toets een punt toe te voegen

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
        punt = Punt.createPunt(ID, stamboeknummer_leerling, naam_toets, Waarde, datetime.datetime.now())  # https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python
        self.punten.insert(punt, ID)  # Key
        #TODO: de retrieve van een LL geeft een tuple terug ma is da echt nodig?
        if self.toetsen.type == "ll":
            toets[1].addPunt(punt)
        else:
            toets.addPunt(punt)
        return True

    def addPuntenLijst(self, ID, type, periode, namecodes, vak_afkorting, klas, uren):
        self.instructies.insert(str(ID) + " puntenlijst " + str(type) + " " + str(periode) + " " +
                                str(namecodes) + " " + str(vak_afkorting) + " " + str(klas) + " " + str(uren))
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
        puntenlijst = Puntenlijst.createPuntenLijst(ID, type, periode, leraren, vak_afkorting, klas, uren, [])
        self.puntenlijst.insert(puntenlijst, ID)

        key = str(type) + str(periode)
        rapport = self.rapporten.retrieve(key)
        if rapport[0] == False:
            self.rapporten.insert(Rapport.Rapport([puntenlijst], key), key)
        else:
            rapport[1].addList(puntenlijst)
            # Volgende 2 lijnen nodig indien problemen met mutable types
            # self.rapporten.delete(key)
            # self.rapporten.insert(rapport, key)
        return True

    def addToets(self, puntenlijst_id, titel, maxscore):
        self.instructies.insert("toets " + str(puntenlijst_id) + " " + str(titel) + " " + str(maxscore))
        puntenlijst = self.puntenlijst.retrieve(puntenlijst_id)
        if puntenlijst is None:
            print("ERROR: De puntenlijst met id " + puntenlijst_id + " werd niet teruggevonden in het systeem. "
                                                 "Gelieve deze eerst aan te maken")
            return False
        toets = Toets.createToets(puntenlijst, titel, maxscore, [])
        self.toetsen.insert(toets, titel)
        if type(puntenlijst) == tuple:
            puntenlijst[1].addToets(toets)
        else:
            puntenlijst.addToets(toets)

    def deletePunt(self, ID):
        # verwijdert een eerder aangemaakt punt
        self.toetsen.traverse(self.puntenDetect, ID)
        self.punten.delete(ID)
        return True

    def deleteVak(self, afkorting):
        if self.vakken.delete(afkorting):
            self.puntenlijst.traverse(self.puntenlijstVakDelete, afkorting)
            print("Vak succesvol verwijderd")
            return True
        else:
            print("ERROR: Vak" + afkorting + "Zit niet in het systeem")
            return False

    def deleteKlas(self, naam):
        if self.klassen.delete(naam):
            self.puntenlijst.traverse(self.puntenlijstKlasdelete, naam)
            self.leerlingen.traverse(self.leerlingKlasdelete, naam)
            self.rapporten.traverse(self.rapportKlasdetect, naam)
            print("Klas succesvol verwijderd")
            return True
        else:
            print("ERROR: Klas" + naam + "Zit niet in het systeem")

    def deleteLeerling(self, key):
        #TODO: elke datastructuur toevoegen aan de delete

        #de punten die gelinkt zijn aan het stamboom nummer verwijderen

        if self.punten.type == "cl":
            node = self.punten.dataStructure.head.next
            for x in range(self.punten.dataStructure.count):
                if node.value.getStamboekNummer() == key:
                    nextnode = node.next
                    self.deletePunt(self.punten.dataStructure.findIndexValue(node.value.getID()))
                    node = nextnode
                else:
                    node = node.next
        elif self.punten.type == "ll":
            self.punten.traverse(self.collector, key)
            # node = self.punten.dataStructure.dummy.next
            # while node is not None:
            #     if node.value.getStamboekNummer == key:
            #         nextnode = node.next
            #         self.deletePunt(node.value.getID())
            #     else:
            #         nextnode = node.next
            #     node = nextnode
        elif self.punten.type == "234" or self.punten.type == "23" or self.punten.type == "bst" or self.punten.type == "rb":
            self.punten.traverse(self.collector, key)


        #alle punten uit de testen verwijderen
        # if self.toetsen.type == "cl":
        #     node = self.toetsen.dataStructure.head.next
        #     for x in range(self.toetsen.dataStructure.count):
        #         for i in range(len(node.value.verzamelingVanPunten)-1):
        #             if node.value.verzamelingVanPunten[i].getStamboekNummer == key:
        #                 del node.value.verzamelingVanPunten[i]
        #         node = node.next
        # elif self.toetsen.type == "ll":
        #     node = self.toetsen.dataStructure.dummy.next
        #     while node is not None:
        #         for i in range(len(node.value.verzamelingVanPunten)-1):
        #             if node.value.getStamboekNummer[i].getStamboekNummer == key:
        #                 del node.verzamelingVanPunten[i]
        #         node = node.next

        self.leerlingen.delete(key)

    def deletePuntenlijst(self, key):
        puntenlijst = self.puntenlijst.retrieve(key)
        for i in range(len(puntenlijst.toetsen)-1, -1, -1):
            self.deleteToets(puntenlijst.toetsen[i].getNaam())
        self.puntenlijst.delete(key)

    def deleteToets(self, naam):
        toets = self.retrieveToets(naam)
        for i in range(len(toets.verzamelingVanPunten)-1, -1, -1):
            self.deletePunt(toets.verzamelingVanPunten[i].getID())
        self.puntenlijst.traverse(self.puntenlijstToetsenDetect, naam)
        #TODO: Als het een cl is dan is dit het speciaal geval, controleren hoe te werk gaan bij andere datastructuren # Hoezo een speciaal geval? # Omda ge eerst de index moet vinden en bij de andere niet
        self.toetsen.delete(self.toetsen.dataStructure.findIndexValue(naam))

    def deleteLeraar(self, naam):
        self.puntenlijst.traverse(self.puntenlijstleerkrachtdetect, naam)
        self.leraars.delete(naam)

    def removeAllPunten(self):
        # Verwijdert alle punten in het systeem (in theorie nooit nodig)
        self.punten.destroy()

    def collector(self, item, key):
        #TODO: veel efficienter maken
        if item.getStamboekNummer() == key:
            self.deletePunt(item.getID())
            self.punten.traverse(self.collector, key)
            return True
        else:
            return False

    def puntenlijstToetsenDetect(self, item, key):
        item.deleteToets(key)

    def puntenDetect(self, item, key):
        item.removePunt(key)

    def puntenlijstleerkrachtdetect(self, item, key):
        item.deleteNamecodes(key)
        if len(item.getNameCodes()) == 0:
            self.deletePuntenlijst(item.getID())

    def puntenlijstVakDelete(self, item, key):
        if item.getVakcode() == key:
            self.deletePuntenlijst(item.getID())
            self.puntenlijst.traverse(self.puntenlijstVakDelete, key)

    def puntenlijstKlasdelete(self, item, key):
        if item.getKlas() == key:
            self.deletePuntenlijst(item.getID())
            self.puntenlijst.traverse(self.puntenlijstKlasdelete, key)

    def leerlingKlasdelete(self, item, key):
        if item.getKlas() == key:
            self.deleteLeerling(item.getNummer())
            self.leerlingen.traverse(self.leerlingKlasdelete, key)

    def rapportKlasdetect(self, item, key):
        for i in range(len(item.list)-1, -1, -1):
            if item.list[i].getKlas() == key:
                del item.list[i]
                i -= 1

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

    def retrievePunt(self, key):
        # Vraag een specifiek punt op
        return self.punten.retrieve(key)

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

    def retrieveKlas(self, naam):   #waarom 2 keer retrieveKlas??
        return naam

    def retrieveVak(self, afkorting):
        return self.vakken.retrieve(afkorting)

    def buildGradeOverview(self):

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

    # def printPunt(self):    #todo moet dit want want een dot file maken van 1 waarde is toch nutteloos?
    #     return self.punten.Print()

    def buildRapport(self, samengestelde_zoeksleutel, klas):  # Bv. voor "M2"
        # TODO: fix nested for loops
        punten_per_leerling = []  # structuur: [[jan, [wiskunde, 7, 3, 5]]] # 7u, 3/5
        rapport = self.rapporten.retrieve(samengestelde_zoeksleutel)[1]
        for puntenlijst in rapport.getList():
            leerkrachten = puntenlijst.namecodes
            klas = puntenlijst.klas
            if klas != klas:
                continue
            aantal_uren = puntenlijst.uren
            vak = puntenlijst.vakcode
            for toets in puntenlijst.getToetsen():
                max = toets.maximum
                punten = toets.verzamelingVanPunten
                for punt in punten:
                    leerlingnr = punt.stamboomnummer
                    score = punt.waarde
                    leerlingFound = False
                    for leerling in punten_per_leerling:
                        if leerling[0] == leerlingnr:
                            leerlingFound = True
                            vakFound = False
                            for i in range(1, len(leerling)):  # De naam + uren dus niet meegerekend
                                if leerling[i][0] == vak:
                                    vakFound = True
                                    leerling[i][3] += int(score)
                                    leerling[i][4] += int(max)
                                    break
                            if not vakFound:
                                leerling.append([vak, aantal_uren, leerkrachten, int(score), int(max)])
                            break
                    if not leerlingFound:
                        punten_per_leerling.append([leerlingnr, [vak, aantal_uren, leerkrachten, int(score), int(max)]])

        rapportFile = HtmlMaker.HtmlRapport(str("rapport-" + str(samengestelde_zoeksleutel) + "-" + str(klas) + ".html"))
        for leerling in punten_per_leerling:
            gegevens_leerling = self.leerlingen.retrieve(leerling[0])[1]
            klas = gegevens_leerling.getKlas()
            voornaam = gegevens_leerling.getVoornaam()
            naam = gegevens_leerling.getNaam()
            rapportFile.addStructure(HtmlMaker.HtmlTitle("Rapport " + klas + " - " + voornaam + " " + naam))
            resultaten = [["vak", "uren", "leraar", "totaal"]]
            for i in range(1, len(leerling)): #  Overloop alle vakken, skip het studentennr vd leerling
                huidig_vak = leerling[i]
                naam_vak = self.vakken.retrieve(huidig_vak[0])[1]
                uren_vak = huidig_vak[1]
                leraren = ""
                j = 0
                for leraar in huidig_vak[2]:
                    j += 1
                    gegevens_leeraar = self.leraars.retrieve(leraar)[1]
                    leraren += gegevens_leeraar.getNaam() + " " + gegevens_leeraar.getAchternaam()
                    if j != len(huidig_vak[2]):
                        leraren += ", "
                totaal = 100*huidig_vak[3]/huidig_vak[4]
                resultaten.append([naam_vak, uren_vak, leraren, totaal])

            totaal_aantal_uren = 0
            totaal_punten = 0
            for i in range(1, len(resultaten)):
                totaal_aantal_uren += int(resultaten[i][1])
                totaal_punten += int(resultaten[i][3])*int(resultaten[i][1])
                resultaten[i][3] = str(round(int(resultaten[i][3]))) + "%"
            totaal = totaal_punten/totaal_aantal_uren
            totaal = str(round(totaal)) + "%"
            resultaten.append(["Totaal", "", "", totaal])
            rapportFile.addStructure(HtmlMaker.HtmlTable(resultaten))
        rapportFile.buildfile()

    def printToets(self):
        return self.toetsen.Print()

    def printKlas(self):
        return self.klassen.Print()

    def printPuntenlijst(self):
        return self.puntenlijst.Print()

    def printLeerling(self):
        return self.leerlingen.Print()

    def printLeeraar(self):
        return self.leraars.Print()

    def printVak(self):
        return self.vakken.Print()

    def undo(self):
        vorige_instructie = self.instructies.retrieve()
        print("Undo: " + vorige_instructie)
        words = vorige_instructie.split(' ')

        if words[0] == "init":
            print("Instruction \"init\" can't be undone")

        elif words[0] == "vak":
            self.deleteVak(words[1])

        elif words[0] == "klas":
            self.deleteKlas(words[1])

        elif words[0] == "leraar":
            self.deleteLeraar(words[3])

        elif words[0] == "leerling":
            self.deleteLeerling(words[5])

        elif len(words) > 1 and words[1] == "puntenlijst":
            self.deletePuntenlijst(words[0])

        elif words[0] == "start":
            print("Instruction \"start\" can't be undone")

        elif words[0] == "toets":
            self.deleteToets(words[2])

        elif words[0] == "punt":
            self.deletePunt(words[5])

        elif words[0] == "undo":
            print("Instruction \"undo\" can't be undone")

        elif words[0] == "rapport":
            print("Instruction \"rapport\" can't be undone")

        self.instructies.delete()



