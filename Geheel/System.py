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
from ReadFile import *

class System:
    def __init__(self):
        #  Deze klassen zijn dus een verzameling van als ik het goed begrijp
        self.punten = TabelWrapper("234")  # dit is de create # puntenlijst nog nodig om punten aan te passen
        self.puntenQueue = TabelWrapper("queue")
        self.toetsen = TabelWrapper("cl")
        self.puntenlijst = TabelWrapper("bst")
        self.vakken = TabelWrapper("ll")  # Key = afkorting, Value = volledige naam
        self.klassen = TabelWrapper("ll")
        self.leraars = TabelWrapper("234")
        self.leerlingen = TabelWrapper("ll")
        self.rapporten = TabelWrapper("234")
        self.instructies = TabelWrapper("stack")  # NOTE: Don't change this ADT
        self.undoPuntStack = TabelWrapper("ll")  # Dit bevat als zoeksleutel een leerkracht, als value een stack
        self.instructies.insert("init")
        self.redoStack = TabelWrapper("stack")

    def addVak(self, afkorting, naam):
        return_messages = []
        if not isinstance(afkorting, str) or not isinstance(naam, str):
            return_messages.append("ERROR: naam en afkorting moeten een string zijn.")
            print(return_messages[0])
            return return_messages

        for vak in self.vakken:
            if vak[0] == afkorting:
                return_messages.append("ERROR: Er is al een vak met deze afkorting.")
        self.instructies.insert("vak " + str(afkorting) + " " + str(naam))
        self.vakken.insert(naam, afkorting)
        return return_messages

    def addKlas(self, naam):
        if not isinstance(naam, str):
            return ["ERROR: De naam van een klas moet een string zijn."]
        for klas in self.klassen:
            if klas[0] == naam:
                return ["ERROR: Er is al een klas met deze naam."]

        self.instructies.insert("klas " + str(naam))
        self.klassen.insert(naam)
        return []

    def addLeraar(self, afkorting, naam, achternaam):
        if not isinstance(afkorting, str) or not isinstance(naam, str) or not isinstance(achternaam, str):
            error = "ERROR: De naam, achternaam en afkorting van een leerkracht moeten een string zijn."
            print(error)
            return [error]

        for leraar in self.leraars:
            if leraar[0] == leraar:
                return ["ERROR: Er bestaat al een leerkracht met deze afkorting"]
        self.instructies.insert("leraar " + str(naam) + " " + str(achternaam) + " " + str(afkorting))
        self.leraars.insert(Leraar.Leraar(afkorting, naam, achternaam), afkorting)
        self.undoPuntStack.insert(TabelWrapper("stack"), afkorting)
        return []

    def addLeerling(self, naam, voornaam, klas, klasnummer, studentennummer):
        return_messages = []
        if not isinstance(naam, str) or not isinstance(voornaam, str) or not isinstance(klas, str) or \
            not isinstance(klasnummer, (str, int)) or not isinstance(studentennummer, (str, int)):
            return_messages.append("Incorrect data types")
            print(return_messages[0])
            return return_messages

        self.instructies.insert("leerling " + str(voornaam) + " " + str(naam) + " " + str(klas) + " " +
                                str(klasnummer) + " " + str(studentennummer))
        if self.leerlingen.retrieve(studentennummer)[0] is not False:
            return_messages.append("Het gegeven studenten nummer is al in gebruik")
            print(return_messages[0])
            return return_messages
        # Kijk of de klas al is aangemaakt
        if self.klassen.retrieve(klas) is None:
            return_messages.append("ERROR: De klas waar je de leerling wil insteken (" + klas + "), bestaat nog niet. "
                                                                               "Gelieve deze eerst aan te maken.")
            print(return_messages[0])
            return return_messages

        for student in self.leerlingen:
            if student[1].getKlas() == klas and student[1].getKlasNummer == klasnummer:
                return_messages.append("ERROR: Er zit al een leerling met hetzelfde klasnummer in de klas.")
                print(return_messages[0])
                return return_messages

        self.leerlingen.insert(Leerling.Leerling(naam, voornaam, klas, klasnummer, studentennummer),
                                      studentennummer)
        return []

    def PermissionCheckLeerkracht(self, naam_toets, leerkracht):
        test = self.toetsen.retrieve(naam_toets)[1]
        if test.puntenlijst[0] is False:
            return False
        else:
            aantal_punten = len(test.puntenlijst[1].namecodes)
            for i in range(aantal_punten):
                if test.puntenlijst[1].namecodes[i] == leerkracht:
                    return True
            return False

    def puntMetIDExists(self, ID):
        for punt in self.punten:
            if punt[0] == ID:
                return True
        else:
            return False

    def addPunt(self, stamboeknummer_leerling, naam_toets, Waarde, leerkracht):
        return_messages = []
        if not isinstance(stamboeknummer_leerling, str) or not isinstance(naam_toets, str) or \
            not isinstance(Waarde, (str, int, float)) or not isinstance(leerkracht, str):
            return_messages.append("Incorrect data types")
            print(return_messages[0])
            return return_messages

        try:
            float(Waarde)
        except:
            return_messages.append("Waarde is not a number")
            print(return_messages[0])
            return return_messages

        ID = 0
        while self.puntMetIDExists(ID):
            ID += 1

        instructie = "punt " + str(leerkracht) + " " + str(naam_toets) + " " + \
                     str(stamboeknummer_leerling) + " " + str(Waarde) + " " + str(ID)
        self.instructies.insert(instructie)
        stack_leerkr = self.undoPuntStack.retrieve(leerkracht)[1]
        stack_leerkr.insert(instructie)

        # maakt een nieuw punt aan met een uniek ID, Stamboomnummer, Naam, Waarde en Timestamp
        toets = self.toetsen.retrieve(naam_toets)[1]
        if toets is None:
            return_messages.append("ERROR: De toets " + naam_toets + " werd niet teruggevonden in het systeem. "
                                                    "Gelieve deze eerst aan te maken.")
            print(return_messages[0])
            return return_messages
        if self.leerlingen.retrieve(stamboeknummer_leerling)[1] is None:
            return_messages.append("ERROR: Het studentennummer " + stamboeknummer_leerling + " werd niet teruggevonden in het systeem. "
                                                                            "Gelieve deze eerst aan te maken.")
            print(return_messages[0])
            return False
        if self.PermissionCheckLeerkracht(naam_toets, leerkracht) is False:
            return_messages.append("ERROR: De leerkracht: " + leerkracht + " Heeft geen toesteming om dit punt toe te voegen")
            print(return_messages[0])
            return return_messages

        punt = Punt.createPunt(ID, stamboeknummer_leerling, naam_toets, Waarde,
                               datetime.datetime.now())  # https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python
        self.puntenQueue.insert(punt)
        while not self.puntenQueue.isEmpty():
            current_punt = self.puntenQueue.retrieve()[1]
            stamboeknummer_leerling = current_punt.getStamboekNummer()
            naam_toets = current_punt.getNaam()
            for punt2 in self.punten:
                punt2 = punt2[1]
                if punt2.getStamboekNummer() == stamboeknummer_leerling and punt2.getNaam() == naam_toets:
                    return_messages.append("Error bij punt: " + str(punt) +
                                           "Punt voor deze leerling en toets al in puntenlijst. "
                                           "Gelieve het vorige punt eerst te verwijderen ")
                    print(return_messages[0])
                    return return_messages
            # Controleer of er al een punt voor deze toets en deze leerkracht in de lijst met punten zit
            self.punten.insert(current_punt, ID)  # Key
            self.puntenQueue.delete()  # Verwwijder het eerste element van de queue
        # DONE: de retrieve van een LL geeft een tuple terug ma is da echt nodig?
        # JHAAAA, alle retrieves returnen een tuple

        toets.addPunt(punt)
        return return_messages

    def addPuntenLijst(self, ID, type, periode, namecodes, vak_afkorting, klas, uren):
        return_messages = []
        self.instructies.insert(str(ID) + " puntenlijst " + str(type) + " " + str(periode) + " " +
                                str(namecodes) + " " + str(vak_afkorting) + " " + str(klas) + " " + str(uren))
        if self.klassen.retrieve(klas) is None:
            return_messages.append("ERROR: De klas waaraan je wil dat de leeraar les geeft (" + klas + "), bestaat nog niet. "
                  "Gelieve deze eerst aan te maken.")
            print(return_messages[0])
            return return_messages

        leraren = namecodes.split(',')
        for leraar in leraren:
            if self.leraars.retrieve(leraar) is None:
                return_messages.append("ERROR: De leraar " + leraar + " werd niet teruggevonden in het systeem. "
                      "Gelieve deze eerst aan te maken")
                print(return_messages[0])
                return return_messages

        for puntenlijst in self.puntenlijst:
            if puntenlijst[1].getID() == ID:
                return_messages.append("ERROR: ID is reeds gebruikt.")
                print(return_messages[0])
                return return_messages

        if self.retrieveVak(vak_afkorting)[0] == False:
            return_messages.append("Het vak werd niet teruggevonden. "
                                   "Gelieve aan een admin te vragen om dit aan te maken.")
            return return_messages

            print(return_messages[0])
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
        return return_messages

    def addToets(self, puntenlijst_id, titel, maxscore):
        return_messages = []
        self.instructies.insert("toets " + str(puntenlijst_id) + " " + str(titel) + " " + str(maxscore))
        puntenlijst = self.puntenlijst.retrieve(puntenlijst_id)
        if puntenlijst[1] is None:
            return_messages.append("ERROR: De puntenlijst met id " + puntenlijst_id + " werd niet teruggevonden in het systeem. "
                                                 "Gelieve deze eerst aan te maken")
            print(return_messages[0])
            return return_messages

        for toets in puntenlijst[1].getToetsen():
            if toets.getNaam() == titel:
                return_messages.append("ERROR: Er bestaat al een toets met dezelfde titel.")
                print(return_messages[0])
                return return_messages

        toets = Toets.createToets(puntenlijst, titel, maxscore, [])
        self.toetsen.insert(toets, titel)
        if type(puntenlijst) == tuple:
            puntenlijst[1].addToets(toets)
        else:
            puntenlijst.addToets(toets)
        return return_messages

    def deletePunt(self, ID):
        # verwijdert een eerder aangemaakt punt
        self.toetsen.traverse(self.puntenDetect, ID)
        self.punten.delete(int(ID))
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
        # de punten die gelinkt zijn aan het stamboom nummer verwijderen
        self.punten.traverse(self.collector, key)
        self.leerlingen.delete(key)

    def deletePuntenlijst(self, key):
        puntenlijst = self.puntenlijst.retrieve(key)
        for i in range(len(puntenlijst[1].toetsen) - 1, -1, -1):
            self.deleteToets(puntenlijst[1].toetsen[i].getNaam())
        self.puntenlijst.delete(key)

    def deleteToets(self, naam):
        #probleem opgelost
        self.puntenlijst.traverse(self.puntenlijstToetsenDetect, naam)
        self.toetsen.delete(naam)

    def deleteLeraar(self, naam):
        self.puntenlijst.traverse(self.puntenlijstleerkrachtdetect, naam)
        #TODO: (note to self) temp fix
        self.puntenlijst.traverse(self.puntenlijstleerkrachtdetect, naam)
        self.leraars.delete(naam)

    def removeAllPunten(self):
        # Verwijdert alle punten in het systeem (in theorie nooit nodig)
        self.punten.destroy()

    def collector(self, item, key):
        if item is not None and item.getStamboekNummer() == key:
            self.deletePunt(item.getID())
            self.punten.traverse(self.collector, key)
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
        for i in range(len(item.list) - 1, -1, -1):
            if item.list[i].getKlas() == key:
                del item.list[i]
                i -= 1

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

    # def retrieveKlas(self, naam):   #waarom 2 keer retrieveKlas??
    #     return naam

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

    def buildRapport(self, samengestelde_zoeksleutel, klas, student=None, buildHTML=True):  # Bv. voor "M2"
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
                                leerling.append([vak, aantal_uren, leerkrachten, float(score), int(max)])
                            break
                    if not leerlingFound:
                        punten_per_leerling.append([leerlingnr, [vak, aantal_uren, leerkrachten, float(score), int(max)]])

        rapportFile = HtmlMaker.HtmlRapport(
            str("rapport-" + str(samengestelde_zoeksleutel) + "-" + str(klas) + ".html"))
        for leerling in punten_per_leerling:
            if student==None or leerling[0]==student:
                studentennr = leerling[0]
                gegevens_leerling = self.leerlingen.retrieve(studentennr)
                gegevens_leerling = gegevens_leerling[1]
                klas = gegevens_leerling.getKlas()
                voornaam = gegevens_leerling.getVoornaam()
                naam = gegevens_leerling.getNaam()
                rapportFile.addStructure(HtmlMaker.HtmlTitle("Rapport " + klas + " - " + voornaam + " " + naam))
                resultaten = [["vak", "uren", "leraar", "totaal"]]
                for i in range(1, len(leerling)):  # Overloop alle vakken, skip het studentennr vd leerling
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
                    totaal = 100 * huidig_vak[3] / huidig_vak[4]
                    resultaten.append([naam_vak, uren_vak, leraren, totaal])

                totaal_aantal_uren = 0
                totaal_punten = 0
                for i in range(1, len(resultaten)):
                    totaal_aantal_uren += int(resultaten[i][1])
                    totaal_punten += int(resultaten[i][3]) * int(resultaten[i][1])
                    resultaten[i][3] = str(round(int(resultaten[i][3]))) + "%"
                totaal = totaal_punten / totaal_aantal_uren
                totaal = str(round(totaal)) + "%"
                resultaten.append(["Totaal", "", "", totaal])
                if not buildHTML:
                    return resultaten
                rapportFile.addStructure(HtmlMaker.HtmlTable(resultaten))
        return rapportFile.buildfile()

    def printPunt(self):
        return self.punten.Print()

    def printToets(self):
        return self.toetsen.Print()

    def printKlas(self):
        return self.klassen.Print()

    def printPuntenlijst(self):
        return self.puntenlijst.Print()

    def printLeerling(self):
        return self.leerlingen.Print()

    def printLeraar(self):
        return self.leraars.Print()

    def printVak(self):
        return self.vakken.Print()

    def printRapport(self):
        return self.rapporten.Print()

    def printUndo(self):
        return self.undoPuntStack.Print()

    def printRedo(self):
        return self.redoStack.Print()

    def printQueue(self):
        return self.puntenQueue.Print()

    def printInstructies(self, teacher=None):
        if teacher != None:
            return self.undoPuntStack.retrieve(teacher)[1].Print()
        return self.instructies.Print()

    def redo(self):
        if self.redoStack.isEmpty():
            return ["Nothing to redo."]
        instructie = self.redoStack.retrieve()
        print("Redo: " + instructie)
        self = readLine(instructie, self)
        self.redoStack.delete()
        return ["Done: Redo " + instructie]

    def undo(self, leerkr=None):
        if leerkr != None:
            leerkr_stack = self.undoPuntStack.retrieve(leerkr)[1]
            vorige_instructie = leerkr_stack.retrieve()
        else:
            vorige_instructie = self.instructies.retrieve()
        self.redoStack.insert(vorige_instructie)
        print("Undo: " + vorige_instructie)
        words = vorige_instructie.split(' ')

        if words[0] == "init":
            error = "Instruction \"init\" can't be undone"
            print(error)
            return [error]

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
            error = "Instruction \"start\" can't be undone"
            print(error)
            return [error]

        elif words[0] == "toets":
            self.deleteToets(words[2])

        elif words[0] == "punt":
            self.deletePunt(words[5])

        elif words[0] == "undo":
            self.redo()

        elif words[0] == "rapport":
            error = "Instruction \"rapport\" can't be undone"
            print(error)
            return [error]

        if leerkr == None:
            self.instructies.delete()
        else:
            self.leerkr_stack.delete()

        return ["Done: Undo " + vorige_instructie]

    def save(self, filename):
        filestring = ""
        for instuction in self.instructies:
            filestring = str(instuction) + "\n" + filestring
        file = open(filename, 'w+')
        file.write(filestring)
        file.close()


    # Functies aangemaakt voor GUI
    def isLeerkracht(self, naam):
        for leerkracht in self.leraars:
            searchkey = leerkracht[0] # De afkorting van de leerkracht
            if searchkey == naam:
                return True
        return False

    def isLeerling(self, naam):
        for leerling in self.leerlingen:
            if leerling[0] == naam:
                return True
        return False

    def lijstLeerkrachtenToStr(self, leerkrachten):
        string = ""
        i = 0
        for afkorting in leerkrachten:
            leerkracht = self.retrieveLeeraar(afkorting)[1]
            string += leerkracht.getNaam() + " " + leerkracht.getAchternaam()
            i+=1
            if i < len(leerkrachten):
                string += ", "
        return string

    def permissionCheckPuntenlijst(self, afkorting, puntenlijst):
        for leraar in puntenlijst.getNameCodes():
            if leraar == afkorting:
                return True
        return False

    def puntenLijstenVanLeerkracht(self, naam):
        lijsten = []
        for puntenlijst in self.puntenlijst:
            if self.permissionCheckPuntenlijst(naam, puntenlijst[1]):
                puntenlijst = puntenlijst[1]
                lijstarray = [puntenlijst.getID(),
                              puntenlijst.getKlas(),
                              puntenlijst.getVakcode(),
                              puntenlijst.getType()+puntenlijst.getPeriode(),
                              self.lijstLeerkrachtenToStr(puntenlijst.getNameCodes()),
                              puntenlijst.getUren()]
                lijsten.append(lijstarray)
        return lijsten

    def toetsenVanPuntenlijst(self, ID):
        toetsen = []
        for toets in self.retrievePuntenlijst(ID)[1].getToetsen():
            toetsarray = [toets.getNaam(), toets.getMaximum(), toets.getGemiddelde()]
            toetsen.append(toetsarray)
        return toetsen


    def puntenVanToets(self, naam):
        punten = []
        toets = self.retrieveToets(naam)[1]
        for punt in toets.getVerzamelingVanPunten():
            stamboeknr = punt.getStamboekNummer()
            leerling = self.retrieveLeerling(stamboeknr)[1]
            naam_leerling = leerling.getVoornaam() + " " + leerling.getNaam()
            puntarray = [punt.getID(), stamboeknr, naam_leerling, punt.getWaarde(), punt.getTimestamp()]
            punten.append(puntarray)
        return punten


    def tabelVakken(self):
        tabel = []
        for vak in self.vakken:
            vakrij = [vak[0], vak[1]]
            tabel.append(vakrij)
        return tabel


    def tabelLeraars(self):
        tabel = []
        for leraar in self.leraars:
            naam = leraar[1].getNaam() + " " + leraar[1].getAchternaam()
            rij = [leraar[0], naam]
            tabel.append(rij)
        return tabel

    def tabelKlassen(self):
        tabel = []
        for klas in self.klassen:
            rij = [klas[0]]
            tabel.append(rij)
        return tabel

    def tabelLeerlingen(self):
        tabel = []
        for leerling in self.leerlingen:
            naam = leerling[1].getVoornaam() + " " + leerling[1].getNaam()
            klas = leerling[1].getKlas()
            klasnr = leerling[1].getKlasNummer()
            rij = [leerling[0], naam, klas, klasnr]
            tabel.append(rij)
        return tabel

    def datastructuresinfo(self):
        vakken = [self.vakken.type, self.vakken.getLength()]
        leraars = [self.leraars.type, self.leraars.getLength()]
        punt = [self.punten.type, self.punten.getLength()]
        puntenlijst = [self.puntenlijst.type, self.puntenlijst.getLength()]
        leerling = [self.leerlingen.type, self.leerlingen.getLength()]
        rapport = [self.rapporten.type, self.rapporten.getLength()]
        klassen = [self.klassen.type, self.klassen.getLength()]
        toetsen = [self.toetsen.type, self.toetsen.getLength()]
        undoStack = [self.undoPuntStack.type, self.undoPuntStack.getLength()]
        redoStack = [self.redoStack.type, self.redoStack.getLength()]
        instructies = [self.instructies.type, self.instructies.getLength()]
        puntenQueue = [self.puntenQueue.type, self.puntenQueue.getLength()]
        return [vakken, leraars, punt, puntenlijst, leerling, rapport, klassen, undoStack, redoStack, instructies,
                puntenQueue, toetsen]

    def puntdatatypechange(self, new):
        temp = TabelWrapper(new)
        self.punten.traverse(self.transferid, temp)
        self.punten = temp

    def leraardatatypechange(self, new):
        temp = TabelWrapper(new)
        self.leraars.traverse(self.transferafkorting, temp)
        self.leraars = temp

    def vakkendatatypechange(self, new):
        temp = TabelWrapper(new)
        for vak in self.vakken:
            temp.insert(vak[1], vak[0])
        self.vakken = temp

    def toetsendatatypechange(self, new):
        temp = TabelWrapper(new)
        self.toetsen.traverse(self.transfernaam, temp)
        self.toetsen = temp

    def puntenlijstdatatypechange(self, new):
        temp = TabelWrapper(new)
        self.puntenlijst.traverse(self.transferid, temp)
        self.puntenlijst = temp

    def leerlingdatatypechange(self, new):
        temp = TabelWrapper(new)
        self.puntenlijst.traverse(self.transferid, temp)
        self.puntenlijst = temp

    def rapportdatatypechange(self, new):
        temp = TabelWrapper(new)
        self.rapporten.traverse(self.transferzoeksleutel, temp)
        self.rapporten = temp

    def klassendatatypechange(self, new):
        temp = TabelWrapper(new)
        for klas in self.klassen:
            temp.insert(klas[0], klas[1])
        self.klassen = temp

    def transferid(self, value, newadt):
        return newadt.insert(value, value.id)

    def transferafkorting(self, value, newadt):
        return newadt.insert(value, value.afkorting)

    def transfernummer(self, value, newadt):
        return newadt.insert(value, value.naam)

    def transferzoeksleutel(self, value, newadt):
        return newadt.insert(value, value.Zoeksleutel)

    def transfernaam(self, value, newadt):
        return newadt.insert(value, value.naam)

    def rapportenMetPuntenVanLeerling(self, studentennr):
        rapporten = []
        for zoeksleutel,rapport in self.rapporten:
            for puntenlijst in rapport.getList():
                for toets in puntenlijst.getToetsen():
                    for punt in toets.getVerzamelingVanPunten():
                        if punt.getStamboekNummer() == studentennr and zoeksleutel not in rapporten:
                            rapporten.append(zoeksleutel)
        return rapporten

