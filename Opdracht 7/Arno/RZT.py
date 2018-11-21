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

        # Aangekomen in een blad, het item wordt toegevoegd in het blad

        # find the connection between self and his parent
        if self.parent == None:
            connection_with_parent = 0  # Zwarte verbinding is geen speciaal geval
        else:
            if self.root_key < self.parent.root_key:
                connection_with_parent = self.parent.left_connection
            elif self.root_key > self.parent.root_key:
                connection_with_parent = self.parent.right_connection

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
            if connection_with_parent == 0:
                return True
            # Anders moet de knoop nog 'draaien' rond zichzelf.
            # Dwz dat zijn parent zijn rechterdeelboom wordt en zijn oorspronkelijke rechterdeelboom
            # De linkerdeelboom daarvan wordt
            elif connection_with_parent == 1:

                temp_tree = self.right_tree
                self.right_tree = self.parent
                self.right_connection = 1

                self.right_tree.left_tree = temp_tree
                self.right_tree.left_connection = 0
                return True



        if newItem.key > self.root_key and self.right_tree is None:


            subtree = RoodZwartBoom()

            subtree.root_key = newItem.key
            subtree.root_value = newItem.value

            subtree.parent = self
            self.right_tree = subtree
            self.right_connection = 1

            if connection_with_parent == 0:
                # Het toevoegen in dit blad is gebeurd
                return True

            elif connection_with_parent == 1:

                temp_tree = self.left_tree
                self.left_tree = self.parent
                self.left_connection = 1

                self.left_tree.right_tree = temp_tree
                self.left_tree.right_connection = 0
                return True

        # Doorloop pad van de wortel naar een blad
        if self.root_key < newItem.key:
            self.left_tree.insert(newItem)
        elif self.root_key < newItem.key:
            self.left_tree.insert(newItem)

        # Eens aan dit punt geraakt, zou de node toegevoegd moeten zijn
        # Splits overvolle knopen op de terugweg van blad richting wortel
        # In een Rood-Zwart boom kan een knoop pas overvol zijn als:
        # Deze zelf 2 rode pointers bevat
        # En een van deze rode pointers nog een rode pointer bevat.

        # Als een van de twee verbindingen geen rode verbinding is,
        # Dan kan het geen overvolle boom meer zijn (dankzijn redestribute bij toevoegen knoop)
        if self.right_connection is None or self.left_connection is None:
            return True

        if self.right_connection == 1 and self.left_connection == 1:

            # To split or not to split, that is the question
            to_split = False

            # Left tree bestaat sowieso (anders zou de functie hierboven al verlaten zijn)
            # Dus is er ook een self.left_tree.left_connection. Deze verbinding zelf kan
            # wel None zijn, maar left_tree niet, dus dit zou geen error mogen geven.
            if self.left_tree.left_connection == 1:
                to_split = True
                self.left_tree.left_connection = 0

            elif self.left_tree.right_connection == 1:
                to_split = True
                self.left_tree.right_connection = 0

            elif self.right_tree.left_connection == 1:
                to_split = True
                self.right_tree.left_connection = 0

            elif self.right_tree.right_connection == 1:
                to_split = True
                self.right_tree.right_connection = 0

            if to_split:
                self.left_connection = 0
                self.right_connection = 0

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
pass