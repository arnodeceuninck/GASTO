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

class RoodZwartBoom:

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

    def insert(self, newItem):
        # Bij een lege boom
        if self.isEmpty():
            self.root_key = newItem.key
            self.root_value = newItem.value
            return True

        # Doorloop het blad van wortel tot blad en splits alle 4-knopen
        # 4 knoop als zowel linker als rechter boom in dezelfde node zitten
        if self.left_connection == 1 and self.right_connection == 1:
            self.left_connection = 0
            self.right_connection = 0
            # De node wordt gesplitst en de middelste 'springt' in de node van zijn parent
            if self.parent != None:
                if self.parent.left_tree == self:
                    self.parent.left_connection = 1
                elif self.parent.right_tree == self:
                    self.parent.right_connection = 1
        # Splitsen gedaan

        # Bepaal de verbinding tussen self en parent, om te weten of er een rotation moet komen na het toevoegen
        if self.parent == None:
            connection_with_parent = 0  # Zwarte verbinding is geen speciaal geval
        elif self.parent.left_tree == self:
            connection_with_parent = self.parent.left_connection
        elif self.parent.right_tree == self:
            connection_with_parent = self.parent.right_connection


        # Kunnen we vanuit deze deelboom inserten?
        # Linkerblad is leeg, hier moet het item komen, in dezelfde node
        if newItem.key < self.root_key and self.left_tree is None:
            # maak de nieuwe boom aan
            subtree = RoodZwartBoom()

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
            if connection_with_parent == 1:
                if self.parent.parent.left_tree == self.parent:
                    self.parent.parent.left_tree = self
                elif self.parent.parent.right_tree == self.parent:
                    self.parent.parent.right_tree = self

                temp_tree = self.right_tree
                self.right_tree = self.parent
                self.right_connection = 1
                self.parent = self.left_tree.parent
                self.right_tree.parent = self

                self.right_tree.left_tree = temp_tree
                self.right_tree.left_connection = 0

                if self.left_tree.right_tree is not None:
                    self.left_tree.right_tree.parent = self.left_tree

            return True

        # Voeg het item rechts toe
        if newItem.key > self.root_key and self.right_tree is None:

            subtree = RoodZwartBoom()

            subtree.root_key = newItem.key
            subtree.root_value = newItem.value

            subtree.parent = self
            self.right_tree = subtree
            self.right_connection = 1

            if connection_with_parent == 1:
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

            return True

        # Deze parent heeft geen vrije plaatsen, het moet dus een niveau lager geinsert worden
        if self.root_key < newItem.key:
            self.right_tree.insert(newItem)
        elif self.root_key > newItem.key:
            self.left_tree.insert(newItem)

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


vgraph = Graph()
vgraph.change_rankdir("TB")

sprookjesboom = RoodZwartBoom()
sprookjesboom.insert(RBTItem(3, 3))

vgraph = Graph()
vgraph.change_rankdir("TB")
sprookjesboom.createVisualisation(vgraph)
vgraph.rebuild_file()

sprookjesboom.insert(RBTItem(4, 4))
vgraph = Graph()
vgraph.change_rankdir("TB")
sprookjesboom.createVisualisation(vgraph)
vgraph.rebuild_file()

sprookjesboom.insert(RBTItem(2, 2))
vgraph = Graph()
vgraph.change_rankdir("TB")
sprookjesboom.createVisualisation(vgraph)
vgraph.rebuild_file()
sprookjesboom.insert(RBTItem(1, 1))
vgraph = Graph()
vgraph.change_rankdir("TB")
sprookjesboom.createVisualisation(vgraph)
vgraph.rebuild_file()

sprookjesboom.insert(RBTItem(5, 5))
vgraph = Graph()
vgraph.change_rankdir("TB")
sprookjesboom.createVisualisation(vgraph)
vgraph.rebuild_file()

# Hier is er nog een probleem, wat er zou moeten gebeuren:
# 5 wordt het nieuwe kind van 3, 4 komt daar liks van en 7 rechts
sprookjesboom.insert(RBTItem(7, 7))
vgraph = Graph()
vgraph.change_rankdir("TB")
sprookjesboom.createVisualisation(vgraph)
vgraph.rebuild_file()

sprookjesboom.insert(RBTItem(8, 8))
vgraph = Graph()
vgraph.change_rankdir("TB")
sprookjesboom.createVisualisation(vgraph)
vgraph.rebuild_file()

pass