import Graph
class Pointer:
    def __init__(self, target):
        self.target = target

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def createQueue(self):
        self.Front = Pointer(None)
        self.Back = Pointer(None)
        return self

    def destroyQueue(self):
        self.Front.target = None


    def isEmpty(self):
        if self.Front.target is None:
            return True
        else:
            return False

    def enqueue(self, value):
        newNode = Node(value)
        self.Last = self.Back.target
        if self.Front.target is None:
            self.Front.target = newNode
            self.Back.target = newNode
            return True
        else:
            self.Last.next = newNode
            self.Back.target = newNode
            return True


    def dequeue(self):
        First = self.Front.target
        self.Front.target = First.next
        First.next = None
        return First.value, True


    def getFront(self):
        if not self.isEmpty():
            return True, self.Front.target.value
        return False, None

    def getLenght(self):
        size = 0
        node = self.getFront()
        while node is not None:
            size += 1
            node = node.next

    def print(self, filename):

        # Maakt een .dot file met daarin een visuele representatie van de boom (in .dot language)

        vgraph = Graph.Graph(filename)
        vgraph.change_rankdir("TB")  # Bomen worden meestal van Top to Bottem getoond

        node = self.Front.target
        while node is not None:
            vgraph.add_node(node.value, node.value)
            if node.next != None:
                vgraph.add_connection(node.value, node.next.value, 0)
            node = node.next

        # Alle nodes en verbindingen zijn nu toegevooegd aan vgraph, maak er nu dus het bestand zelf van
        vgraph.rebuild_file()


if __name__ == '__main__':
    q = Queue()
    q.createQueue()
    q.enqueue(10)
    print(q.getFront())
    print(q.dequeue())