import TweeDrieBoom

class lees:
    def __init__(self, file):
        self.file = open(file, 'r')
        self.nummer_file = 0
        self.lees(self.file)
    def lees(self, file):
        type = ""
        TTT = TweeDrieBoom.create23T()
        for line in file:
            if line[0] == "#" or line[0] == "\n":
                pass
            else:
                if line[0:4] == "type":
                    type = self.readType(line)
                    if type != "23":
                        print("onbekend type")
                if type == "23":
                    if "insert" in line:
                        self.insert(line, TTT)
                    elif "delete" in line:
                        self.delete(line, TTT)
                    elif "print" in line:
                        self.print(TTT)

    def readType(self, line):
        type = ""
        typeGevonden = False
        for char in line:
            if char == "\n":
                return type
            if char == "=":
                typeGevonden = True
            elif typeGevonden == True:
                type += char
    def insert(self, line, TTT):
        wordsInLine = line.split()
        Item = TweeDrieBoom.TreeItem(int(wordsInLine[1]), int(wordsInLine[1]))
        TTT.insertItem(Item)
        return

    def delete(self, line, TTT):
        wordsInLine = line.split()
        TTT.delete(int(wordsInLine[1]))
        return
    def print(self, TTT):
        filename = "23-" + str(self.nummer_file) + ".dot"
        TweeDrieBoom.write_dot(filename, TTT)
        self.nummer_file += 1
        return
lees("adt.txt")