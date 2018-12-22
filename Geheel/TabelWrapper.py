from KeyValueItem import *
import Stack
# import queue
# import bst
import Dubbelgelinktelijst
import ADTcircularLinkedChain
# import 23
import _234T
import RBT
# import hashmap
import Heap

# GLOBAL VARIABLES
supportedDataStructures = ["stack", "queue", "bst", "cl", "ll", "23", "234", "rb", "hlin", "hquad", "hsep", "heap"]

createDataStructure = {"stack": Stack.createstack(),
                       "queue": None,
                       "bst": None,
                       "cl": ADTcircularLinkedChain.createList(),
                       "ll": Dubbelgelinktelijst.createLinkedChain(),
                       "23": None,
                       "234": _234T.createSearchTree(),
                       "rb": RBT.createRBT(),
                       "hlin": None,
                       "hquad": None,
                       "hsep": None,
                       "heap": Heap.createHeap()}


class TabelWrapper:
    def __init__(self, structure_type):  # structure_type is een string
        self.type = None
        self.dataStructure = None
        self.create(structure_type)

    def type_assigned(self):
        if self.type is not None:
            return True
        else:
            print("Please initialise your datastructure first with create(structure_type)")
            return False

    def create(self, structure_type):
        if structure_type not in supportedDataStructures:
            print("Datastructure " + structure_type + " is not supported")
            return False
        else:
            self.type = structure_type
            self.dataStructure = createDataStructure[structure_type]
            return self.dataStructure

    def insert(self, value, key):
        if not self.type_assigned:
            return False
        elif self.type == "stack":
            return self.dataStructure.push(Stack.Node(value))
        elif self.type == "queue":
            return self.dataStructure.insert(key)
        elif self.type == "bst":
            return self.dataStructure.insert(key)
        elif self.type == "cl":
            return self.dataStructure.insert(key, value)
        elif self.type == "ll":
            return self.dataStructure.insert(Dubbelgelinktelijst.Node(value, key))
        elif self.type == "23":
            return self.dataStructure.insert(key)
        elif self.type == "234":
            return self.dataStructure.T234Insert(_234T.TreeItem(value, key))
        elif self.type == "rb":
            return self.dataStructure.insert(KeyValueItem(key, value))
        elif self.type == "hlin" or self.type == "hquad" or self.type == "hsep":
            return self.dataStructure.insert(key)
        elif self.type == "heap":
            return self.dataStructure.insert(KeyValueItem(key, value))

    def retrieve(self, key=None):
        if not self.type_assigned:
            return False
        elif self.type == "stack":
            return self.dataStructure.getTop()
        elif self.type == "queue":
            return self.dataStructure.retrieve(key)
        elif self.type == "bst":
            return self.dataStructure.retrieve(key)
        elif self.type == "cl":
            return self.dataStructure.retrieve(key)
        elif self.type == "ll":
            return self.dataStructure.retrieve(key)
        elif self.type == "23":
            return self.dataStructure.retrieve(key)
        elif self.type == "234":
            return self.dataStructure.retrieve(key)
        elif self.type == "rb":
            return self.dataStructure.retrieve(key)
        elif self.type == "hlin" or self.type == "hquad" or self.type == "hsep":
            return self.dataStructure.retrieve(key)
        elif self.type == "heap":
            print("Retrieve is niet mogelijk bij een heap")  # Not implemented
            return False
            # return self.dataStructure.retrieve(key)

    def delete(self, key=None):
        if not self.type_assigned:
            return False
        elif self.type == "stack":
            return self.dataStructure.pop()
        elif self.type == "queue":
            return self.dataStructure.delete(key)
        elif self.type == "bst":
            return self.dataStructure.delete(key)
        elif self.type == "cl":
            return self.dataStructure.delete(key)
        elif self.type == "ll":
            return self.dataStructure.delete(key)
        elif self.type == "23":
            return self.dataStructure.delete(key)
        elif self.type == "234":
            return self.dataStructure.T234Delete(key)
        elif self.type == "rb":
            return self.dataStructure.remove(key)
        elif self.type == "hlin" or self.type == "hquad" or self.type == "hsep":
            return self.dataStructure.delete(key)
        elif self.type == "heap":
            return self.dataStructure.remove() # Altijd de top die verwijderd wordt

    def destroy(self):
        if not self.type_assigned:
            return False
        elif self.type == "stack":
            return self.dataStructure.destroyStack()
        elif self.type == "queue":
            return self.dataStructure.destroy()
        elif self.type == "bst":
            return self.dataStructure.destroy()
        elif self.type == "cl":
            return self.dataStructure.destroyList()
        elif self.type == "ll":
            return self.dataStructure.destroyList()
        elif self.type == "23":
            return self.dataStructure.destroy()
        elif self.type == "234":
            return self.dataStructure.destroySearchTree()
        elif self.type == "rb":
            return self.dataStructure.destroyRBT()
        elif self.type == "hlin" or self.type == "hquad" or self.type == "hsep":
            return self.dataStructure.destroy()
        elif self.type == "heap":
            return self.dataStructure.destroy()

    def isEmpty(self, key=None):
        if not self.type_assigned:
            return False
        elif self.type == "stack":
            return self.dataStructure.pop()
        elif self.type == "queue":
            return self.dataStructure.isEmpty(key)
        elif self.type == "bst":
            return self.dataStructure.isEmpty(key)
        elif self.type == "cl":
            return self.dataStructure.isEmpty(key)
        elif self.type == "ll":
            return self.dataStructure.isEmpty(key)
        elif self.type == "23":
            return self.dataStructure.isEmpty(key)
        elif self.type == "234":
            return self.dataStructure.isEmpty(key)
        elif self.type == "rb":
            return self.dataStructure.isEmpty(key)
        elif self.type == "hlin" or self.type == "hquad" or self.type == "hsep":
            return self.dataStructure.isEmpty(key)
        elif self.type == "heap":
            return self.dataStructure.isEmpty(key)

    def getLength(self, key=None):
        if not self.type_assigned:
            return False
        elif self.type == "stack":
            pass  # Not implemented
            return False
            # return self.dataStructure.getLength()
        elif self.type == "queue":
            return self.dataStructure.getLength(key)
        elif self.type == "bst":
            return self.dataStructure.getLength(key)
        elif self.type == "cl":
            return self.dataStructure.getLength(key)
        elif self.type == "ll":
            return self.dataStructure.getLength(key)
        elif self.type == "23":
            return self.dataStructure.getLength(key)
        elif self.type == "234":
            pass  # Not implemented
            return False
            # return self.dataStructure.getLength(key)
        elif self.type == "rb":
            pass  # Not implemented
            return False
            return self.dataStructure.getLength(key)
        elif self.type == "hlin" or self.type == "hquad" or self.type == "hsep":
            return self.dataStructure.getLength(key)
        elif self.type == "heap":
            return self.dataStructure.size()

    # Moet een wrapper traverse ook ondersteunen?


bob = Dubbelgelinktelijst.createLinkedChain()
bob.insert(Dubbelgelinktelijst.Node(70, 1))  # Value - key

bob2 = TabelWrapper("234")
bob2.insert(70, 1)  # Value - key
pass
