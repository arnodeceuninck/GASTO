from graph import Graph

class node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def attach_node(self, node):
        self.next = node

class queue:

    def __init__(self):
        self.first = None
        self.back = None
        self.count = 0

    def createQueue(self):
        self.__init__()

    def destroyQueue(self):
        del self # Todo: test if possible

    def isEmpty(self):
        if self.count == 0:
            return True
        return False

    def enqueue(self, element):
        if self.back == None:
            n = node(element)
            self.first = n
            self.back = n
        else:
            n = node(element)
            self.back.attach_node(n) # De nieuwe node komt achter de vorige laatste knoop
            self.back = n
        self.count += 1

    def dequeue(self):
        next_first = self.first.next
        value = self.first.value
        del self.first # clean up the used memory
        self.first = next_first
        self.count -= 1
        return value

    def getFront(self):
        return self.first.value

    def visualize(self):
        self.grafiek = Graph()
        self.grafiek.change_rankdir("RL")
        node = self.first
        while node != None:
            self.grafiek.add_node(node.value, node.value, "box")
            if node.next != None:
                self.grafiek.add_connection(node.value, node.next.value, "arrow")
            node = node.next
        self.grafiek.rebuild_file()
        return True

rij = queue()
rij.enqueue(12)
rij.enqueue(52)
rij.enqueue(1)
rij.enqueue(4)
rij.enqueue(9)
print(rij.getFront())
rij.dequeue()
print(rij.getFront())
rij.visualize()


