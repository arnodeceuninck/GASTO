import dotConversion
class TreeItem:
    def __init__(self, item, key):
        self.item = item
        self.key = key



class BinaireZoekBoom:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right
        self.nonecounter = 0

    def __del__(self):
        return

    def IsEmpty(self):
        if self.left is None and self.right is None and self.root is None:
            return True
        return False

    def searchTreeInsert(self, item, key):
        #base case: blad
        if self.IsEmpty():
            self.root = TreeItem(item, key)
        if key == self.root.key:
            return False
        if key < self.root.key:
            if self.left == None:
                self.left = BinaireZoekBoom(None, None, None)
            self.left.searchTreeInsert(item, key)
        else:
            if self.right == None:
                self.right = BinaireZoekBoom(None, None, None)
            self.right.searchTreeInsert(item, key)


    def searchTreeRetrieve(self, key):
        if key == self.root.key:
            return self.root.item
        if key < self.root.key:
            return self.left.searchTreeRetrieve(key)
        else:
            return self.right.searchTreeRetrieve(key)

    def deleteSelf(self):
        self.root = None
        self.left = None
        self.right = None
        del self

    def searchTreeDelete(self, key):
        if key == self.root.key:
            self.root = self.inorderSuccesor().root
            if self.right is self.inorderSuccesor():
                self.right = None
        elif key < self.root.key:
            self.left.searchTreeDelete(key)
        else:
            self.right.searchTreeDelete(key)

    def inorderSuccesor(self):
        target = self.right
        if self.left is None and self.right is None:
            return self
        if target is None:
            target = self.left
        while target.left is not None:
            target = target.left
        return target

    def traverse(self):
        dotConversion.Node(self.root.item, self.root.key, "circle")
        if self.left != None:
            dotConversion.Verbinden(self.root.item, self.left.root.item, "->")
            self.left.traverse()
        else:
            dotConversion.Node(str("None" + str(self.root.key)), "-1", "invisible")
            dotConversion.Verbinden(self.root.item, str("None" + str(self.root.key) + " [style=invis]"), "->")
            self.nonecounter += 1
        if self.right != None:
            dotConversion.Verbinden(self.root.item, self.right.root.item, "->")
            self.right.traverse()
        else:
            dotConversion.Node(str("None" + str(self.root.key)), "-1", "invisible")
            dotConversion.Verbinden(self.root.item, str("None" + str(self.root.key) + " [style=invis]"), "->")

    def print(self, nummer):
        self.traverse()
        dotConversion.BSToutput(nummer)

def createSearchTree(item, key):
    return BinaireZoekBoom(TreeItem(item, key), None, None)



Punten = createSearchTree(5, 5)
Punten.searchTreeInsert(10, 10)
Punten.searchTreeInsert(5, 5)
Punten.searchTreeInsert(9, 9)
Punten.print(1)
Punten.searchTreeInsert(12, 12)
Punten.searchTreeDelete(10)
Punten.print(2)
