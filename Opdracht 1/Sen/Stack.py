class stack:
    def __init__(self, file):
        self.file = open(file, 'r')
        self.element = 0
        self.start_lijn_operaties = 0
        self.stack = []
        self.nummer_file = 1
        stack.lees(self)
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
            if type == "stack":
                stack.lees_operaties(self)
                break
            elif type != "" and type != "stack":
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
                        stack.insert(self)
                    elif words[0] == "delete":
                        stack.delete(self)
                    elif words[0] == "print":
                        stack.print(self)
    def insert(self):
        self.stack.append(self.element)
    def delete(self):
        self.stack.remove(self.stack[-1])
    def print(self):
        naam_bestand = "stack-" + str(self.nummer_file) + ".dot"
        print(naam_bestand)
        file = open(naam_bestand, "w")
        file.write("digraph G {\nnodesep = 0.5;\n\n")
        stack = ""
        file.write("node [shape=record];\n")
        aantal_elementen = len(self.stack)-1
        element = 0
        while aantal_elementen != 0:
            stack = "<f"+str(element)+">"+str(self.stack[aantal_elementen])
            file.write("node"+str(element)+"[label = "+'"'+stack+'"'+"];\n")
            element += 1
            aantal_elementen -= 1
        stack = "<f"+str(self.stack[0])+">"+str(self.stack[0])
        file.write("node"+str(element)+"[label = "+'"'+stack+'"'+"];\n")
        #file.write("node0[label = "+'"'+stack+'"'+"];\n")
        file.write("subgraph cluster_0 {\n\tstyle=filled;\n\tcolor=white;\n\tnode [style=filled,color=white];\n\tnode0;\n")
        file.write("}\n")
        for i in range(len(self.stack)-1):
            file.write("node"+str(i)+" -> "+"node"+str(i+1)+"\n")
        file.write("}")
        file.close()
stack("adt.txt")