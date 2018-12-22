# TODO: Stel python folderstructuur op
# TODO: Steek deze klasse in een apart bestand

class Graph:
    def __init__(self, filename):
        self.nodes = []
        self.connections = []
        self.rankdir = "LR"
        self.filename = filename
        self.rebuild_file()

    def rebuild_file(self):
        name = self.filename + ".dot"
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

    def add_node(self, name, label_elements, shape="circle", extra=None):
        new_node = node(name, label_elements, shape, extra)
        self.nodes.append(new_node)

    def add_connection(self, fromN, toN, type, extra=None):
        new_connection = connection(fromN, toN, type, extra)
        self.connections.append(new_connection)

class node:
    def __init__(self, name, label_elements, shape, extra=None):
        self.name = name
        self.labels = label_elements
        self.shape = shape
        self.extra = extra
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
        string += " shape="+self.shape+" "
        if self.extra != None:
            string += self.extra
        string += "]"

        return string

class connection:
    def __init__(self, fromN, toN, type, extra=None):
        self.fromN = fromN
        self.toN = toN
        self.type = type
        self.extra = extra

    def __str__(self):
        CONNECTIONTYPES = {"arrow":"->", 0:"--", 1:"--"}
        string = ""
        string += str(self.fromN) + " "
        string += CONNECTIONTYPES[self.type] + " "
        string += str(self.toN) + " "
        string += '['
        if self.type == 0:
            string += 'color ="black"' + " "
        elif self.type == 1:
            string += 'color ="red"' + " "
        if self.extra != None:
            string += self.extra
        string += ']'
        return string
