from RBT import *
from heap import *
import sys

if len(sys.argv) != 2:
    print('Usage: adts.py <inputfile>')
else:
    print('Running ADT operations given in file ', sys.argv[1])

filename = sys.argv[1]
instructionFile = open(filename) # Default is read only

functions = {"create": 0, "insert": 1, "remove": 2, "print": 3}

instructions = dict()

# TODO: fix doorgeven van methods
instructions["rbt"] = [RoodZwartBoom(), RoodZwartBoom.insert, RoodZwartBoom.remove, RoodZwartBoom.visualize]
dataStructuresWithoutRemoveParameter = ["heap"]
instructions["heap"] = [Heap()]
dataStructure = RoodZwartBoom() # Default data structure
dataStructure = None

for line in instructionFile:
    # skip alle regels die beginnen met een '#'
    if line[0] == '#':
        continue

    words = line.split(' ')
    i = 0
    for word in words:
        if word[len(word)-1] == '\n':
            word = word[:len(word)-1]
            words[i] = word
        i += 1

    if line[0:4] == "type":
        structureName = line[5:len(line)-1]
        dataStructure = instructions[structureName][functions["create"]]

    if words[0] == "insert":
        dataStructure.insert(KeyValueItem(words[1], words[1]))
        dataStructure.visualize() #TODO: comment

    if words[0] == "remove":
        if structureName in dataStructuresWithoutRemoveParameter:
            dataStructure.remove()
        else:
            dataStructure.remove(words[1][0:len(words[0])-1])  # Remove the '\n'
        dataStructure.visualize()
