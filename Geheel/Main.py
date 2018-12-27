# Bestand voor Command Line Interface

from System import *

geheel = system()

# init
geheel.addVak("WIS", "Wiskunde")
geheel.addVak("NED", "Nederlands")

geheel.addKlas("6WEWI")

geheel.addLeraar("HOFKT", "Tom", "Hofkens")
geheel.addLeraar("PAUWS", "Stephen", "Pauwels")
geheel.addLeraar("LAENE", "Els", "Laenens")

geheel.addLeerling("Doe", "Jane", "6WEWI", "1", "1800001")
geheel.addLeerling("Doe", "John", "6WEWI", "2", "1800002")

geheel.addPuntenLijst("1", "M", "1", "HOFKT,PAUWS", "WIS", "6WEWI", "7")
geheel.addPuntenLijst("2", "M", "1", "LAENE", "NED", "6WEWI", "4")

# start
geheel.addToets("1", "afgeleiden", "10")
geheel.addToets("1", "integralen", "20")

geheel.addToets("2", "opstel", "5")

geheel.addPunt("1800001", "afgeleiden", "5", "HOFKT")
geheel.addPunt("1800002", "afgeleiden", "9", "HOFKT")
geheel.addPunt("1800001", "integralen", "15", "PAUWS")
geheel.addPunt("1800002", "integralen", "19", "PAUWS")
geheel.addPunt("1800001", "opstel", "5", "LAENE")
geheel.addPunt("1800002", "opstel", "2", "LAENE")

geheel.buildRapport("M1", "6WEWI")

# #### Starting #### #

print("\nWelkom!")

while True:

    input_str = input("\n(1) Info Opvragen, (2) Data toevoegen, (3) Data verwijderen, (e) Exit" + '\n')

    if input_str == "e":
        break  # Verlaat de While loop -> exit het programma

    if input_str == "1":
        print("Waar wil je info over opvragen?")
        input_str = input(
            "(1) Vak, "
            "(2) Klas, "
            "(3) leraar, "
            "(4) leerling, "
            "(5) Puntenlijst, "
            "(6) Toets, "
            "(7) Punt, "
            "(8) Rapport maken,"
            "(9) Vorige instructies,"
            "(c) Cancel" + '\n')

        # TODO: checken of dotfile gegenereerd wordt
        if input_str == "1":
            geheel.printVak()
            print(str(geheel.retrieveVak(input("Afkorting: "))))
        elif input_str == "2":
            geheel.printKlas()
            print(str(geheel.retrieveKlas(input("ID: "))))
        elif input_str == "3":
            geheel.printLeraar()
            print(str(geheel.retrieveLeeraar(input("Afkorting: "))))
        elif input_str == "4":
            geheel.printLeerling()
            print(str(geheel.retrieveLeerling(input("ID: "))))
        elif input_str == "5":
            geheel.printPuntenlijst()
            print(str(geheel.retrievePuntenlijst(input("ID: "))))
        elif input_str == "6":
            geheel.printToets()
            print(str(geheel.retrieveToets(input("Naam: "))))
        elif input_str == "7":
            print(str(geheel.retrievePunt(input("ID: "))))
        elif input_str == "8":
            geheel.buildRapport(input("Samengestelde zoeksleutel TP: "), input("Klas: "))
            print("Done. Je kan het rapport terugvinden tussen je bestanden.")
        elif input_str == "9":
            geheel.printInstructies()
        elif input_str == "c":
            continue  # Ga terug naar het begin van de While-loop

    elif input_str == "2":

        print("Wat wil je gaan toevoegen?")
        input_str = input("(1) Vak, "
                          "(2) Klas, "
                          "(3) leraar, "
                          "(4) leerling, "
                          "(5) Puntenlijst, "
                          "(6) Toets, "
                          "(7) Punt, "
                          "(c) Cancel" + '\n')

        if input_str == "1":
            geheel.addVak(input("Afkorting: "),
                          input("Vak: "))
        elif input_str == "2":
            geheel.addKlas(input("Naam: "))
        elif input_str == "3":
            geheel.addLeraar(input("Afkorting: "),
                             input("Voornaam: "),
                             input("Achternaam: "))
        elif input_str == "4":
            geheel.addLeerling(input("Naam: "),
                               input("Voornaam: "),
                               input("Klas: "),
                               input("Klasnummer: "),
                               input("Studentennummer: "))
        elif input_str == "5":
            geheel.addPuntenLijst(input("ID: "),
                                  input("Type(M/E): "),
                                  input("Periode: "),
                                  input("Afkorting leerkracht (komma's tussen, zonder spaties): "),
                                  input("Afkorting vak:"),
                                  input("Klas: "),
                                  input("Uren: "))
        elif input_str == "6":
            geheel.addToets(input("Puntenlijst waar de toets in moet komen: "),
                            input("Naam toets: "),
                            input("Max. Score: "))
        elif input_str == "7":
            geheel.addPunt(input("Stamboomnummer: "),
                           input("Naam: "),
                           input("Waarde: "),
                           input("Afkorting leerkracht: "))
        elif input_str == "c":
            continue  # Ga terug naar het begin van de While-loop

    elif input_str == "3":
        print("Wat wil je gaan verwijderen?")
        input_str = input(
            "(1) Vak, "
            "(2) Klas, "
            "(3) leraar, "
            "(4) leerling, "
            "(5) Puntenlijst, "
            "(6) Toets, "
            "(7) Punt, "
            "(z) Undo, "
            "(c) Cancel" + '\n')

        if input_str == "1":
            geheel.deleteVak(input("Afkorting: "))
        elif input_str == "2":
            geheel.deleteKlas(input("Naam: "))
        elif input_str == "3":
            geheel.deleteLeraar(input("Afkorting: "))
        elif input_str == "4":
            geheel.deleteLeerling(input("Stamboomnummer: "))
        elif input_str == "5":
            geheel.deletePuntenlijst(input("ID: "))
        elif input_str == "6":
            geheel.deleteToets(input("Naam toets: "))
        elif input_str == "7":
            geheel.deletePunt(input("ID: "))
        elif input_str == "z":
            geheel.undo()
        elif input_str == "c":
            continue  # Ga terug naar het begin van de While-loop
        pass

