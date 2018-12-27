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
                    return_value = index_place.root[self.element]
                    self.element += 1
                    return return_value.key, return_value.item
                else:
                    self.index += 1
                    return self.__next__()
            else:
                self.index += 1
                return index_place.key, index_place.item

            self.index += 1
            return index_place.key, index_place.item

    # def getLength(self):
    #     size = 0
    #     for i in range(self.tableSize):
    #         if self.type == "hsep":
    #             if self.hashTable[i] != None:
    #                 size += len(self.hashTable[i])
    #         else:
    #             if self.hashTable[i] != None:
    #                 size += 1
    #     return size

    def hashf(self, key):
        num = 0
        if type(key) != int:
            for char in key:
                num += ord(char)
            return num % self.tableSize
        else:
            return key % self.tableSize

    def herHashf(self, key):
        num = 0
        if type(key) != int:
            for char in key:
                num += ord(char)
            key = num

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
                        print("Yay")
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
        return self.count

    def show(self):
        # i = 0
        # while i < self.tableSize:
        #     if self.hashTable[i] != None:
        #         print("Op plaats %s staat: %s" %(i, self.hashTable[i].item))
        #     else:
        #         print("Op plaats %s staat niets" %i)
        #     i += 1
        # print("\n")
        leeg = ""
        count = 0
        f = open("Hahsmap.dot", "w+")
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
        # for i in range(self.tableSize):
        #     self.hashTable[i] = None


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
        legeNode = TreeItem(None, -1)
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
                self.hashTable[index] = legeNode
            else:
                self.hashTable[index] = legeNode

    def isEmpty(self):
        leeg = True
        for i in self.hashTable:
            if i != None:
                leeg = False
        return leeg


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
            self.count -= 1


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


h = createHashmap(23, 2)
# h.insert(24, 1)
# h.insert(47, 2)
# h.insert(70, 5)
# h.insert(93, 10)

# h.insert(24, "Rob")
# h.insert(47, "Roel")
# h.insert(70, "Aline")
# h.insert(93, "Dylan")

h.insert("Rob", "Vijftien") #291 -> 15
h.insert("Bor", "Zestien") #291
h.insert("Orb", "Negentien") #291
h.insert("Bro", "Een")


h.show()