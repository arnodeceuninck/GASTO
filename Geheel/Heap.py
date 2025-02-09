from Graph import *
from KeyValueItem import *

class Heap:
    def __init__(self):
        self.top = None
        self.createHeap()

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        size = self.size()
        if size > self.index:  # Of self.index-1?
            x = self.top.getIndex(self.index)
            self.index += 1
            return (x[0].key, x[0].value)
        else:
            raise StopIteration

    def createHeap(self):
        self.top = HeapNode()
        
    def destroyHeap(self):
        del self
        # Omdat we werken in python en de nodes niet meer gebruikt worden, zal python zelf de rest van de heap afbreken
        
    def isEmpty(self):
        return self.size() == 0
        
    def insert(self, newItem):
        return self.top.insert(newItem)

        
    def getTop(self):
        return self.top.root # Returnt het volledige item, dus de key en de value als een object

    def remove(self):
        if self.top != None:
            top = self.top.root
            self.top.remove()
            return top
        return False

    def size(self):
        if self.top is None:
            return 0
        return self.top.size()

    def visualize(self, name):
        vgraph = Graph(name)
        vgraph.change_rankdir("TB")
        self.top.createVisualisation(vgraph)
        vgraph.rebuild_file()

class HeapNode:
    def __init__(self):
        self.parent = None
        self.left_tree = None
        self.right_tree = None
        self.root = None

    def destroy(self):
        self.parent = None
        self.left_tree = None
        self.right_tree = None
        self.root = None


    def size(self):
        size = 0
        if(self.left_tree != None):
            size += self.left_tree.size()
        if(self.right_tree != None):
            size += self.right_tree.size()
        if(self.root != None):
            size += 1
        return size

    def isPowerOfTwo(self, n):
        i = 1
        s = i # s is de som van alle machten
        while i <= n:
            if n == s:
                return True
            i *= 2
            s += i
        return False


    def is_full(self):
        if(self.left_tree == None and self.right_tree == None):
            return True
        if self.right_tree == None and self.left_tree.size() == 1:
            return False
        if self.left_tree == None and self.right_tree.size() == 1:
            return False
        if self.isPowerOfTwo(self.left_tree.size()) and self.isPowerOfTwo(self.right_tree.size())\
                and self.left_tree.is_full() and self.right_tree.is_full()\
                and self.left_tree.size() == self.right_tree.size():
                return True
        return False

    def findLastItem(self):
        if (self.left_tree == None and self.right_tree == None):
            return self
        if self.right_tree == None:
            return self.left_tree
        if self.right_tree.is_full() and self.left_tree.size() > self.right_tree.size():
            return self.left_tree.findLastItem()
        else:
            return self.right_tree.findLastItem()


    def trickleUp(self):
        if self.parent != None and self.parent.root.key < self.root.key:
            tempRoot = self.parent.root
            self.parent.root = self.root
            self.root = tempRoot
            self.parent.trickleUp()

    def insert(self, newItem):
        if self.root is None:
            self.root = newItem
            self.trickleUp()
            return True
        if self.left_tree is None:
            self.left_tree = HeapNode()
            self.left_tree.parent = self
            return self.left_tree.insert(newItem)

        if self.right_tree is None:
            self.right_tree = HeapNode()
            self.right_tree.parent = self
            return self.right_tree.insert(newItem)

        if self.left_tree.is_full() and self.left_tree.size() > self.right_tree.size():
            return self.right_tree.insert(newItem)
        else:
            return self.left_tree.insert(newItem)

    def isEmpty(self):
        return self.size() == 0

    def createVisualisation(self, vgraph):
        # voeg iedere node toe
        if not self.isEmpty():
            vgraph.add_node(self.root.key, self.root.key)
            if self.left_tree is None and self.right_tree is None:
                return

            # voeg de linkerverbinding toe
            if self.left_tree is not None:
                self.left_tree.createVisualisation(vgraph)
                vgraph.add_connection(self.root.key, self.left_tree.root.key, 0)
            else:
                # (Kan ook onzichtbaar zijn als er geen is, zodat het andere element duidelijk links of rechts van de node is)
                vgraph.add_node("left" + str(self.root.key), "", "circle",
                                "style=invis")
                vgraph.add_connection(self.root.key, "left" + str(self.root.key), 0, "style=invis")

            # voeg de rechterverbinding toe
            if self.right_tree is not None:
                self.right_tree.createVisualisation(vgraph)
                vgraph.add_connection(self.root.key, self.right_tree.root.key, 0)
            else:
                vgraph.add_node("right" + str(self.root.key), "", "circle",
                                "style=invis")
                vgraph.add_connection(self.root.key, "right" + str(self.root.key), 0, "style=invis")

    def findGreatestChild(self):
        if self.left_tree == None:
            return self.right_tree
        if self.right_tree == None:
            return self.left_tree
        if self.left_tree.root.key > self.right_tree.root.key:
            return self.left_tree
        return self.right_tree

    def trickleDown(self):
        greatestChild = self.findGreatestChild()
        if greatestChild != None and greatestChild.root.key > self.root.key:
            tempRoot = greatestChild.root
            greatestChild.root = self.root
            self.root = tempRoot
            greatestChild.trickleDown()

    def remove(self):
        if self.parent == None and self.size() == 1:
            return self.destroy()
        lastItem = self.findLastItem()
        self.root = lastItem.root
        if lastItem.parent != None:
            if lastItem.parent.left_tree == lastItem:
                lastItem.parent.left_tree = None
            elif lastItem.parent.right_tree == lastItem:
                lastItem.parent.right_tree = None
        lastItem.destroy()
        self.trickleDown()

    def getIndex(self, index):
        if index == 0:
            return (self.root, index)
        index -= 1
        if self.left_tree is not None:
            returned = self.left_tree.getIndex(index)
            index = returned[1]
            if returned[0] != None:
                return returned
        if self.right_tree is not None:
            returned = self.right_tree.getIndex(index)
            index = returned[1]
            if returned[0] != None:
                return returned
        return (None, index)

def createHeap():
    return Heap()