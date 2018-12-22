from Graph import *
from KeyValueItem import *

class RoodZwartBoom:
    # Aparte klasse nodig aangezien de root kan veranderen

    def __init__(self):
        self.root = None # Alle waarden moeten eerst in de __init__ voorkomen
        self.createRBT()

    def createRBT(self):
        # Stelt alle waarden in op de default-waarden
        self.root = RBTNode()
        return self.root.createRBT()

    def destroyRBT(self):
        # Verwijdert een boom
        return self.root.destroyRBT()

    def isEmpty(self):
        # Kijkt of een boom leeg is
        # Een boom is leeg als zijn root leeg is
        # De root zou altijd moeten bestaan, aangezien deze in de __init__ -> createRBT() wordt aangemaakt
        return self.root.isEmpty()

    def insert(self, newItem):
        # Steek een nieuw item in de boom
        success = self.root.insert(newItem)
        # Tijdens het inserten kan de root veranderd worden
        self.root = self.root.findNewRoot()
        return success

    def remove(self, key):
        # Verwijdert een item uit de boom
        success = self.root.remove(key)
        # Tijdens het verwijderen kan de root veranderd worden
        self.root = self.root.findNewRoot()
        return success

    def visualize(self):
        # Maakt een .dot file met daarin een visuele representatie van de boom (in .dot language)
        vgraph = Graph("RBT")
        vgraph.change_rankdir("TB") # Bomen worden meestal van Top to Bottem getoond
        # Doorloop de boom, startende bij de root om er een visualisatie van te maken
        self.root.createVisualisation(vgraph)
        # Alle nodes en verbindingen zijn nu toegevooegd aan vgraph, maak er nu dus het bestand zelf van
        vgraph.rebuild_file()

    def remove(self, key):
        # Verwijdert een item uit de boom
        # Er moet wel een item bestaan dat verwijderc kan worden, dus als er geen root is,
        # Dan is dit al niet het geval
        if self.root is not None:
            return self.root.remove(key)
        else:
            return False

    def retrieve(self, key):
        # returnt het RBTItem waarbij RBTItem.key == key
        # Er moet een item bestaan om een item te vinden
        if self.root is not None:
            return self.root.retrieve(key)
        else:
            return False

    def getRoot(self):
        # Returnt het RBTItem dat in de top van de RZB zit
        return self.root

