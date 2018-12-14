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

class Heap:
    def __init__(self):
        self.top = None
        self.createHeap()
        
    def createHeap(self):
        self.top = HeapNode()
        self.size = 0
        
    def destroyHeap(self):
        self.top = None
        self.size = None
        del self
        
    def isEmpty(self):
        return self.size == 0
        
    def insert(self, newItem):
       self.top.insert(newItem)
       return
        
    def getTop(self):
        return self.top # TODO: moet .value of getValue erbij?

    def remove(self):
        top = self.top
        # TODO: Remove top + heaprebuild
        self.top.remove()
        return top

    def size(self):
        if self.top is None: return 0
        return self.top.size()

    def visualize(self):
        vgraph = Graph()
        vgraph.change_rankdir("TB")
        self.top.createVisualisation(vgraph)
        vgraph.rebuild_file()
        
class HeapItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def getKey(self):
        return self.key
    def getValue(self):
        return self.value
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
        if self.left_tree.size() > self.right_tree.size():
            return self.left_tree.findLastItem()
        else:
            self.right_tree.findLastItem()


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
            return
        if self.left_tree is None:
            self.left_tree = HeapNode()
            self.left_tree.parent = self
            self.left_tree.insert(newItem)
            return
        if self.right_tree is None:
            self.right_tree = HeapNode()
            self.right_tree.parent = self
            self.right_tree.insert(newItem)
            return
        if self.left_tree.is_full() and self.left_tree.size() > self.right_tree.size():
            self.right_tree.insert(newItem)
            return
        else:
            self.left_tree.insert(newItem)
            return

    def isEmpty(self):
        return self.size() == 0

    def createVisualisation(self, vgraph):
        if not self.isEmpty():
            if self.left_tree is not None:
                vgraph.add_connection(self.root.value, self.left_tree.root.value, 0)
                self.left_tree.createVisualisation(vgraph)

            if self.right_tree is not None:
                vgraph.add_connection(self.root.value, self.right_tree.root.value, 0)
                self.right_tree.createVisualisation(vgraph)

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

hoera = Heap() # Heap heap heap, Hoera!
hoera.insert(HeapItem(5, "vijf"))
hoera.insert(HeapItem(4, "vier"))
hoera.insert(HeapItem(2, "twee"))
hoera.insert(HeapItem(3, "drie"))
hoera.insert(HeapItem(6, "zes"))
hoera.insert(HeapItem(7, "zeven"))
hoera.insert(HeapItem(8, "acht"))
hoera.insert(HeapItem(9, "negen"))
# hoera.remove()
hoera.visualize()
pass