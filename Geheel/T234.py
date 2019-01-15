
class TreeItem:
    def __init__(self, item, key):
        self.item = item                    #Deze classe word gebruikt om items te inserten in de 234T
        self.key = key


class T234:
    def __init__(self, item1, item2, item3, left, mleft, mright, right, parent):
        self.parent = parent                #Deze parent zal terug linken naar de parent van een node
        self.item1 = item1                  #De items komen overeen met alle items die een node kan hebben
        self.item2 = item2
        self.item3 = item3
        self.left = left                    #De volgende pointers komen overeen met de kinderen van de node
        self.mleft = mleft
        self.mright = mright
        self.right = right

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        size = self.size()
        if size > self.index:
            x = self.getIndex(self.index)
            self.index += 1
            return (x[0].key, x[0].item)
        else:
            raise StopIteration

    def change(self):
        while self.parent is not None:
            self = self.parent

    def isEmpty(self):
        if self.item1 is None and self.item2 is None and self.item3 is None and self.left is None and self.parent is None:
            return True                 #als de boom geen items, kinderen en parent heeft returned de functie true
        return False

    def destroyNode(self):
        self.left = None                #Deze functie zal een node verwijderen door al zijn pointers op None te zetten
        self.mleft = None
        self.mright = None
        self.right = None
        self.item1 = None
        self.item2 = None
        self.item3 = None
        self.parent = None

    def split(self):            #Deze functie zal een 4node opslitsen om de gebalanceerde structuur te behouden
        if self.parent is None: #als we in de root zitten
            if self.left is None:#als de root geen kinderen heeft
                self.left = T234(self.item1, None, None, None, None, None, None, self)      #een nieuwe node word aangemaakt als linker kind
                self.mleft = T234(self.item3, None, None, None, None, None, None, self)     #een nieuwe node word aangemaakt als mlinker kind
                self.item1 = self.item2     # het item dat op de 2de locatie stond word opgeschoven naar de juiste locatie
                self.item2 = None
                self.item3 = None           # De items die nu naar de kinderen zijn vershoven worden op none gezet
                return True         # de root is nu in het midden gesplit en heeft 2 kinderen
            else: #als de root wel kinderen heeft
                self.left.parent = None     #de parent van de kinderen worden allemaal op None gezet
                self.mleft.parent = None
                self.mright.parent = None
                self.right.parent = None
                self.left = T234(self.item1, None, None, self.left, self.mleft, None, None, self)       #er worden nieuwe kinderen aangemaakt met de vorige kinderen van de root
                self.mleft = T234(self.item3, None, None, self.mright, self.right, None, None, self)
                self.left.left.parent = self.left           # De parent pointers worden gereset
                self.left.mleft.parent = self.left
                self.mleft.left.parent = self.mleft
                self.mleft.mleft.parent = self.mleft
                self.item1 = self.item2
                self.item2 = None       #De items worden op de juiste plek gezet
                self.item3 = None
                self.mright = None
                self.right = None
                return True
        else: #als we niet de root zitten
            if self.parent.mright is None: #als de parent maar 2 kinderen heeft
                if self.parent.left == self: #als we het over het linker kind hebben
                    self.parent.item2 = self.parent.item1       #We schuiven het eerste item naar rechts
                    self.parent.item1 = self.item2      #we halen het middelste item uit de node en zetten het bij de parent node
                    self.parent.mright = self.parent.mleft      #we schuiven de kindere op
                    if self.left is not None:#als we kinderen hebben
                        self.parent.mleft = T234(self.item3, None, None, self.mright, self.right, None, None, self.parent)  #we maken een nieuwe kind aan de parent met de kinderen van de node
                        self.mright.parent = self.parent.mleft      #we passen de parent pointers aan
                        self.right.parent = self.parent.mleft
                        self.mright = None  #we zetten de verplaatste elementen op None
                        self.right = None
                        self.item3 = None
                        self.item2 = None
                        return True
                    else: #als de node geen kinderen heeft
                        self.parent.mleft = T234(self.item3, None, None, None, None, None, None, self.parent)      #We maken een nieuw kind aan
                        self.item3 = None #we zetten de gebruikte items op None
                        self.item2 = None
                        return True
                else: #als we over het rechterkind(mleft) hebben
                    self.parent.item2 = self.item2      # We brengen het middelste item naar de parent
                    self.parent.mright = self
                    if self.left is not None: #als de node kinderen heeft
                        self.parent.mleft = T234(self.item1, None, None, self.left, self.mleft, None, None, self.parent)    #We maken een nieuwe kind aan met de kindere van de node
                        self.left.parent = self.parent.mleft    #we zetten de parent pointers juist
                        self.mleft.parent = self.parent.mleft
                        self.left = self.mright         #we zetten de kinderen op de juiste plek
                        self.mleft = self.right
                        self.mright = None      # we reset de verplaatste items
                        self.right = None
                        self.item1 = self.item3
                        self.item2 = None
                        self.item3 = None
                        return True
                    else: # als de node wel kinderen heeft
                        self.parent.mleft = T234(self.item1, None, None, None, None, None, None, self.parent) #we maken nieuwe kinderen aan
                        self.item1 = self.item3
                        self.item2 = None
                        self.item3 = None
                        return True
            else: #als de parent 3 kinderen heeft
                if self.parent.left == self: #als we het linker kind zijn
                    self.parent.item3 = self.parent.item2   #We schuiven de items op
                    self.parent.item2 = self.parent.item1
                    self.parent.item1 = self.item2
                    self.parent.right = self.parent.mright  #we schuiven de kinderen op
                    self.parent.mright = self.parent.mleft
                    if self.left is not None: #als de node kinderen heeft
                        self.parent.mleft = T234(self.item3, None, None, self.mright, self.right, None, None, self.parent)  #we maken een nieuw kind aan de met de kinderen van de node
                        self.mright.parent = self.parent.mleft      #we zetten de parent pointers juist
                        self.right.parent = self.parent.mleft
                        self.item3 = None   # we passen de verschoven pointers aan
                        self.item2 = None
                        self.mright = None
                        self.right = None
                        return True
                    else: #als we geen kinderen hebben
                        self.parent.mleft = T234(self.item3, None, None, None, None, None, None,  #we maken een nieuw kind aan
                                                  self.parent)
                        self.item3 = None       #we passen de pointers aan
                        self.item2 = None
                        return True

                elif self.parent.mleft == self: #als we het middel kind zijn
                    self.parent.item3 = self.parent.item2       # we brengen het middelste item naar de parent
                    self.parent.item2 = self.item2
                    self.parent.right = self.parent.mright
                    if self.left is not None: # als we kinderen hebben
                        self.parent.mright = T234(self.item3, None, None, self.mright, self.right, None, None, self.parent) #we maken een nieuw kind aan
                        self.mright.parent = self.parent.mright #we passen de parent pointers aan
                        self.right.parent = self.parent.mright
                        self.item3 = None   #we resetten de ver plaatste items
                        self.item2 = None
                        self.mright = None
                        self.right = None
                        return True
                    else: # als we geen kinderen hebben
                        self.parent.mright = T234(self.item3, None, None, None, None, None, None,   #we maken een nieuw kind aan
                                                   self.parent)
                        self.item3 = None #we resseten de items
                        self.item2 = None
                        return True
                else: #als we het rechter kind zijn
                    self.parent.item3 = self.item2 # we brengen het middelste item naar de parent
                    self.parent.right = self
                    if self.left is not None: # als we kinderen hebben
                        self.parent.mright = T234(self.item1, None, None, self.left, self.mleft, None, None, #we maken een nieuw kind aan
                                                   self.parent)
                        self.item1 = self.item3 #we veplaatsen de items
                        self.item2 = None
                        self.item3 = None
                        self.left.parent = self.parent.mright   # we passen de parent pointers aan
                        self.mleft.parent = self.parent.mright
                        self.left = self.mright     # we passen de kinderen aan
                        self.mleft = self.right
                        self.mright = None
                        self.right = None
                        return True
                    else: #als we wel kinderen hebben
                        self.parent.mright = T234(self.item1, None, None, None, None, None, None, #we maken een nieuw kind aan
                                                   self.parent)
                        self.item1 = self.item3     # we passen de items van de node aan
                        self.item2 = None
                        self.item3 = None
                        return True


    def T234Insert(self, treeitem):
        if self.isEmpty():
            self.item1 = treeitem
            return True
        if self.item1 is not None and self.item2 is not None and self.item3 is not None:
            self.split()
            if self.parent is not None:
                self = self.parent
        if self.left is None:
            if self.item2 is not None:
                if treeitem.key < self.item1.key:
                    self.item3 = self.item2
                    self.item2 = self.item1
                    self.item1 = treeitem
                    return True
                elif treeitem.key < self.item2.key:
                    self.item3 = self.item2
                    self.item2 = treeitem
                    return True
                else:
                    self.item3 = treeitem
                    return True
            else:
                if treeitem.key < self.item1.key:
                    self.item2 = self.item1
                    self.item1 = treeitem
                    return True
                else:
                    self.item2 = treeitem
                    return True
        elif treeitem.key < self.item1.key:
            self.left.T234Insert(treeitem)
        elif self.item2 is None or treeitem.key > self.item1.key and treeitem.key < self.item2.key:
            self.mleft.T234Insert(treeitem)
        elif self.item3 is None or treeitem.key > self.item2.key and treeitem.key < self.item3.key:
            self.mright.T234Insert(treeitem)
        elif treeitem.key > self.item3.key:
            self.right.T234Insert(treeitem)

    def inorder1(self):
        target = self.mleft
        while target.left is not None:
            target = target.left
        return target

    def inorder2(self):
        target = self.mright
        while target.left is not None:
            target = target.left
        return target

    def inorder3(self):
        target = self.right
        while target.left is not None:
            target = target.left
        return target

    def redistributeleft(self):
        self.item1 = self.parent.item1
        self.parent.item1 = self.parent.mleft.item1
        self.parent.mleft.item1 = self.parent.mleft.item2
        self.parent.mleft.item2 = None
        if self.parent.mleft.item3 is not None:
            self.parent.mleft.item2 = self.parent.mleft.item3
            self.parent.mleft.item3 = None

    def redistributeright(self):
        self.item1 = self.parent.item3
        if self.parent.mright.item3 is None:
            self.parent.item3 = self.parent.mright.item2
            self.parent.mright.item2 = None
        else:
            self.parent.item3 = self.parent.mright.item3
            self.parent.mright.item3 = None

    def redistributemleft(self, sibling):
        if sibling == self.parent.left:
            self.item1 = self.parent.item1
            if self.parent.left.item3 is None:
                self.parent.item1 = self.parent.left.item2
                self.parent.left.item2 = None
            else:
                self.parent.item1 = self.parent.left.item3
                self.parent.left.item3 = None
        else:
            self.item1 = self.parent.item2
            if self.parent.mright.item3 is None:
                self.parent.item2 = self.parent.mright.item1
                self.parent.mright.item1 = self.parent.mright.item2
                self.parent.mright.item2 = None
            else:
                self.parent.item2 = self.parent.mright.item1
                self.parent.mright.item1 =self.parent.mright.item2
                self.parent.mright.item2 = self.parent.mright.item3
                self.parent.mright.item3 = None

    def redistributemright(self, sibling):
        if sibling == self.parent.mleft:
            self.item1 = self.parent.item2
            if self.parent.mleft.item3 is None:
                self.parent.item2 = self.parent.mleft.item2
                self.parent.mleft.item2 = None
            else:
                self.parent.item2 = self.parent.mleft.item3
                self.parent.mleft.item3 = None
        else:
            self.item1 = self.parent.item3
            if self.parent.right.item3 is None:
                self.parent.item3 = self.parent.right.item1
                self.parent.right.item1 = self.parent.right.item2
                self.parent.right.item2 = None
            else:
                self.parent.item3 = self.parent.right.item1
                self.parent.right.item1 = self.parent.right.item2
                self.parent.right.item2 = self.parent.right.item3
                self.parent.mright.item3 = None

    def redistributeInternalleft(self):
        self.item1 = self.parent.item1
        self.parent.item1 = self.parent.mleft.item1
        self.parent.mleft.item1 = self.parent.mleft.item2
        self.mleft = self.parent.mleft.left
        self.parent.mleft.left.parent = self
        self.parent.mleft.left = self.parent.mleft.mleft
        self.parent.mleft.mleft = self.parent.mleft.mright
        if self.parent.mleft.item3 is None:
            self.parent.mleft.item2 = None
            self.parent.mleft.mright = None
        else:
            self.parent.mleft.item2 = self.parent.mleft.item3
            self.parent.mleft.item3 = None
            self.parent.mleft.mright = self.parent.mleft.right
            self.parent.mleft.right = None

    def redistributeInternalmleft(self, sibling):
        if sibling == self.parent.left:
            self.item1 = self.parent.item1
            self.mleft = self.left
            if self.parent.left.item3 is None:
                self.parent.item1 = self.parent.left.item2
                self.parent.left.item2 = None
                self.left = self.parent.left.mright
                self.parent.left.mright.parent = self
                self.parent.left.mright = None
            else:
                self.parent.item1 = self.parent.left.item3
                self.parent.left.item3 = None
                self.left = self.parent.left.right
                self.parent.left.right.parent = self
                self.parent.left.right = None
        else:
            self.item1 = self.parent.item2
            self.parent.item2 = self.parent.mright.item1
            self.parent.mright.item1 = self.parent.mright.item2
            self.mleft = self.parent.mright.left
            self.parent.mright.left.parent = self
            self.parent.mright.left = self.parent.mright.mleft
            self.parent.mright.mleft = self.parent.mright.mright
            if self.parent.mright.item3 is None:
                self.parent.mright.item2 = None
                self.parent.mright.mright = None
            else:
                self.parent.mright.item2 = self.parent.mright.item3
                self.parent.mright.item3 = None
                self.parent.mright.mright = self.parent.mright.right
                self.parent.mright.right = None

    def redistributeInternalmright(self, sibling):
        if sibling == self.parent.mleft:
            self.item1 = self.parent.item2
            self.mleft = self.left
            if self.parent.mleft.item3 is None:
                self.parent.item1 = self.parent.mleft.item2
                self.parent.mleft.item2 = None
                self.left = self.parent.mleft.mright
                self.parent.mleft.mright.parent = self
                self.parent.mleft.mright = None
            else:
                self.parent.item1 = self.parent.mleft.item3
                self.parent.mleft.item3 = None
                self.left = self.parent.mleft.right
                self.parent.mleft.right.parent = self
                self.parent.mleft.right = None
        else:
            self.item1 = self.parent.item3
            self.parent.item1 = self.parent.right.item1
            self.parent.right.item1 = self.parent.right.item2
            self.mleft = self.parent.right.left
            self.parent.right.left.parent = self
            self.parent.right.left = self.parent.right.mleft
            self.parent.right.mleft = self.parent.right.mright
            if self.parent.right.item3 is None:
                self.parent.right.item2 = None
                self.parent.right.mright = None
            else:
                self.parent.right.item2 = self.parent.right.item3
                self.parent.right.item3 = None
                self.parent.right.mright = self.parent.right.right
                self.parent.right.right = None

    def redistributeInternalright(self):
        self.item1 = self.parent.item3
        self.mleft = self.left
        if self.parent.mright.item3 is None:
            self.parent.item3 = self.parent.mright.item2
            self.parent.mright.item2 = None
            self.left = self.parent.mright.mright
            self.parent.mright.mright.parent = self
            self.parent.mright.mright = None
        else:
            self.parent.item3 = self.parent.mright.item3
            self.parent.mright.item3 = None
            self.left = self.parent.mright.right
            self.parent.mright.right.parent = self
            self.parent.mright.right = None

    def mergeitemleft(self):
        self.parent.mleft.item2 = self.parent.mleft.item1
        self.parent.mleft.item1 = self.parent.item1
        self.parent.item1 = None
        self.parent.left = self.parent.mleft
        self.parent.mleft = None
        if self.parent.item2 is not None:
            self.parent.item1 = self.parent.item2
            self.parent.item2 = None
            self.parent.mleft = self.parent.mright
            self.parent.mright = None
        if self.parent.item3 is not None:
            self.parent.item2 = self.parent.item3
            self.parent.item3 = None
            self.parent.mright= self.parent.right
            self.parent.right = None

    def mergeitemmleft(self):
        self.parent.left.item2 = self.parent.item1
        self.parent.item1 = None
        self.parent.mleft = None
        if self.parent.item2 is not None:
            self.parent.item1 = self.parent.item2
            self.parent.item2 = None
            self.parent.mleft = self.parent.mright
            self.parent.mright = None
        if self.parent.item3 is not None:
            self.parent.item2 = self.parent.item3
            self.parent.item3 = None
            self.parent.mright = self.parent.right
            self.parent.right = None

    def mergeitemmright(self):
        self.parent.mleft.item2 = self.parent.item2
        self.parent.item2 = None
        self.parent.mright = None
        if self.parent.item3 is not None:
            self.parent.item2 = self.parent.item3
            self.parent.item3 = None
            self.parent.mright = self.parent.right
            self.parent.right = None

    def mergeitemright(self):
        self.parent.mright.item2 = self.parent.item3
        self.parent.item3 = None
        self.parent.right = None

    def mergeInternalLeft(self):
        self.parent.mleft.item2 = self.parent.mleft.item1
        self.parent.mleft.item1 = self.parent.item1
        self.parent.item1 = None
        self.parent.left = self.parent.mleft
        self.parent.mleft = None
        self.parent.left.mright = self.parent.left.mleft
        self.parent.left.mleft = self.parent.left.left
        self.parent.left.left = self.left
        self.left.parent = self.parent.left
        if self.parent.item2 is not None:
            self.parent.item1 = self.parent.item2
            self.parent.item2 = None
            self.parent.mleft = self.parent.mright
            self.parent.mright = None
        if self.parent.item3 is not None:
            self.parent.item2 = self.parent.item3
            self.parent.item3 = None
            self.parent.mright = self.parent.right
            self.parent.right = None

    def mergeInternalmleft(self):
        self.parent.left.item2 = self.parent.item1
        self.parent.item1 = None
        self.left.parent = self.parent.left
        self.parent.left.mright = self.left
        self.left = None
        self.parent.mleft = None
        if self.parent.item2 is not None:
            self.parent.item1 = self.parent.item2
            self.parent.item2 = None
            self.parent.mleft = self.parent.mright
            self.parent.mright = None
        if self.parent.item3 is not None:
            self.parent.item2 = self.parent.item3
            self.parent.item3 = None
            self.parent.mright = self.parent.right
            self.parent.right = None

    def mergeInternalmright(self):
        self.parent.mleft.item2 = self.parent.item2
        self.parent.item2 = None
        self.left.parent = self.parent.mleft
        self.parent.mleft.mright = self.left
        self.left = None
        self.mright = None
        if self.parent.item3 is not None:
            self.parent.item2 = self.parent.item3
            self.parent.item3 = None
            self.parent.mright = self.parent.right
            self.parent.right = None

    def mergeInternalright(self):
        self.parent.mright.item2 = self.parent.item2
        self.parent.item2 = self.parent.item3
        self.parent.item3 = None
        self.left.parent = self.parent.mright
        self.parent.mright.mleft = self.left
        self.left = None
        self.parent.right = None

    def fixtree(self):
        if self.parent is None and self.left is None and self.item1 is None:
            return True
        if self.parent is None:
            self.item1 = self.left.item1
            self.left.item1 = None
            if self.left.mleft is not None:
                self.left.mleft.parent = self
                self.mleft = self.left.mleft
                self.left.mleft = None

            if self.left.item2 is not None:
                self.item2 = self.left.item2
                self.left.item2 = None
                if self.left.mright is not None:
                    self.left.mright.parent = self
                    self.mright = self.left.mright
                    self.left.mright = None

            if self.left.item3 is not None:
                self.item3 = self.left.item3
                self.left.item3 = None
                if self.left.right is not None:
                    self.left.right.parent = self
                    self.right = self.left.right
                    self.left.right = None

            if self.left.left is not None:
                self.left.left.parent = self
                temp = self.left
                self.left = self.left.left
                temp.left = None
                temp.parent = None
                del temp
            else:
                self.left = None

        else:

            if self.parent.left is not None and self == self.parent.left and self.parent.mleft.item2 is not None:
                if self.left is None:
                    self.redistributeleft()
                else:
                    self.redistributeInternalleft()

            elif self.parent.mleft is not None and self == self.parent.mleft and (self.parent.left.item2 is not None
                                                                             or (self.parent.mright is not None and
                                                                                 self.parent.mright.item2
                                                                                 is not None)):
                if self.left is None:
                    if self.parent.left.item2 is not None:
                        self.redistributemleft(self.parent.left)
                    elif self.parent.mright is not None and self.parent.mright.item2 is not None:
                        self.redistributemleft(self.parent.mright)
                else:
                    if self.parent.left.item2 is not None:
                        self.redistributeInternalmleft(self.parent.left)
                    elif self.parent.mright is not None and self.parent.mright.item2 is not None:
                        self.redistributeInternalmleft(self.parent.mright)

            elif self.parent.mright is not None and self == self.parent.mright and (self.parent.mleft.item2 is not None
                                                                                    or (self.parent.right is not None
                                                                                        and self.parent.right.item2
                                                                                        is not None)):
                if self.left is None:
                    if self.parent.mleft is not None:
                        self.redistributemright(self.parent.mleft)
                    elif self.parent.right is not None and self.parent.right.item2 is not None:
                        self.redistributemright(self.parent.right)
                else:
                    if self.parent.mleft.item2 is not None:
                        self.redistributemright(self.parent.mleft)
                    elif self.parent.right is not None and self.parent.right.item2 is not None:
                        self.redistributeInternalmright(self.parent.right)

            elif self.parent.right is not None and self == self.parent.right and self.parent.mright.item2 is not None:
                if self.left is None:
                    self.redistributeright()
                else:
                    self.redistributeInternalright()
            else:
                if self.parent.left == self:
                    if self.left is not None:
                        self.mergeInternalLeft()
                    else:
                        self.mergeitemleft()
                elif self.parent.mleft == self:
                    if self.left is not None:
                        self.mergeInternalmleft()
                    else:
                        self.mergeitemmleft()
                elif self.parent.mright == self:
                    if self.left is not None:
                        self.mergeInternalmright()
                    else:
                        self.mergeitemmright()
                elif self.parent.right == self:
                    if self.left is not None:
                        self.mergeInternalright()
                    else:
                        self.mergeitemmright()

                parent = self.parent
                self.parent = None
                if parent.item1 is None:
                    parent.fixtree()
                self.left = None # mogelijk een probleem
                del self


    def T234Delete(self, key):
        if self.item1.key == key:
            if self.left is None:
                if self.item2 is None:
                    self.item1 = None
                elif self.item3 is not None:
                    self.item1 = self.item2
                    self.item2 = self.item3
                    self.item3 = None
                else:
                    self.item1 = self.item2
                    self.item2 = None
            else:
                inordernode = self.inorder1()
                temp = self.item1
                self.item1 = inordernode.item1
                inordernode.item1 = temp
                inordernode.T234Delete(key)

            if self.item1 is None:
                self.fixtree()

        elif self.item2 is not None and self.item2.key == key:
            if self.left is None:
                if self.item3 is not None:
                    self.item2 = self.item3
                    self.item3 = None
                else:
                    self.item2 = None
            else:
                inordernode = self.inorder2()
                temp = self.item2
                self.item2 = inordernode.item1
                inordernode.item1 = temp
                inordernode.T234Delete(key)

        elif self.item3 is not None and self.item3.key == key:
            if self.left is None:
                self.item3 = None
            else:
                inordernode = self.inorder3()
                temp = self.item2
                self.item2 = inordernode.item1
                inordernode.item1 = temp
                inordernode.T234Delete(key)
        elif key < self.item1.key:
            self.left.T234Delete(key)

        elif self.item2 is None or key < self.item2.key:
            self.mleft.T234Delete(key)

        elif self.item3 is None or key < self.item3.key:
            self.mright.T234Delete(key)

        else:
            self.right.T234Delete(key)

    def retrieve(self, key):
        if self.item1 is not None and self.item1.key == key:
            return (True, self.item1.item)
        elif self.item2 is not None and self.item2.key == key:
            return (True, self.item2.item)
        elif self.item3 is not None and self.item3.key == key:
            return (True, self.item3.item)
        elif self.left is not None and key < self.item1.key:
            return self.left.retrieve(key)

        elif self.mleft is not None and (self.item2 is None or key < self.item2.key):
            return self.mleft.retrieve(key)

        elif self.mright is not None and (self.item3 is None or key < self.item3.key):
            return self.mright.retrieve(key)

        elif self.right is not None:
            return self.right.retrieve(key)

        else:
            return (False, None)

    def getRoot(self):
        if self.item1 is None:
            return
        elif self.item2 is None:
            return tuple(self.item1)
        elif self.item3 is None:
            return tuple(self.item1, self.item2)
        else:
            return tuple(self.item1, self.item2, self.item3)

    def print(self, nummer):
        f = open(nummer, "w")
        f.write("digraph 234{")
        f.write(str("node [shape=record];") + '\n')
        f.write(str("edge[splines=" + "line" + "];" + '\n'))
        if not self.isEmpty():
            self.dotread(f)
        f.write("}")
        f.close()

    def dotread(self, file):
        if self.item3 is not None:
            file.write(str(self.item1.key) + str("[label=" + '"' + "<left> " + str(self.item1.key) +
                                                 "|<middle> " + str(self.item2.key) + "|<right> " + str(self.item3.key) +
                                                 '"' + "];") + '\n')
        elif self.item2 is not None:
            file.write(str(self.item1.key) + str("[label=" + '"' + "<left> " + str(self.item1.key) +
                                                 "|<middle> " + str(self.item2.key) + '"' + "];") + '\n')
        elif self.item1 is not None:
            file.write(str(self.item1.key) + str("[label=" + '"' + "<left> " + str(self.item1.key) + '"' + "];") + '\n')
        else:
            return

        if self.left is not None:
            self.left.dotread(file)
            file.write(str(self.item1.key) + " -> " + str(self.left.item1.key) + ";" + '\n')

        if self.mleft is not None:
            self.mleft.dotread(file)
            file.write(str(self.item1.key) + " -> " + str(self.mleft.item1.key) + ";" + '\n')

        if self.mright is not None:
            self.mright.dotread(file)
            file.write(str(self.item1.key) + " -> " + str(self.mright.item1.key) + ";" + '\n')

        if self.right is not None:
            self.right.dotread(file)
            file.write(str(self.item1.key) + "-> " + str(self.right.item1.key) + ";" + '\n')

    def destroySearchtree(self):
        if self.left is not None:
            self.left.destroySearchtree()

        if self.mleft is not None:
            self.mleft.destroySearchtree()

        if self.mright is not None:
            self.mright.destroySearchtree()

        if self.right is not None:
            self.right.destroySearchtree()

        return self.destroyNode()

    def traverse(self, visit, key=None):
        self.inorderTraversal(visit, key)

    def inorderTraversal(self, visit, key=None):
        if self.left is not None:
            self.left.inorderTraversal(visit, key)
        if self.item1 is not None:
            visit(self.item1.item, key)
        if self.mleft is not None:
            self.mleft.inorderTraversal(visit, key)
        if self.item2 is not None:
            visit(self.item2.item, key)
        if self.mright is not None:
            self.mright.inorderTraversal(visit, key)
        if self.item3 is not None:
            visit(self.item3.item, key)
        if self.right is not None:
            self.right.inorderTraversal(visit, key)

    def preorderTraversal(self, visit, key=None):
        if self.item1 is not None:
            visit(self.item1.item, key)
        if self.left is not None:
            self.left.preorderTraversal(visit, key)
        if self.mleft is not None:
            self.mleft.preorderTraversal(visit, key)
        if self.item2 is not None:
            visit(self.item2.item, key)
        if self.mright is not None:
            self.mright.preorderTraversal(visit, key)
        if self.item3 is not None:
            visit(self.item3.item, key)
        if self.right is not None:
            self.right.preoderTraversal(visit, key)

    def postorderTraversal(self, visit, key=None):
        if self.left is not None:
            self.left.postorderTraversal(visit, key)
        if self.mleft is not None:
            self.mleft.postorderTraversal(visit, key)
        if self.mright is not None:
            self.mright.postorderTraversal(visit, key)
        if self.right is not None:
            self.right.postorderTraversal(visit, key)
        if self.item3 is not None:
            visit(self.item3.item, key)
        if self.item2 is not None:
            visit(self.item2.item, key)
        if self.item1 is not None:
            visit(self.item1.item, key)

    def getIndex(self, index):
        temp = index
        if self.item1 is not None:
            if index == 0:
                return (self.item1, index)
            temp = index - 1
        if self.item2 is not None:
            if index == 1:
                return (self.item2, index)
            temp -= 1
        if self.item3 is not None:
            if index == 2:
                return (self.item3, index)
            temp -= 1
        index = temp
        if self.left != None:
            returned = self.left.getIndex(index)
            index = returned[1]
            if returned[0] != None:
                return returned
        if self.mleft != None:
            returned = self.mleft.getIndex(index)
            index = returned[1]
            if returned[0] != None:
                return returned
        if self.mright != None:
            returned = self.mright.getIndex(index)
            index = returned[1]
            if returned[0] != None:
                return returned
        if self.right != None:
            returned = self.right.getIndex(index)
            index = returned[1]
            if returned[0] != None:
                return returned
        return (None, index)

    def size(self):
        size = 0
        if self.item3 is not None:
            size = 3
        elif self.item2 is not None:
            size = 2
        elif self.item1 is not None:
            size = 1
        if self.left is not None:
            size += self.left.size()
        if self.mleft is not None:
            size += self.mleft.size()
        if self.mright is not None:
            size += self.mright.size()
        if self.right is not None:
            size += self.right.size()
        return size


def createSearchTree():
    return T234(None, None, None, None, None, None, None, None)

test = T234(None, None, None, None, None, None, None, None)
test.T234Insert(TreeItem(None, 0))
test.T234Insert(TreeItem(None, 1))
test.T234Insert(TreeItem(None, 2))
test.T234Insert(TreeItem(None, 3))
test.T234Insert(TreeItem(None, 4))
test.T234Insert(TreeItem(None, 5))
test.T234Insert(TreeItem(None, 6))
test.T234Insert(TreeItem(None, 7))
test.T234Insert(TreeItem(None, 8))
test.T234Insert(TreeItem(None, 9))
test.T234Insert(TreeItem(None, 10))
test.T234Insert(TreeItem(None, 11))
test.T234Insert(TreeItem(None, 12))
test.print("test0.dot")
test.T234Insert(TreeItem(None, 13))
test.print("test1.dot")
test.T234Insert(TreeItem(None, 14))
test.print("test2.dot")
test.T234Insert(TreeItem(None, 15))
test.print("test3.dot")
test.T234Insert(TreeItem(None, 16))
test.print("test4.dot")
