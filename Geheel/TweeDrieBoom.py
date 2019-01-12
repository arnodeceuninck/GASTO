class TweeDrieBoom:
    def __init__(self):
        self.root = []
        self.childrenLeft = None
        self.childrenRight = None
        self.childrenMiddle = None
        self.childrenMiddle2 = None #wordt gebruikt voor het splitsen van nodes als tijdelijk extra kind.
        self.parent = None

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        size = self.size()
        if size > self.index:
            x = self.getIndex(self.index)
            self.index += 1
            return (x[0].key, x[0].value)
        else:
            raise StopIteration

    def destroy23T(self):
        if self.childrenLeft == None:   #indien er geen linker kind
            if self.childrenMiddle != None: #Indien er een middel kind is bezoekt het die
                self.childrenMiddle.destroy23T()
            elif self.childrenRight != None: #bezoekt het rechterkind
                self.childrenRight.destroy23T()
            else:
                self.root.clear()   #verwijdert de TreeItems
                if self.parent == None and self.childrenLeft == self.childrenRight == self.childrenMiddle == None:
                    del self    #verwijdert de node
                elif self == self.parent.childrenLeft:
                    self.parent.childrenLeft = None #indien de node het linkerkind is wordt het linkerkind verwijdert uit de parent.
                    return self.parent.destroy23T()
                elif self == self.parent.childrenRight:
                    self.parent.childrenRight = None    #indien de node het rechterkind is wordt het rechterkind verwijdert uit de parent.
                    return self.parent.destroy23T()
                else:
                    self.parent.childrenMiddle = None
                    return self.parent.destroy23T() #indien de node het middelkind is wordt het middelkind verwijdert uit de parent.
        else:
            return self.childrenLeft.destroy23T()

    def isEmpty(self):
        if len(self.root) == 0 and self.childrenLeft == self.childrenMiddle == self.childrenRight == self.parent == None:
            return True #Geeft True terug indien de 23T leeg is.

    def insertItem(self, TreeItem):
        size = self.size()
        # if size > 0:
        #     check = self.zoek(TreeItem.key, False)  # checkt of het element in de 23T zit
        #     if check[0] == True:
        #         print("error")
        # #         return False
        if len(self.root) == 0 and self.parent == None:
            self.root.append(TreeItem)  #indien er nog geen elementen in de 23T zitten
        elif len(self.root) == 0:
            self.root.append(TreeItem)  #Voegt het element toe aan de node self.
            self.parent = self
        elif len(self.root) == 1:   #Als de huidige node 1 element bevat
            if self.childrenLeft != None and self.childrenRight != None:
                if TreeItem.key > self.root[0].key: #controleert of het TreeItem.key groter is dan het TreeItem.key in de node
                    self.childrenRight.insertItem(TreeItem) #bezoekt het rechterkind
                else:   #indien het TreeItem.key kleiner is dan het TreeIten.key in de node.
                    self.childrenLeft.insertItem(TreeItem)  #Bezoekt het linkerkind
            else:
                if TreeItem.key > self.root[0].key:
                    self.root.append(TreeItem)  #Voegt het element toe aan het blad
                else:
                    self.root.insert(0, TreeItem)   #voegt het element toe aan het blad
        elif len(self.root) == 2:   #indien de node uit 2 elementen bestaat
            if self.childrenLeft != None or self.childrenMiddle != None or self.childrenRight != None:
                if TreeItem.key > self.root[1].key:
                    self.childrenRight.insertItem(TreeItem) #Bezoekt het rechterkind indien het TreeItem groter is dan het 2de element in de node
                elif self.root[0].key < TreeItem.key < self.root[1].key:
                    self.childrenMiddle.insertItem(TreeItem)    #Bezoekt het middelste kind indien het TreeItem groter is dan het eerste TreeItem in de node maar kleiner dan de 2de.
                else:
                    self.childrenLeft.insertItem(TreeItem)  #Bezeoekt het linkerkind indien het TreeItem kleiner is dan het eerste element in de node.
            else:
                if TreeItem.key > self.root[1].key:
                    self.root.append(TreeItem)  #Voegt het element toe aan het blad
                    self.split()    #roept de spilts functie aan
                elif self.root[0].key < TreeItem.key < self.root[1].key:
                    self.root.insert(1, TreeItem)   #voegt het element toe aan het blad
                    self.split()    #roept de splits functie aan
                else:
                    self.root.insert(0, TreeItem)   #Voegt het element toe aan het blad
                    self.split()    #roept de splits functie aan

    def split(self):
        """
        Deze Functie splits de node met 3 elementen.
        Deze functie is recursief opgesteld en zal zichzelf blijven oproepen tot alles is verdeelt.
        """
        if self.parent == None: #Geval dat de root gesplitst wordt.
            #De uiterste elementen worden de kinderen.
            NodeLeft = TweeDrieBoom()
            NodeRight = TweeDrieBoom()
            NodeLeft.childrenLeft = self.childrenLeft
            self.childrenLeft = NodeLeft
            NodeRight.childrenRight = self.childrenRight
            self.childrenRight = NodeRight
            NodeLeft.parent = self
            NodeRight.parent = self
            NodeLeft.root.append(self.root[0])
            NodeRight.root.append(self.root[2])
            self.root.remove(self.root[0])
            self.root.remove(self.root[1])
            if self.childrenMiddle != None and self.childrenMiddle2 != None:    #bij het geval dat er een tijdelijk 4de kind is.
                NodeLeft.childrenRight = self.childrenMiddle2
                NodeRight.childrenLeft = self.childrenMiddle
                NodeLeft.childrenRight.parent = NodeLeft
                NodeLeft.childrenLeft.parent = NodeLeft
                NodeRight.childrenLeft.parent = NodeRight
                NodeRight.childrenRight.parent = NodeRight
                self.childrenMiddle = None
                self.childrenMiddle2 = None
        else:
            if len(self.parent.root) == 1:  #als de lengte van de parent 1 is.
                #uiterste elementen van de node worden de kinderen.
                NodeMiddle = TweeDrieBoom()
                self.parent.childrenMiddle = NodeMiddle
                NodeMiddle.parent = self.parent
                if self == self.parent.childrenLeft:    #bij geval dat de node het linkerkind is van de parent
                    self.parent.root.insert(0, self.root[1])
                    NodeMiddle.root.append(self.root[2])

                    self.root.remove(self.root[1])
                    self.root.remove(self.root[1])

                    if self.childrenMiddle2 != None:    #indien er een tijdelijke kind.
                        NodeMiddle.childrenLeft = self.childrenMiddle
                        NodeMiddle.childrenRight = self.childrenRight
                        NodeMiddle.childrenLeft.parent = NodeMiddle
                        NodeMiddle.childrenRight.parent = NodeMiddle
                        self.childrenRight = self.childrenMiddle2
                        self.childrenMiddle = None
                        self.childrenMiddle2 = None

                elif self == self.parent.childrenRight: #bij geval dat de node het rechterkind is van de parent
                    self.parent.root.append(self.root[1])
                    NodeMiddle.root.append(self.root[0])

                    self.root.remove(self.root[0])
                    self.root.remove(self.root[0])

                    if self.childrenMiddle2 != None:    #indien er een tijdelijke kind.
                        NodeMiddle.childrenLeft = self.childrenLeft
                        NodeMiddle.childrenRight = self.childrenMiddle2
                        NodeMiddle.childrenLeft.parent = NodeMiddle
                        NodeMiddle.childrenRight.parent = NodeMiddle
                        self.childrenLeft = self.childrenMiddle
                        self.childrenMiddle = None
                        self.childrenMiddle2 = None

            elif len(self.parent.root) == 2:    #indien de parent uit 2 elementen bestaat.
                NodeMiddle = TweeDrieBoom()
                if self == self.parent.childrenLeft:
                    self.parent.root.insert(0, self.root[1])
                    self.root.remove(self.root[1])
                    if self.childrenMiddle2 != None:    #indien er een tijdelijke kind.
                        NodeMiddle.root.append(self.root[1])

                        NodeMiddle.childrenLeft = self.childrenMiddle
                        NodeMiddle.childrenRight = self.childrenRight
                        NodeMiddle.childrenLeft.parent = NodeMiddle
                        NodeMiddle.childrenRight.parent = NodeMiddle
                        self.root.remove(self.root[1])
                        self.childrenMiddle = None
                        self.childrenRight = self.childrenMiddle2
                        self.childrenMiddle2 = None

                        NodeMiddle.parent = self.parent
                        self.parent.childrenMiddle2 = NodeMiddle
                        self.parent.split()
                    else:
                        NodeMiddle.root.append(self.root[1])
                        self.root.remove(self.root[1])
                        self.parent.childrenMiddle2 = NodeMiddle
                        NodeMiddle.parent = self.parent
                        self.parent.split()
                elif self == self.parent.childrenMiddle:
                    self.parent.root.insert(1, self.root[1])
                    self.root.remove(self.root[1])

                    if self.childrenMiddle2 != None:    #indien er een tijdelijke kind.
                        NodeMiddle.root.append(self.root[0])

                        NodeMiddle.childrenLeft = self.childrenLeft
                        NodeMiddle.childrenRight = self.childrenMiddle2
                        NodeMiddle.childrenLeft.parent = NodeMiddle
                        NodeMiddle.childrenRight.parent = NodeMiddle
                        self.root.remove(self.root[0])
                        self.childrenMiddle2 = None
                        self.childrenLeft = self.childrenMiddle
                        self.childrenMiddle = None

                        NodeMiddle.parent = self.parent
                        self.parent.childrenMiddle2 = NodeMiddle
                        self.parent.split()
                    else:
                        NodeMiddle.root.append(self.root[0])
                        self.root.remove(self.root[0])
                        self.parent.childrenMiddle2 = NodeMiddle
                        self.parent.split()
                else:
                    self.parent.root.append(self.root[1])
                    self.root.remove(self.root[1])

                    if self.childrenMiddle2 != None:    #indien er een tijdelijke kind.
                        NodeMiddle.root.append(self.root[0])

                        NodeMiddle.childrenLeft = self.childrenLeft
                        NodeMiddle.childrenRight = self.childrenMiddle2
                        NodeMiddle.childrenLeft.parent = NodeMiddle
                        NodeMiddle.childrenRight.parent = NodeMiddle
                        self.root.remove(self.root[0])
                        self.childrenMiddle2 = None
                        self.childrenLeft = self.childrenMiddle
                        self.childrenMiddle = None

                        NodeMiddle.parent = self.parent
                        self.parent.childrenMiddle2 = self.parent.childrenMiddle
                        self.parent.childrenMiddle = NodeMiddle
                        self.parent.split()
                    else:
                        NodeMiddle.root.append(self.root[0])
                        self.root.remove(self.root[0])
                        self.parent.childrenMiddle2 = self.parent.childrenMiddle
                        NodeMiddle.parent = self.parent
                        self.parent.childrenMiddle = NodeMiddle
                        self.parent.split()

    def delete(self, key):
        check = self.zoek(key, False)   #checkt of het element in de 23T zit
        if check[0] == False:
            return False
        Treeitem = None
        if key == self.root[0].key: #Zoekt het Treetem
            Treeitem = self.root[0]
        elif len(self.root) == 2 and self.root[1].key == key:
            Treeitem = self.root[1]
        if Treeitem != None:    #indien het TreeItem gevonden is
            if self.childrenLeft == None:
                self.root.remove(Treeitem)
                if self.parent == None and self.childrenLeft == None:
                    pass
                else:
                    self.fix()
            else:
                size = self.size()
                if 3 < size < 6 and self.parent == None and len(self.root) == 1:    #indien het aantal elementen kleiner dan 6 is maar groter dan 5 is, er moet geen fix functie aangeroepen worden.
                    self.root.clear()
                    if len(self.childrenLeft.root) == 2:
                        self.root.append(self.childrenLeft.root[1])
                        self.childrenLeft.root.remove(self.childrenLeft.root[1])
                    elif len(self.childrenRight.root) == 2:
                        self.root.append(self.childrenRight.root[0])
                        self.childrenRight.root.remove(self.childrenRight.root[0])
                else:
                    successor = self.inorder_successor(Treeitem)    #Zoekt inordersuccessor indien het element niet in een blad zit.
                    if len(self.root) == 1: #node bestaat uit 1 element
                        self.root.clear()   #wisselt het element in de node met de successor
                        self.root.append(successor.root[0])
                        successor.root.remove(successor.root[0])    #verwijdert het verplaatste element uit het blad
                        successor.fix() #fix functie wordt aangeroepen
                    else:   #node bestaat uit 2 elementen
                        if self.root[0] == Treeitem:    #eerste element van de node
                            self.root.insert(0, successor.root[0])
                        else:   #2de element van de node
                            self.root.append(successor.root[0])
                        self.root.remove(Treeitem)  #wisselt het element met de successor
                        successor.root.remove(successor.root[0])    #verwijdert het verplaatste element uit het blad
                        successor.fix() #roept fix functie aan
        else:
            if key < self.root[0].key:  #indien de key kleiner is dan het eerste element van de node
                self.childrenLeft.delete(key)   #linkerkind wordt bezocht
            else:
                if len(self.root) == 1: #1 element in de node
                    self.childrenRight.delete(key)  #rechterkind wordt bezocht
                else:
                    if key < self.root[1].key:  #indien de key kleiner is dan het 2de kind
                        self.childrenMiddle.delete(key) #middelste kind wordt bezocht
                    else:   #indien de key groter is dan het 2de element
                        self.childrenRight.delete(key)  #rechterkind wordt bezocht

    def fix(self):
        if len(self.root) == 0: #indien de node leeg is
            if self.parent == None: #indien de node de root is
                self.root = self.childrenMiddle.root
                self.childrenLeft = self.childrenMiddle.childrenLeft
                self.childrenRight = self.childrenMiddle.childrenRight
                self.childrenMiddle = self.childrenMiddle.childrenMiddle
                if self.childrenLeft != None or self.childrenMiddle != None:
                    self.childrenLeft.parent = self
                    self.childrenMiddle.parent = self
                    self.childrenRight.parent = self
            elif self.childrenMiddle != None:   #als er een middelste kind is.
                nodemiddle = TweeDrieBoom() #maak een nieuwe node aan
                nodemiddle.parent = self.parent
                if self == self.parent.childrenLeft:    #als de node het linkerkind is van de parent
                    nodemiddle.root.append(self.parent.root[0])
                    if len(self.parent.root) == 1:  #als de parent uit 1 element bestaat
                        nodemiddle.root.append(self.parent.childrenRight.root[0])
                        nodemiddle.childrenLeft = self.childrenMiddle
                        nodemiddle.childrenMiddle = self.parent.childrenRight.childrenLeft
                        nodemiddle.childrenRight = self.parent.childrenRight.childrenRight
                        self.childrenMiddle.parent = nodemiddle
                        self.parent.childrenRight.childrenLeft.parent = nodemiddle
                        self.parent.childrenRight.childrenRight.parent = nodemiddle
                        self.parent.root.clear()
                        self.parent.childrenMiddle = nodemiddle
                        self.parent.childrenLeft = None
                        self.parent.childrenRight = None
                    else:   #als de parent uit 2 elementen bestaat
                        nodemiddle.root.append(self.parent.childrenMiddle.root[0])
                        self.parent.root.remove(self.parent.root[0])
                        nodemiddle.childrenLeft = self.childrenMiddle
                        nodemiddle.childrenMiddle = self.parent.childrenMiddle.childrenLeft
                        nodemiddle.childrenRight = self.parent.childrenMiddle.childrenRight
                        self.childrenMiddle.parent = nodemiddle
                        self.parent.childrenMiddle.childrenLeft.parent = nodemiddle
                        self.parent.childrenMiddle.childrenRight.parent = nodemiddle
                        self.parent.childrenMiddle = None
                        self.parent.childrenLeft = nodemiddle
                elif self == self.parent.childrenRight: #als de node het rechterkind is van de parent
                    if len(self.parent.root) == 1:  #als de parent uit 1 element bestaat
                        nodemiddle.root.append(self.parent.root[0])
                        nodemiddle.root.insert(0, self.parent.childrenLeft.root[0])
                        nodemiddle.childrenLeft = self.parent.childrenLeft.childrenLeft
                        nodemiddle.childrenMiddle = self.parent.childrenLeft.childrenRight
                        nodemiddle.childrenRight = self.childrenMiddle
                        self.childrenMiddle.parent = nodemiddle
                        self.parent.childrenRight.childrenLeft.parent = nodemiddle
                        self.parent.childrenRight.childrenRight.parent = nodemiddle
                        self.parent.root.clear()
                        self.parent.childrenMiddle = nodemiddle
                        self.parent.childrenLeft = None
                        self.parent.childrenRight = None
                    else:   #als de parent uit 2 elementen bestaat
                        nodemiddle.root.append(self.parent.root[1])
                        nodemiddle.root.insert(0, self.parent.childrenMiddle.root[0])
                        self.parent.root.remove(self.parent.root[1])
                        nodemiddle.childrenLeft = self.parent.childrenMiddle.childrenLeft
                        nodemiddle.childrenMiddle = self.parent.childrenMiddle.childrenRight
                        nodemiddle.childrenRight = self.childrenMiddle
                        self.childrenMiddle.parent = nodemiddle
                        self.parent.childrenMiddle.childrenLeft.parent = nodemiddle
                        self.parent.childrenMiddle.childrenRight.parent = nodemiddle
                        self.parent.childrenMiddle = None
                        self.parent.childrenRight = nodemiddle
                else:   #als de node het middelste kind is van de parent
                    if len(self.parent.childrenLeft.root) == 2 or len(self.parent.childrenRight.root) == 2: #als het linkerkind of het rechterkind van de parent uit 2 elementen bestaat
                        if len(self.parent.childrenLeft.root) == 2: #linkerkind van de parent bestaat uit 2 elementen
                            self.root.append(self.parent.root[0])
                            self.parent.root.remove(self.parent.root[0])
                            self.parent.root.insert(0, self.parent.childrenLeft.root[1])
                            self.parent.childrenLeft.root.remove(self.parent.childrenLeft.root[1])
                            self.childrenRight = self.childrenMiddle
                            self.childrenMiddle = None
                            self.childrenLeft = self.parent.childrenLeft.childrenRight
                            self.childrenLeft.parent = self
                            self.parent.childrenLeft.childrenRight = self.parent.childrenLeft.childrenMiddle
                            self.parent.childrenLeft.childrenMiddle = None
                        else:   #rechterkind bestaat uit 2 elementen
                            self.root.append(self.parent.root[1])
                            self.parent.root.remove(self.parent.root[1])
                            self.parent.root.append(self.parent.childrenRight.root[0])
                            self.parent.childrenRight.root.remove(self.parent.childrenRight.root[0])
                            self.childrenLeft = self.childrenMiddle
                            self.childrenMiddle = None
                            self.childrenRight = self.parent.childrenRight.childrenLeft
                            self.childrenRight.parent = self
                            self.parent.childrenRight.childrenLeft = self.parent.childrenRight.childrenMiddle
                            self.parent.childrenRight.childrenMiddle = None
                    else:   #indien het linker- en rechterkind van de parent uit 1 element bestaan
                        nodemiddle.root.append(self.parent.childrenLeft.root[0])
                        nodemiddle.root.append(self.parent.root[0])
                        self.parent.root.remove(self.parent.root[0])
                        nodemiddle.childrenLeft = self.parent.childrenLeft.childrenLeft
                        nodemiddle.childrenMiddle = self.parent.childrenLeft.childrenRight
                        nodemiddle.childrenRight = self.childrenMiddle
                        nodemiddle.childrenLeft.parent = nodemiddle
                        nodemiddle.childrenMiddle.parent = nodemiddle
                        nodemiddle.childrenRight.parent = nodemiddle
                        self.parent.childrenMiddle = None
                        self.parent.childrenLeft = nodemiddle
                self.parent.fix()

            else:   #base case fix
                if self == self.parent.childrenLeft and len(self.parent.childrenRight.root) == 2 and len(self.parent.root) == 1:
                    self.root.append(self.parent.root[0])
                    self.parent.root.clear()
                    self.parent.root.append(self.parent.childrenRight.root[0])
                    self.parent.childrenRight.root.remove(self.parent.childrenRight.root[0])
                elif self == self.parent.childrenRight and len(self.parent.childrenLeft.root) == 2 and len(self.parent.root) == 1:
                    self.root.append(self.parent.root[0])
                    self.parent.root.clear()
                    self.parent.root.append(self.parent.childrenLeft.root[1])
                    self.parent.childrenLeft.root.remove(self.parent.childrenLeft.root[1])
                elif self == self.parent.childrenLeft and self.parent.childrenMiddle != None and (len(self.parent.childrenRight.root) == 2 or len(self.parent.childrenMiddle.root) == 2) and len(self.parent.root) == 2:
                    if len(self.parent.childrenRight.root) == 2:
                        self.root.append(self.parent.root[0])
                        self.parent.childrenMiddle.root.append(self.parent.root[1])
                        self.parent.root.clear()
                        self.parent.root.append(self.parent.childrenMiddle.root[0])
                        self.parent.root.append(self.parent.childrenRight.root[0])
                        self.parent.childrenRight.root.remove(self.parent.childrenRight.root[0])
                        self.parent.childrenMiddle.root.remove(self.parent.childrenMiddle.root[0])
                    else:
                        self.root.append(self.parent.root[0])
                        self.parent.root.remove(self.parent.root[0])
                        self.parent.root.insert(0, self.parent.childrenMiddle.root[0])
                        self.parent.childrenMiddle.root.remove(self.parent.childrenMiddle.root[0])
                elif self == self.parent.childrenRight and self.parent.childrenMiddle != None and (len(self.parent.childrenLeft.root) == 2 or len(self.parent.childrenMiddle.root) == 2)and len(self.parent.root) == 2:
                    if len(self.parent.childrenLeft.root) == 2:
                        self.root.append(self.parent.root[1])
                        self.parent.childrenMiddle.root.append(self.parent.root[0])
                        self.parent.root.clear()
                        self.parent.root.append(self.parent.childrenLeft.root[1])
                        self.parent.root.append(self.parent.childrenMiddle.root[0])
                        self.parent.childrenRight.root.remove(self.parent.childrenLeft.root[1])
                        self.parent.childrenMiddle.root.remove(self.parent.childrenMiddle.root[0])
                    else:
                        self.root.append(self.parent.root[1])
                        self.parent.root.remove(self.parent.root[1])
                        self.parent.root.append(self.parent.childrenMiddle.root[1])
                        self.parent.childrenMiddle.root.remove(self.parent.childrenMiddle.root[1])
                elif self == self.parent.childrenMiddle and (len(self.parent.childrenLeft.root) == 2 or len(self.parent.childrenRight.root) == 2) and len(self.parent.root) == 2:
                    if len(self.parent.childrenRight.root) == 2:
                        self.root.append(self.parent.root[0])
                        self.parent.root.remove(self.parent.root[0])
                        self.parent.root.insert(0, self.parent.childrenLeft.root[1])
                        self.parent.childrenLeft.root.remove(self.parent.childrenLeft.root[1])
                    if len(self.parent.childrenLeft.root) == 2:
                        self.root.append(self.parent.root[1])
                        self.parent.root.remove(self.parent.root[1])
                        self.parent.root.insert(0, self.parent.childrenRight.root[0])
                        self.parent.childrenRight.root.remove(self.parent.childrenRight.root[0])
                else:
                    nodemiddle = TweeDrieBoom()
                    nodemiddle.parent = self.parent
                    if self == self.parent.childrenLeft:    #indien de node het linkerkind is van de parent
                        if len(self.parent.root) == 2:  #indien de parent uit 2 elementen bestaat
                            self.root.append(self.parent.root[0])
                            self.root.append(self.parent.childrenMiddle.root[0])
                            self.parent.root.remove(self.parent.root[0])
                            self.parent.childrenMiddle.root.clear()
                            self.parent.childrenMiddle = None
                        else:   #indien de parent uit 1 element bestaat
                            nodemiddle.root.append(self.parent.root[0])
                            nodemiddle.root.append(self.parent.childrenRight.root[0])
                            self.parent.root.clear()
                            self.parent.childrenMiddle = nodemiddle
                            self.parent.childrenLeft = None
                            self.parent.childrenRight = None
                    elif self == self.parent.childrenMiddle and len(self.parent.root) == 2: #indien de node het middelste kind is van de parent en de parent uit 2 elementen bestaat
                        self.parent.childrenLeft.root.append(self.parent.root[0])
                        self.parent.root.remove(self.parent.root[0])
                        self.parent.childrenMiddle = None
                    else: #indien de node het rechterkind is van de parent
                        if len(self.parent.root) == 2:  #indien de parent uit 2 elementen bestaat
                            self.root.append(self.parent.childrenMiddle.root[0])
                            self.root.append(self.parent.root[1])
                            self.parent.root.remove(self.parent.root[1])
                            self.parent.childrenMiddle.root.clear()
                            self.parent.childrenMiddle = None
                        else:   #indien de parent uit 1 element bestaat
                            self.parent.root.insert(0, self.parent.childrenLeft.root[0])
                            self.parent.childrenLeft = None
                            self.parent.childrenRight = None
                    self.parent.fix()
        else:   #indien er nog elementen in de node zitten
            pass

    def inorder_successor(self, TreeItem):  #Zoekt inorder successor
        if len(self.root) == 1:
            successor = self.childrenRight.LeftElement()
            return successor
        else:
            if TreeItem == self.root[0]:
                successor = self.childrenMiddle.LeftElement()
                return successor
            else:
                successor = self.childrenRight.LeftElement()
                return successor

    def LeftElement(self):  #bezoekt telkens het linkerkind.
        node = self
        while(node.childrenLeft != None):
            node = node.childrenLeft
        return node

    def zoek(self, key, gevonden):  #Zoekt een TreeItem op basis van een key
        if len(self.root) == 1 and self.childrenLeft == self.childrenRight == None and self.root[0].key != key:
            result = (gevonden, None)
            return result
        elif len(self.root) == 2 and self.childrenLeft == self.childrenRight == self.childrenMiddle == None and self.root[0].key != key and self.root[1].key != key:
            result = (gevonden, None)
            return result
        if key == self.root[0].key:
            gevonden = True
            result = (gevonden, self.root[0])
            return result
        elif len(self.root) == 2 and self.root[1].key:
            gevonden = True
            result = (gevonden, self.root[1])
            return result
        elif key < self.root[0].key:
            return self.childrenLeft.zoek(key, gevonden)
        else:
            if len(self.root) == 1:
                return self.childrenRight.zoek(key, gevonden)
            else:
                if key < self.root[1].key:
                    return self.childrenMiddle.zoek(key, gevonden)
                else:
                    return self.childrenRight.zoek(key, gevonden)

    def retrieve(self, key):    #Zoekt een Treeitem op basis van een key en geeft een tuple terug met True of False als het niet gevonden is en geeft het TreeItem terug.
        result = self.zoek(key, False)
        if result[0] == False:
            return False
        else:
            return result

    def traverse(self, visit, key=None):    #Doorloopt de 23T
        return self.inorderTraverse(visit, key)

    def inorderTraverse(self, visit, key=None): #Voert een inorderTraverse uit op de 23T
        if self.childrenLeft != None:
            self.childrenLeft.inorderTraverse(visit, key)
        if len(self.root) >= 1:
            visit(self.root[0].value, key)
        if self.childrenMiddle != None:
            self.childrenMiddle.inorderTraverse(visit, key)
        if len(self.root) == 2:
            visit(self.root[1].value, key)
        if self.childrenRight != None:
            self.childrenRight.inorderTraverse(visit, key)

    def getIndex(self, index):
        temp = index
        if len(self.root) >= 1:
            temp = index - 1
        if len(self.root) == 2:
            temp -= 1
        if index == 0 and len(self.root) >= 1:
            return (self.root[0], index)
        if index == 1 and len(self.root) == 2:
            return (self.root[1], index)
        index = temp
        if self.childrenLeft != None:
            returned = self.childrenLeft.getIndex(index)
            index = returned[1]
            if returned[0] != None:
                return returned
        if self.childrenMiddle != None:
            returned = self.childrenMiddle.getIndex(index)
            index = returned[1]
            if returned[0] != None:
                return returned
        if self.childrenRight != None:
            returned = self.childrenRight.getIndex(index)
            index = returned[1]
            if returned[0] != None:
                return returned
        return (None, index)

    def size(self): #Geeft het aantal elementen in de 23T terug
        size = 0
        if len(self.root) == 1:
            size = 1
        elif len(self.root) == 2:
            size = 2
        if self.childrenLeft != None:
            size += self.childrenLeft.size()
        if self.childrenMiddle != None:
            size += self.childrenMiddle.size()
        if self.childrenRight != None:
            size += self.childrenRight.size()
        return size


    def print(self, filename):
        return write_dot(filename, self)


