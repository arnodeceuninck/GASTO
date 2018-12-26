class TreeItem():
    def __init__(self, item, key):
        self.item = item
        self.key = key
        self.next = None

class Hashmap():
    def __init__(self, size, type):
        self.tableSize = size
        self.hashTable = [None] * (self.tableSize)
        self.step = 1
        self.type = type
        self.count = 0

    def hashf(self, key):
        num = 0
        if type(key) != int:
            for char in key:
                num += ord(char)
            return num % self.tableSize
        else:
            return key % self.tableSize

    def herHashf(self, key):
        if self.type == 1:
            return (key + self.step) % self.tableSize
        elif self.type == 2:
            return int((key + (self.step)**2) % self.tableSize)

    def ll_insert(self, item, key):
        treeItem = TreeItem(item, key)
        index = self.hashf(key)
        if self.hashTable[index] == None:
            self.hashTable[index] = treeItem
        else:
            if self.hashTable[index].next == None:
                self.hashTable[index].next = treeItem
            else:
                self.nu = self.hashTable[index].next
                while True:
                    if self.nu.next == None:
                        self.nu.next = treeItem
                        return False
                    self.nu = self.nu.next

    def getPosition(self, key):
        index = self.hashf(key)
        if self.hashTable[index] == None:
            return index
        else:
            if self.hashTable[index] != None:
                while self.hashTable[index] != None:
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

    def show(self):
        i = 0
        while i < self.tableSize:
            if self.hashTable[i] != None:
                print("Op plaats %s staat: %s" %(i, self.hashTable[i].item))
            else:
                print("Op plaats %s staat niets" %i)
            i += 1
        print("\n")

    def delete_sep(self, key):
        index = self.hashf(key)
        if self.hashTable[index].next == None:
            self.hashTable[index] = None
            return False
        else:
            self.nu = self.hashTable[index].next
            count = 0
            while True:
                if self.nu.next == None and self.nu.key == key:
                    next_str = ".next"
                    for i in range(count+1):
                        self.aj = "self.hashTable[index].next" + next_str
                    self.aj = None
                    return False
                else:
                    count += 1
                    self.nu = self.nu.next


    def delete(self, key):
        self.count -= 1
        if self.type == 3:
            self.delete_sep(key)
        else:
            index = self.hashf(key)
            if len(self.hashTable) == 0:
                return False
            if self.hashTable[index].key != key:
                while self.hashTable[index].key != key:
                    index = self.herHashf(index)
                self.hashTable[index] = None
            else:
                self.hashTable[index] = None

    def retrieve(self, key):
        index = self.hashf(key)
        if len(self.hashTable) == 0:
            return False
        if self.hashTable[index].key != key:
            while self.hashTable[index].key != key:
                index = self.herHashf(index)
            print(self.hashTable[index].item)
        else:
            print(self.hashTable[index].item)

    def insert(self, key, item):
        self.count += 1
        if self.type == 3:
            self.ll_insert(item, key)
        elif self.count < self.tableSize + 1:
            treeItem = TreeItem(item, key)
            self.step = 1
            self.hashTable[self.getPosition(key)] = treeItem
        else:
            print("Je kan maximaal %s items inserten! Item (%s, %s) is niet geinsert geweest." %(self.tableSize, key, item))

def createHashmap(size, type):
    return Hashmap(int(size), int(type))

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


# file = open("sep_test.txt", "r")
# size = input("Hoe groot moet de hashmap worden? ")
# type = 1
# print(createHashmap(size, type))


#lees(file, size)
#select = input("Wilt u linair probing (1), qwadratic probing (2) of seperate chaining (3) gebruiken? ")
# h = Hashmap(int(size), int(select))
# input()

# h.show()
# h.deleteHashmap()
# input()
