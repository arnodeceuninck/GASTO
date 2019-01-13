import System
import sys

def actiefSysteem(geheel):
    if geheel == None:
        print("Gelieve eerst een systeem te activeren met init")
        return False
    else:
        return True

def readFile(filename, geheel):
    instructionFile = open(filename)  # Default is read only
    for line in instructionFile:
        geheel = readLine(line, geheel)
    return geheel


def readLine(line, geheel):
    if len(line) < 1:
        return geheel

    # skip alle regels die beginnen met een '#'
    if line[0] == '#':
        return geheel

    if line[len(line) - 1] == '\n':
        line = line[:len(line) - 1]

    words = line.split(' ')

    if len(words) < 1:
        return geheel

    elif words[0] == "init":
        geheel = System.System()

    elif words[0] == "vak":
        if not actiefSysteem(geheel):
            return geheel
        if len(words) < 3:
            print("Geen 2 parameters gevonden: vak AFK Naam")
            print(line)
            return geheel
        geheel.addVak(words[1], words[2])

    elif words[0] == "klas":
        if not actiefSysteem(geheel):
            return geheel
        if len(words) < 2:
            print("Geen 1 parameters gevonden: klas 1RICH")
            print(line)
            return geheel
        geheel.addKlas(words[1])

    elif words[0] == "leraar":
        if not actiefSysteem(geheel):
            return geheel
        if len(words) < 4:
            print("Geen 3 parameters gevonden: leraar Voornaam Naam AFKOR")
            print(line)
            return geheel
        geheel.addLeraar(words[3], words[1], words[2])

    elif words[0] == "leerling":
        if not actiefSysteem(geheel):
            return geheel
        if len(words) < 6:
            print("Geen 5 parameters gevonden: leerling Voornaam Naam 1KLAS nr studentennr")
            print(line)
            return geheel
        geheel.addLeerling(words[2], words[1], words[3], words[4], words[5])

    elif len(words) > 1 and words[1] == "puntenlijst":
        if not actiefSysteem(geheel):
            return geheel
        if len(words) < 7:
            print("Geen 6 parameters gevonden: id puntenlijst type periode leerkrachten vak uren")
            print(line)
            return geheel
        geheel.addPuntenLijst(words[0], words[2], words[3], words[4], words[5], words[6], words[7])

    elif words[0] == "start":
        if not actiefSysteem(geheel):
            return geheel
        # wat zou er hierbij zelfs moeten gebeuren?

    elif words[0] == "toets":
        if not actiefSysteem(geheel):
            return geheel
        if len(words) < 4:
            print("Geen 3 parameters gevonden: toets idpuntenlijst naam max")
            return geheel
        geheel.addToets(words[1], words[2], words[3])

    elif words[0] == "punt":
        if not actiefSysteem(geheel):
            return geheel
        if len(words) < 5:
            print("Geen 4 parameters gevonden: punt AFKOR naamtoets studentennr waarde")
            return geheel
        geheel.addPunt(words[3], words[2], words[4], words[1])

    elif words[0] == "undo":
        if not actiefSysteem(geheel):
            return geheel
        if len(words) == 1:
            geheel.undo()  # Done: implement undo
        else:
            geheel.undo(words[1])

    elif words[0] == "redo":
        if not actiefSysteem(geheel):
            return geheel
        geheel.redo()

    elif words[0] == "rapport":
        if not actiefSysteem(geheel):
            return geheel
        if len(words) < 3:
            print("Geen 2 parameters gevonden: rapport TP 1KLAS")
            return geheel
        geheel.buildRapport("M1", "6WEWI")

    elif words[0] == "ADT":
        if words[1] == "punten":
            geheel.puntdatatypechange(words[2])
        if words[1] == "leraar":
            geheel.leraardatatypechange(words[2])
        if words[1] == "vakken":
            geheel.vakkendatatypechange(words[2])
        if words[1] == "ADTpuntenlijst":
            geheel.puntenlijstdatatypechange(words[2])
        if words[1] == "leerlingen":
            geheel.leerlingdatatypechange(words[2])
        if words[1] == "rapport":
            geheel.rapportdatatypechange(words[2])
        if words[1] == "klassen":
            geheel.klassendatatypechange(words[2])
        if words[1] == "toetsen":
            geheel.toetsendatatypechange(words[2])


    else:
        pass

    return geheel

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: adts.py <inputfile>')
    else:
        print('Running ADT operations given in file ', sys.argv[1])

    filename = sys.argv[1]

    # filename = "system.txt"  # Done: verwijder deze regel, zodat de meegegeven argumenten worden gebruikt
    readFile(filename, None)