class TreeItem(object):
    def __init__(self, value, key):
        self.key = key
        self.value = value


def dot(current, parent, file): #gaat inordertraverse de dotfile opstellen

    if current.parent != None:
        if len(current.root) == 1:
            if len(parent.root) > 1:
                parentKeys = ""
                for keyNode in parent.root:
                    parentKeys += str(keyNode.key)
                    parentKeys += "|"
                parentKeys = parentKeys[:-1]
                file.write("\t\""+str(parentKeys) + "\" -> \"" + str(current.root[0].key) + "\";\n")
            else:
                file.write("\t\""+str(parent.root[0].key) + "\" -> \"" + str(current.root[0].key) + "\";\n")
        elif len(parent.root) > 1:
            parentKeys = ""
            currentKeys = ""
            for keyNode in parent.root:
                parentKeys += str(keyNode.key)
                parentKeys += "|"
            parentKeys = parentKeys[:-1]
            for keyNode in current.root:
                currentKeys += str(keyNode.key)
                currentKeys += "|"
            currentKeys = currentKeys[:-1]
            file.write("\t\""+str(parentKeys) + "\" -> \"" + str(currentKeys) + "\";\n")
        else:
            currentKeys = ""
            for keyNode in current.root:
                currentKeys += str(keyNode.key)
                currentKeys += "|"
            currentKeys = currentKeys[:-1]
            file.write("\t\""+str(parent.root[0].key) + "\" -> \"" + str(currentKeys) + "\";\n")

    if current.childrenLeft != None:
        dot(current.childrenLeft, current, file)

    if current.childrenMiddle != None:
        dot(current.childrenMiddle, current, file)

    if current.childrenRight != None:
        dot(current.childrenRight, current, file)


