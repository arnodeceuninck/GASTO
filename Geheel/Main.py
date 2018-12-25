# Bestand voor Command Line Interface

from System import *

geheel = system()

# TODO: Overal waar een ID wordt meegegeven er zelf eentje laten genereren (tabel.getLength() + 1) als ID bv
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

geheel.addPunt("1800001", "afgeleiden", "5", "HOFKT")  # TODO: Wat doet de afkorting van de leerkracht erbij in system.txt?
                                                                   #  moet dit mee opgeslaan worden?
                                                                   # TODO: Enkel leerkracht die dit vak geeft aan de kla mag punten toevoegen
                                                                   # Timestamp is momenteel: yyyymmddhhmmss
geheel.addPunt("1800002", "afgeleiden", "9", "HOFKT")  # TODO: timestamp = time.now()
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
            "(c) Cancel" + '\n')

        # TODO: Bij het opvragen ook een .dot file laten genereren van de structuur waaruit geretrieved wordt
        if input_str == "1":
            print(str(geheel.retrieveVak(input("Afkorting: "))))
        elif input_str == "2":
            print(str(geheel.retrieveKlas(input("ID: "))))
        elif input_str == "3":
            print(str(geheel.retrieveLeeraar(input("Afkorting: "))))
        elif input_str == "4":
            print(str(geheel.retrieveLeerling(input("ID: "))))
        elif input_str == "5":
            print(str(geheel.retrievePuntenlijst(input("ID: "))))
        elif input_str == "6":
            print(str(geheel.retrieveToets(input("Naam: "))))
        elif input_str == "7":
            print(str(geheel.retrievePunt(input("ID: "))))
        elif input_str == "7":
            geheel.buildRapport(input("Samengestelde zoeksleutel TP: "), input("Klas: "))
            print("Done. Je kan het rapport terugvinden tussen je bestanden.")
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
            # TODO: uitleggen wat het ID van een punt is, is dit gewoon een random gekozen getal?
            # Misschien kunnen we het ID zelf genereren en returnen, want als 'leerkracht' is het niet de bedoeling
            # dat je dit moet ingeven denk ik (bv. eerst geinserte punt heeft ID 1, daarna 2, 3, 4...)
            geheel.addPunt(input("ID: "),
                           input("Stamboomnummer: "),
                           input("Naam: "),
                           input("Waarde: "),
                           input("Timestamp: "))
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
            "(c) Cancel" + '\n')

        # TODO: support unsupported feautures
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
        elif input_str == "c":
            continue  # Ga terug naar het begin van de While-loop
        pass

