from Graph import Graph

class node:
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.next = None
    def attach_node(self, node):
        self.next = node

class circular_chain:

    def __init__(self):
        self.head = node("head", None)
        self.count = 0

    def __iter__(self):
        self.current = self.head
        self.index = 0
        return self

    def __next__(self):
        # Extra controle op lengte om eeuwige for-loops te vermijden,
        # kan je altijd verwijderen natuurlijk als je wel eeuwig wil loopen
        if self.current.next is None or self.index >= self.getLength():
            raise StopIteration
        else:
            self.current = self.current.next
            self.index += 1
            return (self.current.value, self.current.value)

    def createList(self):
        self.__init__()

    def destroyList(self):
        del self

    def isEmpty(self):
        if self.count == 0:
            return True
        return False

    def getLength(self):
        return self.count

    def findIndexAlphaValue(self, key):
        index = 0
        currentNode = self.head.next
        firstNode = currentNode
        while currentNode != None and currentNode.key < key:
            index += 1
            currentNode = currentNode.next
            if currentNode == firstNode:
                return index
        return index

    def insert(self, key, newItem):
        # test if in chain range
        index = self.findIndexAlphaValue(key)
        if index > self.count or index < 0:
            return False

        # loop through the nodes until the asked index
        current_node = self.head
        previous_node = None
        for i in range(index+1):
            previous_node = current_node
            current_node = current_node.next

        # create the new node
        new_node = node(newItem, key)

        # edit all pointers that have to change
        if self.count == 0:
            new_node.next = new_node
        else:
            new_node.next = current_node
        previous_node.next = new_node
        if self.getLength() == 1 and index == 0:
            current_node.next = new_node

        self.count += 1

        return True

    def delete(self, key):
        index = self.findIndexValue(key)
        # check if in range
        if index > self.count or index < 0:
            return False

        #loop through until index
        current_node = self.head
        previous_node = None
        for i in range(index+1):
            previous_node = current_node
            current_node = current_node.next

        # getting the pointers right
        # special case: deleting the first node
        if index == 0:
            if self.getLength() == 1:
                previous_node.next = None
                del current_node
                self.count -= 1
                return True
            previous_node = None
            current_node2 = self.head
            for i in range(self.getLength()+1):
                previous_node = current_node2
                current_node2 = current_node2.next
            self.head.next = current_node.next

        previous_node.next = current_node.next
        del current_node

        self.count -= 1
        return True

    def findIndexValue(self, string):
        index = 0
        currentNode = self.head.next
        firstNode = currentNode
        while str(currentNode.value.naam) != string:
            index += 1
            currentNode = currentNode.next
            if index >= self.count:
                return None
        return index

    def retrieve(self, key):
        # if index > self.count or index < 0:
        #     return False
        index = self.findIndexValue(key)
        if index == None:
            return False, None
        current_node = self.head
        for i in range(index+1):
            current_node = current_node.next
            if i == self.count:
                return False
        return (True, current_node.value)

    def visualize(self):
        self.grafiek = Graph("cl.dot")
        node = self.head
        # loop once through all nodes, and add the nodes and connections to the graph
        firstTime = True
        Done = False
        while node != None:
            if node == self.head.next and not firstTime:
                break
            if node == self.head.next:
                firstTime = False
            self.grafiek.add_node(node.value, node.value, "box")
            if node.next != None:
                self.grafiek.add_connection(node.value, node.next.value, "arrow")
            node = node.next
        self.grafiek.rebuild_file()

    def traverse(self, visit, key=None):
        node = self.head.next
        for i in range(self.count):
            visit(node.value, key)
            node = node.next

def createList():
    return circular_chain()

# chain = circular_chain()
# chain.insert(0, "first")
# chain.insert(0, "newFirst")
# chain.insert(1, "second")
# chain.insert(2, "third")
# chain.insert(3, "fourth")
# chain.insert(4, "fifth")
# chain.delete(chain.getLength()-1)
# chain.visualize()
#