def write_dot(file, tree):  #maakt een dot file van de 23T.
    dotFile = open(file, "w")
    dotFile.write("digraph Two_Three_Tree { \n")
    dotFile.write("\t"+"size=8.5\n")
    if tree.childrenRight == None and len(tree.root) >= 1:
        current = ""
        current += str(tree.root[0].key)
        if len(tree.root) == 1:
            dotFile.write("\t\"" + current + "\";\n")
        else:
            current += "|"
            current += str(tree.root[1].key)
            dotFile.write("\t\"" + current + "\";\n")
    elif tree.childrenLeft != None:
        global globalCounter
        dot(tree, tree.parent, dotFile)
    dotFile.write("}")


def create23T():    #maakt een 23T aan.
    return TweeDrieBoom()

test = create23T()
test.insertItem(TreeItem(1, 1))
test.insertItem(TreeItem(1, 2))
test.insertItem(TreeItem(1, 3))
test.insertItem(TreeItem(1, 4))
test.insertItem(TreeItem(1, 5))
test.insertItem(TreeItem(1, 6))
test.insertItem(TreeItem(1, 7))
test.insertItem(TreeItem(1, 8))
test.insertItem(TreeItem(1, 9))
test.insertItem(TreeItem(1, 10))
test.insertItem(TreeItem(1, 11))
test.insertItem(TreeItem(1, 12))
test.insertItem(TreeItem(1, 13))
test.insertItem(TreeItem(1, 14))
test.insertItem(TreeItem(1, 15))
test.insertItem(TreeItem(1, 16))
print(test.size())


