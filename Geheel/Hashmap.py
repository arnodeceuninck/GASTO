class TreeItem():
    def __init__(self, item, key):
        self.item = item
        self.key = key
        self.next = None
        self.prev = None

class Hashmap():
    def __init__(self, size, type):
        self.tableSize = size
        self.hashTable = [None] * (self.tableSize)
        self.step = 1
        self.type = type  # 1 lineair, 2 quadratic, 3 bucketing
        self.count = 0      #houden een count bij zodat er niet meer geinsert kan worden dan de hashmap groot is

    def __iter__(self):
        self.index = 0
        self.element = 0 # voor meerdere elementen op 1 index
        return self

    def __next__(self):
        if self.index == self.tableSize:
            raise StopIteration
        else:
            while self.hashTable[self.index] == None:
                self.index += 1
                if self.index >= self.tableSize:
                    raise StopIteration
            index_place = self.hashTable[self.index]
            if self.type == "hsep":
                if self.element != len(index_place.root):
                    return_item = index_place.root[self.element]
                    self.element += 1
                    return return_item.key, return_item.item
                else:
                    self.index += 1
                    return self.__next__()
            else:
                self.index += 1
                return index_place.key, index_place.item

    def hashf(self, key):
        """ Als de key een woord is dan gaan we de hashfunctie nemen van het totaal van alle ascii codes """
        num = 0
        if type(key) != int:
            for char in key:
                num += ord(char)
            return num % self.tableSize
        else:
            return key % self.tableSize

    def herHashf(self, key):
        """ Deze functie wordt gebruikt bij lineair of quadratic probing, wanneer een element op een bezete index komt """
        num = 0
        if type(key) != int:
            for char in key:
                num += ord(char)
            key = num

        if self.type == 1:
            return (key + self.step) % self.tableSize
        elif self.type == 2:
            return int((key + (self.step)**2) % self.tableSize)


    def insert(self, key, item):
        self.count += 1
        if self.type == 3:      #bij seperate chaining gebruiken we een andere insert functie
            self.ll_insert(item, key)
        elif self.count < self.tableSize + 1:
            treeItem = TreeItem(item, key)
            self.step = 1
            self.hashTable[self.getPosition(key)] = treeItem    #getPosition wordt aangeroepen om de juiste positie te bepalen waar een item moet komen
                                                                #en op deze locatie wordt dan het item toegevoegd
        else:
            print("Je kan maximaal %s items inserten! Item (%s, %s) is niet geinsert geweest." %(self.tableSize, key, item))
            self.count -= 1

    def ll_insert(self, item, key):
        treeItem = TreeItem(item, key)
        index = self.hashf(key)
        if self.hashTable[index] == None:       #als er niets op de eerst bekomen index zit, wordt het item hier toegevoegd
            self.hashTable[index] = treeItem
        else:
            if self.hashTable[index].next == None:      #als de bezette index niet gekoppeld is aan een item gaan we het item hieraan toevoegen
                self.hashTable[index].next = treeItem
                self.hashTable[index].next.prev = self.hashTable[index]
            else:
                self.nu = self.hashTable[index].next    #extra var aangemaakt zodat we makkelijk kunnen loopen door de lijst
                while True:
                    if self.nu.next == None:            #de loop blijft doorgaan totdat we een node hebben gevonden waar nog geen item is
                        self.nu.next = treeItem
                        self.nu.next.prev = self.nu
                        return False
                    self.nu = self.nu.next

    def ll_retrieve(self, key):
        index = self.hashf(key)
        if self.hashTable[index] == None:
            return (False, None) # Not found
        elif self.hashTable[index].key == key:
            print(True, self.hashTable[index].item)
            return (True, self.hashTable[index].item)
        else:
            currentItem = self.hashTable[index]
            while currentItem.next is not None:
                currentItem = currentItem.next
                if currentItem.key == key:
                    print(True, currentItem.item)
                    return (True, currentItem.item)
            print(False, None)
            return (False, None)


    def getPosition(self, key):
        index = self.hashf(key)
        if self.hashTable[index] == None:   #als op de huidie plaats in de hasmap niks zit wordt deze plaats terug meegegeven
            return index
        else:
            if self.hashTable[index] != None:
                while self.hashTable[index] != None:        #loop die doorgaat tot er een vrije plaats is gevonden
                    if self.hashTable[index] == None:
                        return index
                    else:
                        if self.type == 1:
                            index = self.herHashf(index)
                        else:
                            index = self.herHashf(key)
                        if self.type == 2:
                            self.step += 1
            return index

    def traverse_sep(self, root):
        self.reserve = TreeItem(None, None)
        if root != None:
            print(root)
            for i in range(len(root)):
                print(root[i])
                if root[i] != None:
                    print(root[i].key, root[i].item)
                    self.reserve = root[i]
                    while root[i].next != None:
                        if root[i].next == None:
                            break
                        root[i].next = self.reserve.next


    def traverse(self, visit, key=None):
        if self.type == 3:
            # self.traverse_sep(self.hashTable)
            return None
        else:
            for i in range(len(self.hashTable)):
                if self.hashTable[i] != None and self.hashTable[i].item is not None:
                    visit(self.hashTable[i].item, key)
                else:
                    return False

    def addNodeForDot(self, i, count):
        if count == 0:
            return i
        else:
            return " | " + i

    def size(self):
        print(self.count)
        return self.count

    def show(self, name):
        leeg = ""
        count = 0
        f = open(name, "w+")
        f.write("graph hashmap{\n")
        f.write("node[shape=record];\n")
        for i in self.hashTable:
            if i != None:
                leeg += self.addNodeForDot(str(i.item), count)
            else:
                leeg += self.addNodeForDot("Leeg", count)
            count += 1
        print(leeg)
        f.write('Hashmap [label = "{%s}"]\n' % leeg)
        f.write("}")

    def destroy(self):
        self.hashTable.clear()
        self.count = 0

    def delete_sep(self, plaats, key):
        index = self.hashf(key)
        if self.hashTable[index].key == key:
            if self.hashTable[index].next != None:
                #eerste node
                #vewijder deze en zet de vorige zijn next naar deze zijn next
                self.hashTable[index] = self.hashTable[index].next
            else:
                self.hashTable[index] = None
            return True
        else:
            node = self.hashTable[index].next
            while node != None:
                if node.key == key:
                    #verwijder node
                    if node.next != None:
                        #verwijder een node in het midden en zet de next pointer van de vorige node op deze zijn next
                        node.prev.next = node.next
                    else:
                        #laatste node
                        #de vorige zijn next laten verwijzen naar None
                        node.prev.next = None

                    return True
                node = node.next


    def delete(self, key):
        self.count -= 1
        self.step = 1
        if self.type == 3:
            index = self.hashf(key)
            plaats = self.hashTable[index]
            plekje_in_de_lijst = 0
            self.delete_sep(plaats, key)
        else:
            index = self.hashf(key)
            if len(self.hashTable) == 0:
                return False
            if self.hashTable[index].key != key:
                while self.hashTable[index].key != key:
                    index = self.herHashf(index)
                # self.hashTable[index] = legeNode
                self.hashTable[index] = None
            else:
                # self.hashTable[index] = legeNode
                self.hashTable[index] = None

    def isEmpty(self):
        leeg = True
        for i in self.hashTable:
            if i != None:
                leeg = False
        print(leeg)
        return leeg

    def getRetrievePosition(self, key):
        index = self.hashf(key)
        if self.hashTable[index] == key:
            return index
        else:
            if self.hashTable[index] != key:
                maxAttempts = 211
                attempts = 0
                while self.hashTable[index].key != key and attempts < maxAttempts:
                    attempts += 1
                    if self.hashTable[index].key == key:
                        return index
                    else:
                        if self.type == 1:
                            index = self.herHashf(index)
                        else:
                            index = self.herHashf(key)
                        if self.type == 2:
                            self.step += 1
                if attempts >= maxAttempts:
                    return -1
            return index

    def retrieve(self, key):
        self.step = 1

        if self.type == 3:
            return self.ll_retrieve(key)

        index = self.hashf(key)
        while self.hashTable[index] == None:
            self.herHashf(key)
        if self.count == 0:
            return (False, None)
        if self.hashTable[index].key != key:
            index = self.getRetrievePosition(key)
            if index == -1:
                return False, None
            else:
                print(True, self.hashTable[index].item)
                return True, self.hashTable[index].item
        print(True, self.hashTable[index].item)
        return True, self.hashTable[index].item



""" Voor het aanmaken van een hashmap """
def createHashmap(size, type):
    return Hashmap(int(size), int(type))

""" Voor wanneer er vanuit een file ingelezen moet worden """
def lees(file, size):
    for i in file:
        if i[0] != "#" or i[0] != "\n":
            zoek_type = i.split("=")
            if zoek_type[0] == "type":
                welke = zoek_type[1].split(" ")
                if welke[0] == "hash":
                    select = welke[1][:-1]
                    h = Hashmap(int(size), int(select))
                    h.type = int(select)
            else:
                words = i.split(" ")
                if words[0] == "insert":
                    # if type(words[1]) == int:
                    h.insert(int(words[1]), int(words[2]))
                    # else:
                    #     h.insert(words[1], int(words[2]))
                if words[0] == "print\n":
                    h.show()
                if words[0] == "delete":
                    h.delete(int(words[1]))