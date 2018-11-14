nodes = []
connecties = []
class Node:

    def __init__(self, name, label, style):
        self.name = name
        self.label = label
        self.style = style
        self.to_string()

    def to_string(self):
        output = str(self.name) + "[label= " + str(self.label) + " , " + "style = " + str(self.style) + "]" + "\n"
        nodes.append(output)
        return output

class Verbinden:

    def __init__(self, a, b, type):
        self.a = a
        self.b = b
        self.type = type
        self.to_string()

    def to_string(self):
        output = str(self.a) + " " + str(self.type) + " " + str(self.b) + "\n"
        connecties.append(output)
        return output


def BSToutput(nummer):
    f = open("BST" + str(nummer) + ".dot", "w")
    f.write("digraph bst{")
    f.write("a [style = ""invisible""]")
    for i in range(len(nodes)):
        f.write(nodes[i])
    f.write("\n")
    for i in range(len(connecties)):
        f.write(connecties[i])
    f.write("}")
    f.close()
    nodes.clear()
    connecties.clear()



