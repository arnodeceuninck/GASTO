from Graph import *
from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.below = None
        self.identifier = randint(0, 10000)  # Vermijdt problemen bij visualisatie als er 2 dezelfde items inzitten


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
        if self.stackpointer == None:
            return None
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

    def hash_code(self, str):
        code = 0
        for char in str:
            code += ord(char)*ord(char)
        return code

        # return str.replace(" ", "")

    def print(self, filename):
        # Maakt een .dot file met daarin een visuele representatie van de boom (in .dot language)

        vgraph = Graph(filename)
        vgraph.change_rankdir("TB")  # Bomen worden meestal van Top to Bottem getoond

        node = self.stackpointer
        while node is not None:
            vgraph.add_node(str(self.hash_code(node.value)+node.identifier), str(node.value))
            if node.below != None:
                vgraph.add_connection(str(self.hash_code(node.value)+node.identifier),
                                      str(self.hash_code(node.below.value)+node.below.identifier), 0)
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
