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

    def lees(self, file):
        for i in file:
            if i[0] != "#":
                words = i.split("- ")
                print(words[0])
                print(words[1])
            else:
                print("Oei")

    def delete(self, key):
        self.count -= 1
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


size = input("Hoe groot moet de hashmap worden? ")
select = input("Wilt u linair probing (1), qwadratic probing (2) of seperate chaining (3) gebruiken? ")
h = Hashmap(int(size), int(select))

file = open("test.txt", "r")
h.lees(file)

#h.insert(searchKey, item)
### (1) ###
# h.insert(66, 0)
# h.insert(63, 8)
# h.insert(71, 5)
# h.insert(10, 10)
# h.insert(93, 6)
# h.insert(28, 7)
# h.insert(18, 9)
# h.insert(72, 1)
# h.insert(71, 2)
# h.insert(5, 3)
# h.insert(12, 4)
# h.delete(12)
# h.insert(12, 345334353)
# h.insert(24, 3453)
# h.retrieve(12)
# h.delete(18)

### (1) delete met aanpassingen aan het invoeren ###
# h.insert(66, 0)
# h.insert(63, 8)
# h.insert(71, 5)
# h.insert(10, 10)
# h.delete(71)
# h.insert(93, 5)
# h.insert(28, 6)
# h.insert(18, 7)
# h.insert(72, 9)
# h.insert(71, 1)
# h.insert(5, 2)
# h.insert(12, 3)

### (2) ###
# h.insert(66, 0)
# h.insert(63, 8)
# h.insert(71, 5)
# h.insert(10, 10)
# h.insert(93, 6)
# h.insert(28, 7)
# h.insert(18, 1)
# h.insert(72, 4)
# h.insert(71, 9)
# h.insert(5, 3)
# h.insert(12, 2)
# h.retrieve(12)
# h.delete(66)



### (3) ###
# h.insert(66, 0)
# h.insert(63, 8)
# h.insert(71, 5)
# h.insert(10, 10)
# h.insert(93, 5)
# h.insert(28, 6)
# h.insert(18, 7)
# h.insert(72, 6)
# h.insert(71, 5)
# h.insert(5, 5)
# h.insert(12, 1)
# h.retrieve(12)
# h.delete(66)

### (3 1 lange ketting) ###
# h.insert(71, 0)
# h.insert(5, 8)
# h.insert(49, 5)
# h.insert(71, 10)
# h.insert(27, 5)
# h.insert(5, 6)
# h.insert(18, 7)
# h.insert(71, 6)
# # h.delete(5)
# h.insert(5, 5)
# h.insert(5, 5)
# h.insert(12, 1)
# h.retrieve(18)
# # h.delete(18)

h.show()
# h.deleteHashmap()
# input()
