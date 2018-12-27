# Bestand voor Command Line Interface

from System import *
from ReadFile import *


geheel = readFile("system.txt", None)

# #### Starting #### #

print("\nWelkom!")

while True:

    input_str = input("\n(1) Info Opvragen, (2) Data toevoegen, (3) Data verwijderen, (4) Save, (e) Exit" + '\n')

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

        if input_str == "1":
            geheel.printVak()
            print(str(geheel.retrieveVak(input("Afkorting: "))[1]))
        elif input_str == "2":
            geheel.printKlas()
            print(str(geheel.retrieveKlas(input("ID: "))[1]))
        elif input_str == "3":
            geheel.printLeraar()
            print(str(geheel.retrieveLeeraar(input("Afkorting: "))[1]))
        elif input_str == "4":
            geheel.printLeerling()
            print(str(geheel.retrieveLeerling(input("ID: "))[1]))
        elif input_str == "5":
            geheel.printPuntenlijst()
            print(str(geheel.retrievePuntenlijst(input("ID: "))[1]))
        elif input_str == "6":
            geheel.printToets()
            print(str(geheel.retrieveToets(input("Naam: "))[1]))
        elif input_str == "7":
            geheel.printPunt()
            print(str(geheel.retrievePunt(input("ID: "))[1]))
        elif input_str == "8":
            geheel.buildRapport(input("Samengestelde zoeksleutel TP: "), input("Klas: "))
            print("Done. Je kan het rapport terugvinden tussen je bestanden.")
        elif input_str == "9":
            leerkr = input("Leerkracht (leave empty for all instr.): ")
            if leerkr == "":
                geheel.printInstructies()
            else:
                geheel.printInstructies(leerkr)
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

    elif input_str == "4":
        geheel.save("system.txt")

