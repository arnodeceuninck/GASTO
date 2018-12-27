# NOTE: wordt alphabetisch gesorteerd

from TabelWrapper import *
import sys

if len(sys.argv) != 2:
    print('Usage: adts.py <inputfile>')
else:
    print('Running ADT operations given in file ', sys.argv[1])

filename = sys.argv[1]
instructionFile = open(filename)  # Default is read only

for line in instructionFile:
    # skip alle regels die beginnen met een '#'
    if line[0] == '#':
        continue

    if line[len(line) - 1] == '\n':
        line = line[:len(line) - 1]

    words = line.split(' ')
    if line[0:4] == "type":
        structureName = line[5:]
        dataStructure = TabelWrapper(structureName)

    if words[0] == "insert":
        dataStructure.insert(words[1], words[1])  # Key is number, value string

    if words[0] == "delete":
        if len(words) < 2:
            words.append(None)
        dataStructure.delete(words[1])

    if words[0] == "print":
        dataStructure.Print()


