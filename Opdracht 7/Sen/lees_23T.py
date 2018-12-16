import TweeDrieBoom

class lees:
    def __init__(self, file):
        self.file = open(file, 'r')
        self.element = 0
        self.start_lijn_operaties = 0
        self.lees()
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
            if type == "23":
                TTT = TweeDrieBoom.TweeDrieBoom()
                TTT.create23T()
                self.lees_operaties(TTT)
                break
            elif type != "" and type != "bst":
                print("onbekend type")
                type = ""
                operatie = False

    def lees_operaties(self, TTT):
        with self.file as f:
            data = f.readlines()
            for line in data:
                if line == '\n':
                    break
                else:
                    words = line.split()
                    if words[0] == "insert":
                        self.element = int(words[1])
                        Item = TweeDrieBoom.TreeItem(0, self.element)
                        TTT.insertItem(Item)
                    elif words[0] == "delete":
                        self.element = int(words[1])
                        TTT.delete(self.element)
                    elif words[0] == "print":
                        TweeDrieBoom.TweeDrieBoom.print(self)

lees("adt.txt")