class RBTNode:

    def __init__(self):
        # Orginele plan was om dit enkel in createRBT te schrijven,
        # maar dan doet python moeilijk aangezien de variabelen niet in de __init__ aangemaakt werden

        # Variabelen ivm de rootgegevens
        self.root = None

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
        # Stelt alle variabelen in op hun defaultwaarden
        self.root = None

        self.left_tree = None
        self.left_connection = None

        self.right_tree = None
        self.right_connection = None

        self.parent = None

    def findNewRoot(self):
        # Zoekt de node waarvan alle andere nodes (klein-)kinderen zijn
        if self.parent != None:
            return self.parent.findNewRoot()
        return self

    def destroyRBT(self):
        # self.preorderTraverse(self.destroyNode) # TODO: Check if this works
        if(self.left_tree != None):
            self.left_tree.destroyNode()
        if (self.right_tree != None):
            self.right_tree.destroyNode()
        return self.destroyNode()

    def destroyNode(self):

        self.root = None

        self.left_tree = None
        self.left_connection = None

        self.right_tree = None
        self.right_connection = None

        self.parent = None

        del self
        return True

    def isEmpty(self):
        if self.root is None:
            return True

    def rotateRight(self):
        # Maakt een rotatie van 3 elementen die in dezelfde Node zitten,
        # self.parent.left_tree == self #TODO: check this
        #   en self.findConnectionWithParent == 1
        #   en self.left_tree.left_connection == 1
        # De nodes staan dus op eenzelfde rechte in het vlak

        # Het kind van de grootouder van de middelste node wordt veranderd naar de huidige node
        # Als self.parent.parent niet bestaat, dan moet deze ook niet veranderd worden
        # Als self.parent niet bestaat, dan zitten we niet in de middelste node, en zijn we dus fout begonnen #TODO
        if self.parent != None and self.parent.parent != None:
            # Hiervoor moeten we eerst weten of self.parent links of rechts staat van self.parent.parent
            if self.parent.parent.left_tree == self.parent:
                self.parent.parent.left_tree = self
            elif self.parent.parent.right_tree == self.parent:
                self.parent.parent.right_tree = self

        # De 'parent' komt rechts van de middelste node
        temp_tree = self.right_tree
        self.right_tree = self.parent
        # Deze verplaatste node, blijft nogsteeds mee in dezelfde node zitten
        self.right_connection = 1
        # deze node krijgt dus een nieuwe parent
        self.parent = self.right_tree.parent
        # En de parent van de net verplaatste node verandert ook
        self.right_tree.parent = self

        # De oorspronkelijke rechter node wordt nu de linkernode van de oorspronkelijke parent
        self.right_tree.left_tree = temp_tree
        self.right_tree.left_connection = 0

        # Parent van de net verplaatste deelboom terug juistzetten
        if self.left_tree.right_tree is not None:
            self.left_tree.right_tree.parent = self.left_tree

    def rotateUp(self):
        # Draait drie nodes met 3 elementen, die niet op eenzelfde rechte in het vlak liggen

        # Bepaal de nieuwe top,
        # dit is het element waarvan het ene element een kleinere waarde heeft en het andere een grotere waarde heeft
        # Dit is dus het element waarvan deze node de parent is
        if(self.right_connection == 1):
            newTop = self.right_tree
        elif(self.left_connection == 1):
            newTop = self.left_tree

        # De top verandert, dus de grootouder krijgt een nieuw kind
        # Bepaal of dit kind links of rechts komt
        if self.parent != None and self.parent.parent != None:
            if self.parent.parent.left_tree == self.parent:
                self.parent.parent.left_tree = newTop
            elif self.parent.parent.right_tree == self.parent:
                self.parent.parent.right_tree = newTop

        # Onthoud de 2 deelbomen van de toekomstige nieuwe top
        tempLeftTree = newTop.left_tree
        tempRightTree = newTop.right_tree

        # Plaats self en de parent van self op de juiste positie van de nieuwe boom,
        #  dwz links indien de key kleiner is en rechts indien de key groter is
        if(self.parent.root.key > newTop.root.key):
            newTop.right_tree = self.parent
            newTop.left_tree = self
        elif(self.parent.root.key > newTop.root.key):
            newTop.left_tree = self.parent
            newTop.right_tree = self

        newTop.left_connection = 1
        newTop.right_connection = 1

        # Zet de oorspronkelijke deelbomen van newTop terug op de juiste plaats

        newTop.left_tree.right_tree = tempLeftTree
        newTop.left_tree.right_connection = 0
        newTop.left_tree.parent = newTop

        newTop.right_tree.left_tree = tempRightTree
        newTop.right_tree.left_connection = 0
        newTop.right_tree.parent = newTop

    def rotateLeft(self):
        # Zie rotateRight() voor de comments die hierbij horen

        # grootvader krijgt een niew kind, namelijk de nieuwe top
        if self.parent != None and self.parent.parent != None:
            if self.parent.parent.left_tree == self.parent:
                self.parent.parent.left_tree = self
            elif self.parent.parent.right_tree == self.parent:
                self.parent.parent.right_tree = self

        # de nieuwe top (self) krijgt een nieuwe linkerdeelboom en rechterdeelboom
        # de rechterdeelboom blijft hetzelfde
        temp_tree = self.left_tree
        self.left_tree = self.parent
        self.left_connection = 1
        self.parent = self.left_tree.parent
        self.left_tree.parent = self

        # juistzetten van de oorspronkelijke linkerdeelboom
        self.left_tree.right_tree = temp_tree
        self.left_tree.right_connection = 0

        if self.left_tree.right_tree is not None:
            self.left_tree.right_tree.parent = self.left_tree

    def check_split(self):
        # controleert of we in een 4-knoop zitten en splitst deze indien nodig
        if self.left_connection == 1 and self.right_connection == 1:
            self.split()

    def check_rotation(self):
        # iedere 4-node bestaat uit een bovenste element, met een linker en rechterdeelboom die in dezelfde node zitten
        # deze functie controleert of dit bij deze node het geval is, indien dit niet is, zal de node gedraaid worden,
        # zodat dit erna wel het geval is
        if self.left_connection == 1 and self.findConnectionWithParent() == 1 and self.parent.left_tree == self:
            return self.rotateRight()
        elif self.right_connection == 1 and self.findConnectionWithParent() == 1 and self.parent.right_tree == self:
            return self.rotateLeft()
        elif (self.left_connection == 1 or self.right_connection == 1) and self.findConnectionWithParent() == 1:
            return self.rotateUp()

    def split(self):
        # Deze functie zal een 4-node splitsen

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
            self.root = newItem
            return True

        # Doorloop het blad van wortel tot blad en splits alle 4-knopen
        # 4 knoop als zowel linker als rechter boom in dezelfde node zitten
        self.check_split()

        # Bepaal de verbinding tussen self en parent, om te weten of er een rotation moet komen na het toevoegen
        # connection_with_parent = self.findConnectionWithParent()

        # Kunnen we vanuit deze deelboom inserten?
        # Linkerblad is leeg, hier moet het item komen, in dezelfde node
        if newItem.key < self.root.key and self.left_tree is None:
            # maak de nieuwe boom aan
            subtree = RBTNode()

            subtree.root = newItem

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
        if newItem.key > self.root.key and self.right_tree is None:

            subtree = RBTNode()

            subtree.root = newItem

            subtree.parent = self
            self.right_tree = subtree
            self.right_connection = 1

            self.check_rotation()

            return True

        # Deze parent heeft geen vrije plaatsen, het moet dus een niveau lager geinsert worden
        if self.root.key < newItem.key:
            self.right_tree.insert(newItem)
        elif self.root.key > newItem.key:
            self.left_tree.insert(newItem)

    def findInorderSuccessor(self):
        if self.right_tree is None:
            return self

        inorder_successor = self.right_tree

        while inorder_successor.left_tree is not None:

            # Alle 2 nodes op het pad moeten 3/4 nodes worden
            if(inorder_successor.check_TwoNode()):
                inorder_successor.makeThreeFoutNode()

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
            # GAS slide 405

            # Ik gebruik hier de letters van de tekening van de cursus van GAS (slide 405)
            # S en L zijn wel omgewisseld tov de onderste tekening van de slide

            if self.parent.findConnectionWithParent() == 0:
                # We zitten in S
                s = self
                m = s.parent
                # p is afhankelijk van geval A of B op die slide
                if s.root.key < m.root.key:
                    p = m.right_tree  # Wordt de nieuwe root
                    l = p.left_tree
                elif s.root.key > m.root.key:
                    p = m.left_tree
                    l = p.right_tree

            elif self.parent.findConnectionWithParent() == 1:
                # We zitten in L
                l = self
                p = self.parent
                m = p.parent
                if p.root.key > m.root.key:
                    s = m.left_tree
                elif p.root.key < m.root.key:
                    s = m.right_tree

            if m.parent.left_tree == m:
                m.parent.left_tree = p
            elif m.parent.right_tree == m:
                m.parent.right_tree = p
            p.parent = m.parent

            # tempLeft = p.left_tree zit al in l
            if p.root.key < m.root.key:
                p.left_tree = m
            elif p.root.key < m.root.key:
                p.right_tree = m

            m.parent = p

            if m.root.key > l.root.key:
                m.left_tree = l
                m.right_tree = s
            elif m.root.key < l.root.key:
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
        # Ga naar het bovenste element van de knoop waar je in zit
        if self.findConnectionWithParent() == 1:
            return self.parent.checkTwoNode()

        # Als zowel links als rechts niet in dezelfde node zitten, dan is het een 2-node
        if self.left_connection == 0 and self.right_connection == 0:
            return True
        return False

    def checkThreeNode(self):
        # Ga naar het bovenste element van een knoop
        if self.findConnectionWithParent() == 1:
            return self.parent.checkTreeNode()

        # Kijk vandaaruit of het een 3 node is
        if (self.left_tree is not None and self.left_tree.root is not None and self.left_connection == 1 and (self.right_tree is None or self.right_connection == 0))\
                or (self.right_tree is not None and self.right_tree.root is not None and self.right_connection == 1 and (self.left_tree is None or self.left_connection == 0)):
            return True
        return False

    def checkThreeNode(self):
        # Ga naar het bovenste element van de knoop
        if self.findConnectionWithParent() == 1:
            return self.parent.checkTreeNode()

        # Kijk of deze 2 andere elementen heeft in dezelfde node
        if self.left_connection is not None \
                and self.right_connection is not None\
                and self.left_connection + self.right_connection == 2: # allebei rood
            return True
        return False

    def remove(self, key):
        # Vorm elke 2 node in het pad om in een 3 of 4 node
        if self.checkTwoNode():
            self.makeThreeFourNode()

        if self.root.key < key and self.right_tree is not None:
            return self.right_tree.remove(key)
        elif self.root.key > key and self.left_tree is not None:
            return self.left_tree.remove(key)
        elif self.root.key != key:
            print("Key to remove not found.")
            return False

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
        # voeg iedere node toe
        vgraph.add_node(self.root.key, self.root.key)
        if not self.isEmpty():

            if self.left_tree is None and self.right_tree is None:
                return

            # voeg de linkerverbinding toe
            if self.left_tree is not None:
                self.left_tree.createVisualisation(vgraph)
                vgraph.add_connection(self.root.key, self.left_tree.root.key, self.left_connection)
            else:
                # (Kan ook onzichtbaar zijn als er geen is, zodat het andere element duidelijk links of rechts van de node is)
                vgraph.add_node("left" + str(self.root.key), "0", "circle", "style=invis")
                vgraph.add_connection(self.root.key, "left" + str(self.root.key), 0, "style=invis")

            # voeg de rechterverbinding toe
            if self.right_tree is not None:
                self.right_tree.createVisualisation(vgraph)
                vgraph.add_connection(self.root.key, self.right_tree.root.key, self.right_connection)
            else:
                vgraph.add_node("right" + str(self.root.key), "0", "circle", "style=invis")
                vgraph.add_connection(self.root.key, "right" + str(self.root.key), 0, "style=invis")

    def retrieve(self, key):

        if self.root is not None and self.root.key == key:
            return (True, (self.root.key, self.root.value))

        elif self.root is not None \
                and self.root.key < key \
                and self.right_tree is not None:
            return self.right_tree.retrieve(key)

        elif self.root is not None \
                and self.root.key > key \
                and self.left_tree is not None:
            return self.left_tree.retrieve(key)

        # key niet gelijk aan de huidige node, en geen verdere linker/rechter vertakkingen
        else:
            return (False, None)

    def inorderTraverse(self, visit):
        if self.left_tree is not None:
            self.left_tree.inorderTraverse(visit)
        visit(self) # Todo: test if works
        if self.right_tree is not None:
            self.right_tree.inorderTravers(visit)

    def preorderTraverse(self, visit):
        visit(self)
        if self.left_tree is not None:
            self.left_tree.inorderTraverse(visit)
        if self.right_tree is not None:
            self.right_tree.inorderTravers(visit)

    def postorderTraverse(self, visit):
        if self.left_tree is not None:
            self.left_tree.inorderTraverse(visit)
        if self.right_tree is not None:
            self.right_tree.inorderTravers(visit)
        visit(self)

def createRBT():
    return RoodZwartBoom()


# # Maak een nieuwe boom aan
# sprookjesboom = createRBT()
#
# # Voeg er een hoop key-value pairs aan toe
# sprookjesboom.insert(KeyValueItem(3, 3))
# sprookjesboom.insert(KeyValueItem(4, 4))
# sprookjesboom.insert(KeyValueItem(2, 2))
# sprookjesboom.insert(KeyValueItem(1, 1))
# sprookjesboom.insert(KeyValueItem(5, 5))
# sprookjesboom.visualize()
# sprookjesboom.insert(KeyValueItem(7, 7))
# sprookjesboom.insert(KeyValueItem(8, 8))
# sprookjesboom.insert(KeyValueItem(6, 6))
# sprookjesboom.insert(KeyValueItem(9, 9))
# # Verwijder het item met zoeksleutel 7
# sprookjesboom.remove(7)
#
# # Maak een .dot file voor deze boom
# sprookjesboom.visualize()
#
# pass