# Bestand voor Command Line Interface

from System import *


geheel = system()
print("Welkom!")
while True:
    temp = input("(1) punt toevoegen, (2) delete, (3) toets toevoegen, (e)" + '\n')
    if temp == "e":
        break
    if temp == "1":
        geheel.addPunt()
    elif temp == "2":
        geheel.deletePunt()
    elif temp == "3":
        geheel.addToets()
