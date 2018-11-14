class bst:
    def __init__(self,file):
        self.file = open(file, 'r')
        self.element = 0
        self.start_lijn_operaties = 0
        self.bst = []
        self.nummer_file = 1
        bst.lees(self)



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
            if type == "bst":
                bst.lees_operaties(self)
                break
            elif type != "" and type != "bst":
                print("onbekend type")

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
                        bst.insert(self)
                    elif words[0] == "delete":
                        self.element = int(words[1])
                        bst.delete(self)
                    elif words[0] == "print":
                        bst.print(self)


    def insert(self):
        hulp_lijst = []
        kleiner = False
        plaats = 0
        if len(self.bst) == 0:
            self.bst.append(self.element)
        else:
            if len(self.bst) == 1:
                if self.element > self.bst[0]:
                    self.bst.append(self.element)
                else:
                    hulp_lijst.append(self.element)
                    self.bst = hulp_lijst + self.bst
            else:
                for element in range(len(self.bst)):
                    if self.element < self.bst[0]:
                        kleiner = True
                        plaats = element
                        break
                    elif self.element > self.bst[-1]:
                        break
                    elif self.element < self.bst[element]:
                        kleiner = True
                        plaats = element
                if kleiner == True:
                    if plaats == 0:
                        hulp_lijst.append(self.element)
                        self.bst = hulp_lijst + self.bst
                    else:
                        for deel1 in range(len(self.bst)-(plaats)):
                            hulp_lijst.append(self.bst[0])
                            self.bst.remove(self.bst[0])
                        hulp_lijst.append(self.element)
                        self.bst = hulp_lijst + self.bst
                else:
                        self.bst.append(self.element)

    def delete(self):
        plaats = 0
        for element in range(len(self.bst)):
            if self.element == self.bst[element]:
                plaats = element
        self.bst.remove(self.bst[plaats])
    def print(self):
        print(self.bst)
        naam_bestand = "bst-" + str(self.nummer_file) + ".dot"
        print(naam_bestand)
        file = open(naam_bestand, "w")
        file.write("digraph G {\n")
        style = "\t"
        for i in range(len(self.bst)-1):
            style += str(self.bst[i])
            style += ","
        style += str(self.bst[-1])
        file.write(style+" "+"[style="+'"'+"solid"+'"'+"]"+"\n")
        root = str(self.bst[(int(len(self.bst)/2))])
        hoogte = 1
        for kind in range(int(len(self.bst)/2)-1):
            if kind == 0:
                file.write("\t"+root+"->"+str(self.bst[(int(len(self.bst)/(2*(hoogte+1))))])+"\n")
                file.write("\t" + root + "->" + str(self.bst[(int(len(self.bst) - (len(self.bst)/(2*(hoogte+1)))))])+"\n")
            else:
                file.write("\t"+str(self.bst[(int(len(self.bst)/(2*(hoogte+1))))])+"->"+ str(self.bst[(int(len(self.bst)/(2*(hoogte+2))))])+ "\n")
                file.write("\t" + str(self.bst[(int(len(self.bst)/(2*(hoogte+1))))]) + "->" + str(self.bst[int(2*(len(self.bst)/(2 * (hoogte + 1))))]) + "\n")
                file.write("\t" + str(self.bst[(int(len(self.bst) - (len(self.bst)/(2*(hoogte+1)))))]) + "->"+ str(self.bst[int(2*hoogte*(len(self.bst)/(2 * (hoogte + 1))))]) + "\n")
                file.write("\t" + str(self.bst[(int(len(self.bst) - (len(self.bst) / (2 * (hoogte + 1)))))]) + "->" + str(self.bst[int(2*hoogte*(len(self.bst)/(2 * (hoogte)))-1)]) + "\n")
            hoogte += 1
        file.write("}")
        self.nummer_file += 1
        file.close()

bst("adt.txt")
