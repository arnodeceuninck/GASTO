#############
# DELETE THIS
from random import randint
class Graph:
    def __init__(self):
        self.nodes = []
        self.connections = []
        self.rankdir = "LR"
        self.rebuild_file()

    def rebuild_file(self):
        name = "graph.dot"
        with open(name, 'w'):
            pass
        file = open(name, "w")
        file.write("graph {\n")
        for node in self.nodes:
            file.write(str(node) + "\n")
        for connection in self.connections:
            file.write(str(connection) + "\n")
        file.write("rankdir=" + self.rankdir + "\n")
        file.write("}\n")
        file.close()

    def change_rankdir(self, rankdir):
        self.rankdir = rankdir

    def add_node(self, name, label_elements, shape):
        new_node = node(name, label_elements, shape)
        self.nodes.append(new_node)

    def add_connection(self, fromN, toN, type):
        new_connection = connection(fromN, toN, type)
        self.connections.append(new_connection)

class node:
    def __init__(self, name, label_elements, shape):
        self.name = name
        self.labels = label_elements
        self.shape = shape
    def __str__(self):
        string = str(self.name) + " ["
        string += "label=\""
        if not isinstance(self.labels, list):
            label_list = []
            label_list.append(self.labels)
            self.labels = label_list
        if len(self.labels) > 1:
            for label in self.labels:
                string += label + "| "
            string += "\""
        else:
            string += str(self.labels[0])
            string += "\""
        string += " shape="+self.shape
        string += "]"

        return string

class connection:
    def __init__(self, fromN, toN, type):
        self.fromN = fromN
        self.toN = toN
        self.type = type

    def __str__(self):
        CONNECTIONTYPES = {"arrow":"->", 0:"--", 1:"--"}
        string = ""
        string += str(self.fromN) + " "
        string += CONNECTIONTYPES[self.type] + " "
        string += str(self.toN) + " "
        if self.type == 0:
            string += '[color ="black"]' + " "
        elif self.type == 1:
            string += '[color ="red"]' + " "
        return string
########################
# Todo: Remove this line, staat er momenteel om tijdens het debuggen de boom te kunnen visualizeren
sprookjesboom = None

class RoodZwartBoom:
    # Aparte klasse nodig aangezien de root kan veranderen
    def __init__(self):
        self.root = RZTNode()

    def createRBT(self):
        return self.root.createRBT()

    def isEmpty(self):
        return self.root.isEmpty()

    def insert(self, newItem):
        self.root.insert(newItem)
        self.root = self.root.findNewRoot()
        return

    def remove(self, key):
        self.root.remove(key)
        self.root = self.root.findNewRoot()
        return

    def visualize(self):
        vgraph = Graph()
        vgraph.change_rankdir("TB")
        self.root.createVisualisation(vgraph)
        vgraph.rebuild_file()

    def remove(self, key):
        return self.root.remove(key)


