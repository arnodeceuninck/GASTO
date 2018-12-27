from KeyValueItem import *
import Stack
import ADTQueue
import BinarySearchTree
import Dubbelgelinktelijst
import ADTcircularLinkedChain
import TweeDrieBoom
import T234
import RBT
import Hashmap
import Heap

# GLOBAL VARIABLES
supportedDataStructures = ["stack", "queue", "bst", "cl", "ll", "23", "234", "rb", "hlin", "hquad", "hsep", "heap"]

class TabelWrapper:
    def __init__(self, structure_type):  # structure_type is een string
        self.type = None
        self.dataStructure = None
        self.grootte = 211
        self.create(structure_type)

    # Currently datastructures supporting iterators: cl, ll, rb, heap
    # !!! Alle iterators returnen een tuple (key, value)
    # Als je niet weet hoe je dit moet implementeren, kijk dan in een van de reeds geimplementeerde
    # https://www.w3schools.com/python/python_iterators.asp
    def __iter__(self):
        self.iterator = iter(self.dataStructure)
        return self
    def __next__(self):
        return next(self.iterator)

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
            # return self.dataStructure
        if not self.type_assigned:
            return False
        elif self.type == "stack":
            self.dataStructure = Stack.createstack()
        elif self.type == "queue":
            self.dataStructure = ADTQueue.Queue()
            self.dataStructure.createQueue()
        elif self.type == "bst":
            self.dataStructure = BinarySearchTree.BinarySearchTree(None, None, None)
        elif self.type == "cl":
            self.dataStructure = ADTcircularLinkedChain.circular_chain()
        elif self.type == "ll":
            self.dataStructure = Dubbelgelinktelijst.createLinkedChain()
        elif self.type == "23":
            self.dataStructure = TweeDrieBoom.create23T()
        elif self.type == "234":
            self.dataStructure = T234.createSearchTree()
        elif self.type == "rb":
            self.dataStructure = RBT.createRBT()
        elif self.type == "hlin":
            self.dataStructure = Hashmap.createHashmap(self.grootte, 1)
        elif self.type == "hquad":
            self.dataStructure = Hashmap.createHashmap(self.grootte, 2)
        elif self.type == "hsep":
            self.dataStructure = Hashmap.createHashmap(self.grootte, 3)
        elif self.type == "heap":
            self.dataStructure = Heap.createHeap()

    def insert(self, value, key=None):
        if key == None:
            key = value

        if not self.type_assigned:
            return False
        elif self.type == "stack":
            return self.dataStructure.push(Stack.Node(value))
        elif self.type == "queue":
            return self.dataStructure.enqueue(key)
        elif self.type == "bst":
            return self.dataStructure.searchTreeInsert(BinarySearchTree.TreeItem(value, key))
        elif self.type == "cl":
            return self.dataStructure.insert(key, value)
        elif self.type == "ll":
            return self.dataStructure.insert(Dubbelgelinktelijst.Node(value, key))
        elif self.type == "23":
            return self.dataStructure.insertItem(TweeDrieBoom.TreeItem(value, key))
        elif self.type == "234":
            return self.dataStructure.T234Insert(T234.TreeItem(value, key))
        elif self.type == "rb":
            return self.dataStructure.insert(KeyValueItem(key, value))
        elif self.type == "hlin" or self.type == "hquad" or self.type == "hsep":
            return self.dataStructure.insert(key, value)
        elif self.type == "heap":
            return self.dataStructure.insert(KeyValueItem(key, value))

    def retrieve(self, key=None, value=None):
        if not self.type_assigned:
            return False
        elif self.type == "stack":
            return self.dataStructure.getTop()
        elif self.type == "queue":
            return self.dataStructure.getFront()
        elif self.type == "bst":
            return self.dataStructure.searchTreeRetrieve(key)
        elif self.type == "cl":
            return self.dataStructure.retrieve(key)
        elif self.type == "ll":
            return self.dataStructure.retrieve(key)
        elif self.type == "23":
            return self.dataStructure.retrieve(key) #geeft een tuple terug (bool, TreeItem)
        elif self.type == "234":
            return self.dataStructure.retrieve(key)
        elif self.type == "rb":
            return self.dataStructure.retrieve(key)
        elif self.type == "hlin" or self.type == "hquad":
            return self.dataStructure.retrieve(key) #enkel voor lin en quad, sep heeft ook item nodig
        elif self.type == "hsep":
            return self.dataStructure.retrieve(key, value)
        elif self.type == "heap":
            print("Retrieve is niet mogelijk bij een heap")  # Not implemented
            return False
            # return self.dataStructure.retrieve(key)

    def delete(self, key=None, value=None):
        if not self.type_assigned:
            return False
        elif self.type == "stack":
            return self.dataStructure.pop()
        elif self.type == "queue":
            return self.dataStructure.dequeue()
        elif self.type == "bst":
            return self.dataStructure.searchTreeDelete(key)
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
            return self.dataStructure.destroyQueue()
        elif self.type == "bst":
            return self.dataStructure.destroySearchTree()
        elif self.type == "cl":
            return self.dataStructure.destroyList()
        elif self.type == "ll":
            return self.dataStructure.destroyList()
        elif self.type == "23":
            return self.dataStructure.destroy23T()
        elif self.type == "234":
            return self.dataStructure.destroySearchtree()
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
            return self.dataStructure.isEmpty()
        elif self.type == "bst":
            return self.dataStructure.isEmpty()
        elif self.type == "cl":
            return self.dataStructure.isEmpty()
        elif self.type == "ll":
            return self.dataStructure.isEmpty()
        elif self.type == "23":
            return self.dataStructure.isEmpty()
        elif self.type == "234":
            return self.dataStructure.isEmpty()
        elif self.type == "rb":
            return self.dataStructure.isEmpty()
        elif self.type == "hlin" or self.type == "hquad" or self.type == "hsep":
            return self.dataStructure.isEmpty()
        elif self.type == "heap":
            return self.dataStructure.isEmpty()

    def getLength(self):
        if not self.type_assigned:
            return False
        elif self.type == "stack":
            return self.dataStructure.getLength()
            # return self.dataStructure.getLength()
        elif self.type == "queue":
            return self.dataStructure.getLength()
            # return self.dataStructure.getLength()
        elif self.type == "bst":
            return self.dataStructure.size()
            # return self.dataStructure.getLength()
        elif self.type == "cl":
            return self.dataStructure.getLength()
        elif self.type == "ll":
            return self.dataStructure.getLength()
        elif self.type == "23":
            return self.dataStructure.size()
            # return self.dataStructure.getLength()
        elif self.type == "234":
            return self.dataStructure.size()
            # return self.dataStructure.getLength()
        elif self.type == "rb":
            return self.dataStructure.size()
        elif self.type == "hlin" or self.type == "hquad" or self.type == "hsep":
            return self.dataStructure.size()
        elif self.type == "heap":
            return self.dataStructure.size()

    def Print(self):
        name = self.filenamegenerate()
        if not self.type_assigned:
            return False
        elif self.type == "stack":
            return self.dataStructure.print()
        elif self.type == "queue":
            return self.dataStructure.print(name)
        elif self.type == "bst":
            return self.dataStructure.print(name)
            return self.dataStructure.print()
        elif self.type == "cl":
            return self.dataStructure.visualize()
        elif self.type == "ll":
            return self.dataStructure.print(name)
        elif self.type == "23":
            return self.dataStructure.write_dot(name, self.dataStructure)
            return self.dataStructure.print("23.dot")
        elif self.type == "234":
            return self.dataStructure.print(name)
        elif self.type == "rb":
            return self.dataStructure.visualize(name)
        elif self.type == "hlin" or self.type == "hquad" or self.type == "hsep":
            return self.dataStructure.show()
        elif self.type == "heap":
            return self.dataStructure.visualize(name)

    # visit is een functie die telkens toegepast wordt op de root value
    def traverse(self, visit, key=None):
        if not self.type_assigned:
            return False
        elif self.type == "stack":
            return self.dataStructure.traverse(visit, key)
        elif self.type == "queue":
            return self.dataStructure.traverse(visit, key)
        elif self.type == "bst":
            return self.dataStructure.traverse(visit, key)  #InorderTraverse
        elif self.type == "cl":
            return self.dataStructure.traverse(visit, key)
        elif self.type == "ll":
            return self.dataStructure.traverse(visit, key)
        elif self.type == "23":
            return self.dataStructure.traverse(visit, key)  #InorderTraverse
        elif self.type == "234":
            return self.dataStructure.traverse(visit, key)  #InorderTraverse
        elif self.type == "rb":
            return self.dataStructure.traverse(visit, key)  #InorderTraverse
        elif self.type == "hlin":
            return self.dataStructure.traverse(visit, key)
        elif self.type == "hquad":
            return self.dataStructure.traverse(visit, key)
        elif self.type == "hsep":
            return self.dataStructure.traverse(visit, key)
        elif self.type == "heap":
            return self.dataStructure.traverse(visit, key)

    def filenamegenerate(self):
        count = 0
        string = self.type + '-' + str(count) + ".dot"
        exist = True
        while exist:
            try:
                fh = open(string, 'r')
            except FileNotFoundError:
                return string
            count += 1
            string = self.type + '-' + str(count) + ".dot"

# bob = Dubbelgelinktelijst.createLinkedChain()
# bob.insert(Dubbelgelinktelijst.Node(70, 1))  # Value - key
#
# bob2 = TabelWrapper("234")
# bob2.insert(70, 1)  # Value - key
#
# bob.destroyList()
# bob2.destroy()
#
#
# bob3 = TabelWrapper("bst")
# bob3.insert("tien", 10)
# bob3.insert("twee", 2)
# bob3.insert("vier", 4)
#
# # bob3.traverse(print)
#
# iterator = iter(bob3)
# print(next(iterator)[0])
# print(next(iterator)[0])
# print(next(iterator)[0])
# print()
#
# for root in bob3:
#     print(root[0])
# pass
