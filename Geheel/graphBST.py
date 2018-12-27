from random import randint
class Graph:
    def __init__(self):
        self.nodes = []
        self.connections = []
        self.rankdir = "LR"
        self.rebuild_file()

    def rebuild_file(self):
        name = "graph.dot"
        file = open(name, "w+")
        file.write("digraph {\n")
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
        CONNECTIONTYPES = {"arrow":"->"}
        string = ""
        string += str(self.fromN) + " "
        string += CONNECTIONTYPES[self.type] + " "
        string += str(self.toN) + " "
        return string

graph = Graph()
graph.add_node("a", ["yolo", "haha"], "Mrecord")
graph.add_connection("a", "b", 0)
graph.rebuild_file()