class RZTNode:

    def __init__(self):

        # Variabelen ivm de rootgegevens
        self.root_key = None
        self.root_value = None

        # Variabelen ivm de linkerdeelboom
        # Connection:
        # 0 = black (parent-child)
        # 1 = red (in same node)
        self.left_tree = None
        self.left_connection = None

        # Variabelen ivm de rechterdeelboom
        self.right_tree = None
        self.right_connection = None

        self.parent = None

        self.createRBT()

    def createRBT(self):

        self.root_key = None
        self.root_value = None

        self.left_tree = None
        self.left_connection = None

        self.right_tree = None
        self.right_connection = None

        self.parent = None

    def findNewRoot(self):
        root = self
        while(root.parent != None):
            root = root.parent
        return root
    def destroyRBT(self):

        self.root_key = None
        self.root_value = None

        # TODO: Delete all items in the subtrees
        self.left_tree = None
        self.left_connection = None

        self.right_tree = None
        self.right_connection = None

        self.parent = None

        del self

    def isEmpty(self):
        if self.root_key is None:
            return True

    def rotateRight(self):

        if self.parent != None and self.parent.parent != None:
            if self.parent.parent.left_tree == self.parent:
                self.parent.parent.left_tree = self
            elif self.parent.parent.right_tree == self.parent:
                self.parent.parent.right_tree = self

        temp_tree = self.right_tree
        self.right_tree = self.parent
        self.right_connection = 1
        self.parent = self.right_tree.parent
        self.right_tree.parent = self

        self.right_tree.left_tree = temp_tree
        self.right_tree.left_connection = 0

        if self.left_tree.right_tree is not None:
            self.left_tree.right_tree.parent = self.left_tree

    def rotateUp(self):
        if(self.right_connection == 1):
            newTop = self.right_tree
        elif(self.left_connection == 1):
            newTop = self.left_tree

        if self.parent != None and self.parent.parent != None:
            if self.parent.parent.left_tree == self.parent:
                self.parent.parent.left_tree = newTop
            elif self.parent.parent.right_tree == self.parent:
                self.parent.parent.right_tree = newTop

        tempLeftTree = newTop.left_tree
        tempRightTree = newTop.right_tree

        if(self.parent.root_key > newTop.root_key):
            newTop.right_tree = self.parent
            newTop.right_connection = 1
            newTop.left_tree = self
            newTop.left_connection = 1
        elif(self.parent.root_key > newTop.root_key):
            newTop.left_tree = self.parent
            newTop.left_connection = 1
            newTop.right_tree = self
            newTop.right_connection = 1

        if(newTop.left_tree != None):
            newTop.left_tree.right_tree = tempLeftTree
            newTop.left_tree.right_connection = 0
            newTop.left_tree.parent = newTop
        if(newTop.right_tree != None):
            newTop.right_tree.left_tree = tempRightTree
            newTop.right_tree.left_connection = 0
            newTop.right_tree.parent = newTop

    def rotateLeft(self):
        if self.parent != None and self.parent.parent != None:
            if self.parent.parent.left_tree == self.parent:
                self.parent.parent.left_tree = self
            elif self.parent.parent.right_tree == self.parent:
                self.parent.parent.right_tree = self

        temp_tree = self.left_tree
        self.left_tree = self.parent
        self.left_connection = 1
        self.parent = self.left_tree.parent
        self.left_tree.parent = self

        self.left_tree.right_tree = temp_tree
        self.left_tree.right_connection = 0

        if self.left_tree.right_tree is not None:
            self.left_tree.right_tree.parent = self.left_tree

    def check_split(self):
        if self.left_connection == 1 and self.right_connection == 1:
            self.split()

    def check_rotation(self):
        if self.left_connection == 1 and self.findConnectionWithParent() == 1 and self.parent.left_tree == self:
            return self.rotateRight()
        elif self.right_connection == 1 and self.findConnectionWithParent() == 1 and self.parent.right_tree == self:
            return self.rotateLeft()
        elif (self.left_connection == 1 or self.right_connection == 1) and self.findConnectionWithParent() == 1:
            return self.rotateUp()

    def split(self):

        self.left_connection = 0
        self.right_connection = 0
        # De node wordt gesplitst en de middelste 'springt' in de node van zijn parent
        if self.parent != None:
            if self.parent.left_tree == self:
                self.parent.left_connection = 1
            elif self.parent.right_tree == self:
                self.parent.right_connection = 1
            self.parent.check_rotation()
            # if self.parent.parent != None: # Niet meer nodig, want alle 4 knopen op pad zijn al gesplitst
            #     self.parent.parent.check_split()
        # Splitsen gedaan

    def findConnectionWithParent(self):
        if self.parent == None:
            return 0  # Zwarte verbinding is geen speciaal geval
        elif self.parent.left_tree == self:
            return self.parent.left_connection
        elif self.parent.right_tree == self:
            return self.parent.right_connection

    def insert(self, newItem):
        # Bij een lege boom
        if self.isEmpty():
            self.root_key = newItem.key
            self.root_value = newItem.value
            return True

        # Doorloop het blad van wortel tot blad en splits alle 4-knopen
        # 4 knoop als zowel linker als rechter boom in dezelfde node zitten
        self.check_split()

        # Bepaal de verbinding tussen self en parent, om te weten of er een rotation moet komen na het toevoegen
        # connection_with_parent = self.findConnectionWithParent()

        # Kunnen we vanuit deze deelboom inserten?
        # Linkerblad is leeg, hier moet het item komen, in dezelfde node
        if newItem.key < self.root_key and self.left_tree is None:
            # maak de nieuwe boom aan
            subtree = RZTNode()

            subtree.root_key = newItem.key
            subtree.root_value = newItem.value

            # Maak de nieuwe boom vast aan de huidige boom met een rode verbinding
            subtree.parent = self
            self.left_tree = subtree
            self.left_connection = 1

            # Als zij een zwarte relatie hebben met elkaar kan de knoop gewoon toegevoegd worden
            # Anders moet de knoop nog 'draaien' rond zichzelf.
            # Dwz dat zijn parent zijn rechterdeelboom wordt en zijn oorspronkelijke rechterdeelboom
            # De linkerdeelboom daarvan wordt
            self.check_rotation()
            return True

        # Voeg het item rechts toe
        if newItem.key > self.root_key and self.right_tree is None:

            subtree = RZTNode()

            subtree.root_key = newItem.key
            subtree.root_value = newItem.value

            subtree.parent = self
            self.right_tree = subtree
            self.right_connection = 1

            self.check_rotation()

            return True

        # Deze parent heeft geen vrije plaatsen, het moet dus een niveau lager geinsert worden
        if self.root_key < newItem.key:
            self.right_tree.insert(newItem)
        elif self.root_key > newItem.key:
            self.left_tree.insert(newItem)

    def findInorderSuccessor(self):
        # TODO: Elke 2-node omvormen in 3-node of 4-node
        if self.right_tree is None:
            return self
        inorder_successor = self.right_tree
        while inorder_successor.left_tree is not None:
            inorder_successor = inorder_successor.left_tree
        return inorder_successor

    def makeThreeFourNode(self):
        # Geval 1: Als de ouder en siblings 2 nodes zijn
        # Gewoon een omgekeerde split doen
        if self.parent == None:
            self.left_connection = 1
            self.right_connection = 1
            self.left_tree.left_connection = 0
            self.right_tree.left_connection = 0
            self.left_tree.right_connection = 0
            self.right_tree.right_connection = 0

        elif self.parent.checkTwoNode() \
                and self.parent.left_tree.checkTwoNode() \
                and self.parent.right_tree.checkTwoNode():
            self.parent.left_connection = 1
            self.parent.right_connection = 1
            # De node wordt gesplitst en de middelste 'springt' in de node van zijn parent
            if self.parent.parent != None:
                if self.parent.parent.left_tree == self:
                    self.parent.parent.left_connection = 0
                elif self.parent.parent.right_tree == self:
                    self.parent.parent.right_connection = 0
                self.parent.parent.check_rotation()

        # Geval 2: Als de ouder een 3-knoop is
        # Eentje uit de ouder laten zakken en in een nieuwe node steken
        #   die bestaat uit een merge van 2 siblings + element uit ouder
        # Let op: Enkel sibling-buurtjes kunnen gemerged worden
        elif self.parent.checkThreeNode():
            # Geval A: We zitten in S
            # Todo: Maak dit met de letters uit de GAS slides, zo kan geval L ook makkelijk geimplementeerd worden
            # GAS slide 405

            # Ik gebruik hier de letters van de tekening van de cursus van GAS (slide 405)
            # S en L zijn wel omgewisseld tov de onderste tekening van de slide

            if self.parent.findConnectionWithParent() == 0:
                # We zitten in S
                s = self
                m = s.parent
                # p is afhankelijk van geval A of B op die slide
                if s.root_key < m.root_key:
                    p = m.right_tree  # Wordt de nieuwe root
                    l = p.left_tree
                elif s.root_key > m.root_key:
                    p = m.left_tree
                    l = p.right_tree

            elif self.parent.findConnectionWithParent() == 1:
                # We zitten in L
                l = self
                p = self.parent
                m = p.parent
                if p.root_key > m.root_key:
                    s = m.left_tree
                elif p.root_key < m.root_key:
                    s = m.right_tree

            if m.parent.left_tree == m:
                m.parent.left_tree = p
            elif m.parent.right_tree == m:
                m.parent.right_tree = p
            p.parent = m.parent

            # tempLeft = p.left_tree zit al in l
            if p.root_key < m.root_key:
                p.left_tree = m
            elif p.root_key < m.root_key:
                p.right_tree = m

            m.parent = p

            if m.root_key > l.root_key:
                m.left_tree = l
                m.right_tree = s
            elif m.root_key < l.root_key:
                m.right_tree = l
                m.left_tree = s

            m.left_connection = 1
            m.right_connection = 1

        # Geval 3: Als de ouder een 4 knoop is
        # Let op: Enkel sibling-buurtjes kunnen gemerged worden
        elif self.parent.checkFourNode():
            m = self.parent
            if m.parent.left_tree == m and m.left_tree == self:
                m.parent.left_connection = 0
                m.left_connection = 1
                m.right_connection = 1
                return
            elif m.parent.right_tree == m and m.right_tree == self:
                m.parent.right_connection = 0
                m.left_connection = 1
                m.right_connection = 1
                return
            else:
                p = m.parent
                if m.right_connection == self:
                    s = self
                    q = p.right_connection
                    l = q.left_connection
                else:
                    l = self
                    q = l.parent
                    p = q.parent
                    m = p.left_tree
                    s = m.right_tree

                p.left_tree = m.left_tree
                p.left_connection = 0
                q.left_tree = m
                m.left_tree = s
                m.left_connection = 1
                m.right_tree = l
                m.right_connection = 1

    def checkTwoNode(self):
        # Werkt ook in sommige gevallen bij 3 nodes,
        #   maar deze moeten dan hetzelfde delete algoritme volgen als een 2 node
        # Nu niet meer:
        if self.findConnectionWithParent() == 1:
            return self.parent.checkTwoNode()

        if self.left_connection == 0 and self.right_connection == 0:
            return True
        return False

    def checkThreeNode(self):
        if self.findConnectionWithParent() == 1:
            return self.parent.checkTreeNode()

        if self.left_connection is not None \
                and self.right_connection is not None\
                and self.left_connection + self.right_connection == 1: # Maar 1 van de 2 is rood
            return True
        return False

    def checkThreeNode(self):
        if self.findConnectionWithParent() == 1:
            return self.parent.checkTreeNode()

        if self.left_connection is not None \
                and self.right_connection is not None\
                and self.left_connection + self.right_connection == 2: # allebei rood
            return True
        return False

    def remove(self, key):
        # TODO: Elke 2-node omvormen in 3-node of 4-node
        if self.checkTwoNode():
            self.makeThreeFourNode()

        if self.root_key < key and self.right_tree is not None:
            return self.right_tree.remove(key)
        elif self.root_key > key and self.left_tree is not None:
            return self.left_tree.remove(key)
        elif self.root_key != key:
            print("Key not found.")
            return 404

        # We bevinden ons in de Node die verwijderd zal moeten worden
        inorder_successor = self.findInorderSuccessor()

        # Blad inorder successor is nu altijd een 3-knoop of 4-knoop
        # swap deze items
        if inorder_successor.parent != self:
            tempParent = inorder_successor.parent
        else:
            tempParent = inorder_successor

        tempRight = inorder_successor.right_tree
        tempRightC = inorder_successor.findConnectionWithParent()

        inorder_successor.left_tree = self.left_tree
        inorder_successor.left_connection = self.left_connection
        self.left_tree = None
        if(self.right_tree != inorder_successor):
            inorder_successor.right_tree = self.right_tree
        else:
            inorder_successor.right_tree = self
        inorder_successor.right_connection = self.right_connection
        # Het type connection met de parent blijft hetzelfde
        if self.parent.left_tree == self:
            self.parent.left_tree = inorder_successor
        elif self.parent.right_tree == self:
            self.parent.right_tree = inorder_successor
        inorder_successor.parent = self.parent
        self.left_tree = None
        self.right_tree = None
        self.parent = tempParent
        if self.parent.left_tree == self:
            self.parent.left_tree = tempRight
            self.parent.left_connection = tempRightC
        elif self.parent.right_tree ==self:
            self.parent.right_tree = tempRight
            self.parent.right_connection = tempRightC

        return self.destroyRBT()

    def createVisualisation(self, vgraph):
        if not self.isEmpty():
            if self.left_tree is not None:
                vgraph.add_connection(self.root_key, self.left_tree.root_key, self.left_connection)
                self.left_tree.createVisualisation(vgraph)

            if self.right_tree is not None:
                vgraph.add_connection(self.root_key, self.right_tree.root_key, self.right_connection)
                self.right_tree.createVisualisation(vgraph)



class RBTItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value



sprookjesboom = RoodZwartBoom()

sprookjesboom.insert(RBTItem(3, 3))

sprookjesboom.insert(RBTItem(4, 4))

sprookjesboom.insert(RBTItem(2, 2))

sprookjesboom.insert(RBTItem(1, 1))

sprookjesboom.insert(RBTItem(5, 5))

sprookjesboom.insert(RBTItem(7, 7))

sprookjesboom.insert(RBTItem(8, 8))

sprookjesboom.insert(RBTItem(6, 6))
#
sprookjesboom.insert(RBTItem(9, 9))

sprookjesboom.remove(7)
sprookjesboom.visualize()

pass