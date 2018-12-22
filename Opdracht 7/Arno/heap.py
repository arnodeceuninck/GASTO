from Graph import *
from KeyValueItem import *

class Heap:
    def __init__(self):
        self.top = None
        self.createHeap()
        
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
        top = self.top.root
        # TODO: Remove top + heaprebuild
        self.top.remove()
        return top

    def size(self):
        if self.top is None:
            return 0
        return self.top.size()

    def visualize(self):
        vgraph = Graph("heap")
        vgraph.change_rankdir("TB")
        self.top.createVisualisation(vgraph)
        vgraph.rebuild_file()

class HeapNode:
    def __init__(self):
        self.parent = None
        self.left_tree = None
        self.right_tree = None
        self.root = None

    # Niet meer nodig omdat de root van de top alleen verandert, en niet de top zelf
    # def findNewTop(self):
    #     if(self.parent == None):
    #         return self
    #     else: return self.parent.findNewTop()

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

    def is_full(self):
        if(self.left_tree == None and self.right_tree == None):
            return True
        if self.left_tree is not None and self.right_tree is not None:
            return self.left_tree.is_full() and self.right_tree.is_full()
        return False

    def findLastItem(self):
        if (self.left_tree == None and self.right_tree == None):
            return self
        if self.right_tree == None:
            return self.left_tree
        if self.right_tree.is_full and self.left_tree.size() > self.right_tree.size():
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
        vgraph.add_node(self.root.key, self.root.key)
        if not self.isEmpty():

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
        lastItem = self.findLastItem()
        self.root = lastItem.root
        # TODO: What if no parent exists?
        if lastItem.parent.left_tree == lastItem:
            lastItem.parent.left_tree = None
        elif lastItem.parent.right_tree == lastItem:
            lastItem.parent.right_tree = None
        lastItem.destroy()
        self.trickleDown()

def createHeap():
    return Heap()

# hoera = createHeap() # Heap heap heap, Hoera!
# hoera.insert(KeyValueItem(5, "vijf"))
# hoera.insert(KeyValueItem(4, "vier"))
# hoera.insert(KeyValueItem(2, "twee"))
# hoera.insert(KeyValueItem(3, "drie"))
# hoera.insert(KeyValueItem(6, "zes"))
# hoera.insert(KeyValueItem(7, "zeven"))
# hoera.insert(KeyValueItem(8, "acht"))
# hoera.insert(KeyValueItem(9, "negen"))
# hoera.insert(KeyValueItem(10, "tien"))
# hoera.remove()
# hoera.visualize()
# pass