from Graph import *

class Node:
    def __init__(self, value):
        self.value = value
        self.below = None


class stack:
    def __init__(self):
            self.stackpointer = None

    def __iter__(self):
        self.iterPointer = self.stackpointer
        return self

    def __next__(self):
        if self.iterPointer == None:
            raise StopIteration
        else:
            return_value = self.iterPointer.value
            self.iterPointer = self.iterPointer.below
            return return_value

    def push(self, new):
        new.below = self.stackpointer
        self.stackpointer = new
        return

    def pop(self):
        if self.stackpointer is None:
            return False
        temp = self.stackpointer
        self.stackpointer = self.stackpointer.below
        return temp.value

    def getTop(self):
        return self.stackpointer.value

    def isEmpty(self):
        if self.stackpointer is None:
            return True
        else:
            return False

    def destroyStack(self):
        while self.isEmpty() is False:
            self.pop()
        return

    def getLength(self):
        size = 0
        node = self.stackpointer
        while node is not None:
            size += 1
            node = node.below
        return size

    def print(self, filename):
        # Maakt een .dot file met daarin een visuele representatie van de boom (in .dot language)

        vgraph = Graph(filename)
        vgraph.change_rankdir("TB")  # Bomen worden meestal van Top to Bottem getoond

        node = self.stackpointer
        while node is not None:
            vgraph.add_node(node.value, node.value)
            if node.below != None:
                vgraph.add_connection(node.value, node.below.value)
            node = node.below

        # Alle nodes en verbindingen zijn nu toegevooegd aan vgraph, maak er nu dus het bestand zelf van
        vgraph.rebuild_file()

def createstack():
    return stack()

test = createstack()
test.push(Node(70))
test.push(Node(80))
test.push(Node(45))
test.pop()
test.push(Node(90))
# print(test.pop())
test.pop()
# print("End")
