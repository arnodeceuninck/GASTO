class clc:
    def __init__(self,file):
        self.file = open(file, 'r')
        self.element = 0
        self.start_lijn_operaties = 0
        self.clc = []
        self.nummer_file = 1
        clc.lees(self)
    def lees(self):
        type = ""
        operatie = False
        for line in self.file:
            for char in line:
                if char == "#":
                    break
                elif char == "=":
                    operatie = True
                    self.start_lijn_operaties = line
                elif char == "\n":
                    break
                elif operatie == True:
                    type += char
            if type == "clc":
                clc.lees_operaties(self)
                break
            elif type != "" and type != "clc":
                print("onbekend type")
                type = ""
                operatie = False
    def lees_operaties(self):
        with self.file as f:
            data = f.readlines()
            for line in data:
                if line == '\n':
                    break
                else:
                    words = line.split()
                    if words[0] == "insert":
                        self.element = int(words[1])
                        clc.insert(self)
                    elif words[0] == "delete":
                        self.element = int(words[1])
                        clc.delete(self)
                    elif words[0] == "print":
                        clc.print(self)
    def insert(self):
        hulp_lijst = []
        plaats = 0
        if len(self.clc) == 0:
            self.clc.append(self.element)
            print(self.clc)
        elif len(self.clc) > 0:
            for element in range(len(self.clc)):
                if self.element < self.clc[0]:
                    hulp_lijst.append(self.element)
                    self.clc = hulp_lijst + self.clc
                    break
                elif self.element > self.clc[element]:
                    plaats += 1
                else:
                    break
            if plaats != 0:
                for i in range(plaats):
                    hulp_lijst.append(self.clc[0])
                    self.clc.remove(self.clc[0])
                hulp_lijst.append(self.element)
                self.clc = hulp_lijst + self.clc
            print(self.clc)
    def delete(self):
        plaats = 0
        for element in range(len(self.clc)-1):
            if self.element == self.clc[element]:
                plaats = element
        self.clc.remove(self.clc[plaats])
        print(self.clc)
    def print(self):
        naam_bestand = "clc-" + str(self.nummer_file) + ".dot"
        print(naam_bestand)
        file = open(naam_bestand, "w")
        file.write("digraph G {\nnodesep = 0.5;\nrankdir = LR;\n\n")
        stack = ""
        file.write("node [shape=record];\n")
        aantal_elementen = 0
        element = 0
        while aantal_elementen < len(self.clc):
            stack = "<f" + str(element) + ">" + str(self.clc[aantal_elementen])
            file.write("node" + str(element) + "[label = " + '"' + stack + '"' + "];\n")
            element += 1
            aantal_elementen += 1
        file.write(
            "subgraph cluster_0 {\n\tstyle=filled;\n\tcolor=white;\n\tnode [style=filled,color=white];\n\tnode0;\n")
        file.write("}\n")
        for i in range(len(self.clc) - 1):
            file.write("node" + str(i) + " -> " + "node" + str(i + 1) + "\n")
        file.write("node" + str(len(self.clc)-1) + " -> " + "node" + str(0) + "\n")
        file.write("}")
        file.close()
clc("adt.txt")

