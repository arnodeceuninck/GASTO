from graphBST import Graph

class BinarySearchTree:
    """
    Root, linker en rechterkant terug binaire zoekbomen -> 3 velden per boom
    Class TreeItem:
    """

    def __init__(self, root, left_tree, right_tree):
        self.root = root
        self.left = left_tree
        self.right = right_tree

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        size = self.size()
        if size > self.index: # Of self.index-1?
            x = self.root.getIndex(self.index)
            self.index += 1
            return (x[0].key, x[0].value)
        else:
            raise StopIteration
    def createSearchTree(self):
        self.__init__(None, None, None)

    def destroySearchTree(self):
        del self

    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False

    def searchTreeInsert(self, treeitem):
        """
        A new Binary Search Tree is created and added in the correct place (order by he key in TreeItem)
        If the key is already present, this method returns False
        """
        # base case
        if self.root == None:
            self.root = treeitem
        elif treeitem.key < self.root.key:
            if self.left == None:
                self.left = BinarySearchTree(treeitem, None, None)
            else:
                self.left.searchTreeInsert(treeitem)
        elif treeitem.key >= self.root.key: # Or equals? Is a search key unique?
            if self.right == None:
                self.right = BinarySearchTree(treeitem, None, None)
            else:
                self.right.searchTreeInsert(treeitem)
        else:
            assert False

    def searchTreeDelete(self, searchKey):
        self.deleteEmpty()
        # base case
        if self.root.key == searchKey:
            if self.left == None and self.right == None:
                self.root = None
                del self # Todo: test if works
            elif self.left == None and self.right != None:
                self.root = self.right.root
                self.left = self.right.left
                self.right = self.right.right
                # Te verwijderen variabele werd zonet overschreven
            elif self.left != None and self.right == None:
                self.root = self.left.root
                self.left = self.left.left
                self.right = self.left.right
                # Te verwijderen variabele werd zonet overschreven
            else:
                previous = self
                inorder_successor = self.right
                stepLeft = False
                while(inorder_successor.left != None):
                    stepLeft = True
                    previous = inorder_successor
                    inorder_successor = inorder_successor.left
                self.root = inorder_successor.root
                if stepLeft == True:
                    previous.left = None # Dit verwijdert het blad
                else:
                    previous.right = None # De inorder succesor is het direct volgende element
                # del inorder_successor
        elif searchKey < self.root.key:
            if self.left == None:
                return True # Element not found, already removed
            else:
                self.left.searchTreeDelete(searchKey)
        elif searchKey >= self.root.key:  # Or equals? Is a search key unique?
            if self.right == None:
                return True  # Element not found, already removed
            else:
                self.right.searchTreeDelete(searchKey)

    def searchTreeRetrieve(self, searchKey):
        """
        returns the (sub-)BinarySearchTree with the given key. Recursive
        """
        # base case
        if self.root.key == searchKey:
            return self.root.item # item found
        elif searchKey < self.root.key:
            if self.left == None:
                return False # item not found
            else:
                self.left.searchTreeRetrieve(searchKey)
        elif searchKey >= self.root.key:  # Or equals? Is a search key unique?
            if self.right == None:
                return False # item not found
            else:
                self.right.searchTreeRetrieve(searchKey)

    def preorderTraverse(self):
        if(not self.isEmpty()):
            print(self.root.item)
            if self.left != None:
                self.left.preorderTraverse()
            if self.right != None:
                self.right.preorderTraverse()

    def deleteEmpty(self):
        if(not self.isEmpty()):
            if self.left != None:
                if self.left.root == None and self.left.left == None and self.left.right == None:
                    self.left = None
            if self.right != None:
                if self.right.root == None and self.right.left == None and self.right.right == None:
                    self.right = None
            if self.left != None:
                self.left.deleteEmpty()
            if self.right != None:
                self.right.deleteEmpty()

    def inorderTraverse(self, visit):   #todo check
        """

        """
        if self.left is not None:
            self.left.inorderTraverse(visit)
        visit(self.root.value) # Todo: test if works
        if self.right is not None:
            self.right.inorderTraverse(visit)

        # if (not self.isEmpty()):
        #     if self.left != None:
        #         self.left.preorderTraverse()
        #     print(self.root.item)
        #     if self.right != None:
        #         self.right.preorderTraverse()

    def traverse(self, visit):  #todo check
        return self.root.inorderTraverse(visit)

    def getIndex(self, index):  #todo check
        if index == 0:
            return (self.root, index)
        index -= 1
        if self.left is not None:
            returned = self.left.getIndex(index)
            index = returned[1]
            if returned[0] != None:
                return returned
        if self.right is not None:
            returned = self.right.getIndex(index)
            index = returned[1]
            if returned[0] != None:
                return returned
        return (None, index)

    def size(self): #todo check
        if self.root == None:
            return 0
        return self.root.size()

    def Size(self): #todo check
        size = 0
        if(self.left != None):
            size += self.left.size()
        if(self.right != None):
            size += self.right.size()
        if(self.root != None):
            size += 1
        return size

    def print(self):
        vgraph = Graph()
        vgraph.change_rankdir("TB")
        self.createVisualisation(vgraph)
        vgraph.rebuild_file()

    def createVisualisation(self, vgraph):
        self.deleteEmpty()
        if (not self.isEmpty()):
            if self.left != None:
                vgraph.add_connection(self.root.key, self.left.root.key, "arrow")
                self.left.createVisualisation(vgraph)
            if self.right != None:
                vgraph.add_connection(self.root.key, self.right.root.key, "arrow")
                self.right.createVisualisation(vgraph)



class TreeItem:
    def __init__(self, item, key):
        self.item = item
        self.key = key


#ItemsToInsert = [561, 23, 624, 26, 324, 743, 11, 874, 325, 634]
#ItemsToInsert = [10, 5, 15, 2, 7, 13, 17, 1, 3, 6, 8, 12, 14, 16, 18, 11]
ItemsToInsert = [12, 11, 13, 10.5,11.5, 11.75, 11.25]
sample_tree = BinarySearchTree(None, None, None)

vgraph = Graph()
vgraph.change_rankdir("TB")

for item in ItemsToInsert:
    sample_tree.searchTreeInsert(TreeItem(item, item))


# sample_tree.searchTreeDelete(12)


sample_tree.preorderTraverse()

sample_tree.createVisualisation(vgraph)
vgraph.rebuild_file()