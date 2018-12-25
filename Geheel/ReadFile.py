from System import *
import sys

# if len(sys.argv) != 2:
#     print('Usage: adts.py <inputfile>')
# else:
#     print('Running ADT operations given in file ', sys.argv[1])
#
# filename = sys.argv[1]
filename = "system.txt"  # TODO: verwijder deze regel, zodat de meegegeven argumenten worden gebruikt
instructionFile = open(filename) # Default is read only

def actiefSysteem():
    if geheel == None:
        print("Gelieve eerst een systeem te activeren met init")
        return False
    else:
        return True

for line in instructionFile:
    # skip alle regels die beginnen met een '#'
    if len(line) < 1:
        continue

    if line[0] == '#':
        continue

    words = line.split(' ')
    i = 0
    # verwijder alle enters op het einde
    for word in words:
        if word[len(word)-1] == '\n':
            word = word[:len(word)-1]
            words[i] = word
        i += 1

    if len(words) < 1:
        continue

    elif words[0] == "init":
        geheel = system()

    elif words[0] == "vak":
        if not actiefSysteem():
            continue
        if len(words) < 3:
            print("Geen 2 parameters gevonden: vak AFK Naam")
            continue
        geheel.addVak(words[1], words[2])

    elif words[0] == "vak":
        if not actiefSysteem():
            continue
        if len(words) < 3:
            print("Geen 2 parameters gevonden: vak AFK Naam")
            continue
        geheel.addVak(words[1], words[2])

    elif words[0] == "klas":
        if not actiefSysteem():
            continue
        if len(words) < 2:
            print("Geen 1 parameters gevonden: klas 1RICH")
            continue
        geheel.addKlas(words[1])

    elif words[0] == "leraar":
        if not actiefSysteem():
            continue
        if len(words) < 4:
            print("Geen 3 parameters gevonden: leraar Voornaam Naam AFKOR")
            continue
        geheel.addLeraar(words[3], words[1], words[2])

    elif words[0] == "leerling":
        if not actiefSysteem():
            continue
        if len(words) < 6:
            print("Geen 5 parameters gevonden: leerling Voornaam Naam 1KLAS nr studentennr")
            continue
        geheel.addLeerling(words[2], words[1], words[3], words[4], words[5])

    elif len(words) > 1 and words[1] == "puntenlijst":
        if not actiefSysteem():
            continue
        if len(words) < 8:
            print("Geen 5 parameters gevonden: leerling Voornaam Naam 1KLAS nr studentennr")
            continue
        geheel.addPuntenLijst(words[0], words[2], words[3], words[4], words[5], words[6], words[7])

    elif words[0] == "start":
        if not actiefSysteem():
            continue
        # TODO: wat zou er hierbij zelfs moeten gebeuren?

    elif words[0] == "toets":
        if not actiefSysteem():
            continue
        if len(words) < 4:
            print("Geen 3 parameters gevonden: toets idpuntenlijst naam max")
            continue
        geheel.addToets(words[1], words[2], words[3])

    elif words[0] == "punt":
        if not actiefSysteem():
            continue
        if len(words) < 5:
            print("Geen 4 parameters gevonden: punt AFKOR naamtoets studentennr waarde")
            continue
        geheel.addPunt(words[3], words[2], words[4], words[1])

    elif words[0] == "undo":
        if not actiefSysteem():
            continue
        # geheel.undo() # TODO: implement undo

    elif words[0] == "rapport":
        if not actiefSysteem():
            continue
        if len(words) < 3:
            print("Geen 2 parameters gevonden: rapport TP 1KLAS")
            continue
        geheel.buildRapport("M1", "6WEWI")

    else:
        pass
