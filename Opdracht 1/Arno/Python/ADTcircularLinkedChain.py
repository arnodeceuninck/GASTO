from graph import Graph

class node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def attach_node(self, node):
        self.next = node

class circular_chain:

    def __init__(self):
        self.head = node("head")
        self.count = 0

    def createList(self):
        self.__init__()

    def destroyList(self):
        del self  # Todo: test if possible

    def isEmpty(self):
        if self.count == 0:
            return True
        return False

    def getLength(self):
        return self.count

    def insert(self, index, newItem):
        # test if in chain range
        if index > self.count or index < 0:
            return False

        # loop through the nodes until the asked index
        current_node = self.head
        previous_node = None
        for i in range(index+1):
            previous_node = current_node
            current_node = current_node.next

        # create the new node
        new_node = node(newItem)

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

    def delete(self, index):
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

    def retrieve(self, index):
        if index > self.count or index < 0:
            return False
        current_node = self.head
        for i in range(index+1):
            current_node = current_node.next
        return current_node.value

    def visualize(self):
        self.grafiek = Graph()
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

chain = circular_chain()
chain.insert(0, "first")
chain.insert(0, "newFirst")
chain.insert(1, "second")
chain.insert(2, "third")
chain.insert(3, "fourth")
chain.insert(4, "fifth")
chain.delete(chain.getLength()-1)
chain.visualize()

