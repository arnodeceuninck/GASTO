class Node:
    def __init__(self, value, key):
        self.value = value
        self.next = None
        self.back = None
        self.key = key

class DGL:
    def __init__(self):
        self.dummy = Node(None, None)
        self.start = self.dummy
        self.dummy.back = self.start

    def __iter__(self):
        self.current = self.dummy
        return self

    def __next__(self):
        if self.current.next is None:
            raise StopIteration
        else:
            self.current = self.current.next
            return (self.current.key, self.current.value)

    def isEmpty(self):
        if self.dummy.next is None:
            return True
        else:
            return False

    def destroyList(self):
        node = self.dummy
        while node.next is not None:
            node = node.next
        while node is not self.start:
            node.next = None
            node = node.back
            node.next.back = None
        self.start.next = None
        self.start = None
        self.dummy = None
        return True

    def getLength(self):
        node = self.dummy
        counter = 0
        while node.next != None:
            counter += 1
            node = node.next
        return counter

    def traverse(self, visit, key=None):
        node = self.dummy.next
        while node is not None:
            debug = node.value
            visit(node.value, key)
            node = node.next

    def insert(self, newnode):
        node = self.dummy
        if node.next is None:
            node.next = newnode
            newnode.back = node
            return True
        node = node.next
        while True:
            if node.next is None and node.key < newnode.key:
                node.next = newnode
                newnode.back = node
                return True
            elif node.next is None and node.key > newnode.key:
                node.back.next = newnode
                newnode.back = node.back
                node.back = newnode
                newnode.next = node
                return True
            elif node.key < newnode.key:
                node = node.next
            elif node.key > newnode.key:
                newnode.back = node.back
                newnode.back.next = newnode
                node.back = newnode
                newnode.next = node
                return True
            elif node.key == newnode.key:
                return False
            else:
                node = node.next

    def delete(self, key):
        node = self.dummy
        while True:
            if node.key == key:
                if node.next is None:
                    node.back.next = None
                    node.back = None
                    del node
                    return True
                else:
                    node.back.next = node.next
                    node.next.back = node.back
                    node.next = None
                    node.back = None
                    del node
                    return True
            elif node.next is None:
                return False
            else:
                node = node.next

    def retrieve(self, key):
        node = self.dummy.next
        if node is None:
            return (False, None)

        while True:
            # debug = node.key
            if str(node.key) == str(key):
                return (True, node.value)
            elif node.next is None:
                return (False, None)
            else:
                node = node.next

    def print(self, nummer):
        f = open(nummer, "w")
        f.write("digraph 234{")
        f.write(str("node [shape=record];") + '\n' + "rankdir=LR;" + '\n')
        #f.write(str("edge[splines=" + "line" + "];" + '\n'))
        f.write(str("start[label= start];" + '\n' + "dummyhead[];" + '\n' + "start -> dummyhead;" + '\n' +
                    "dummyhead -> start;" + '\n'))
        if self.start is not None and self.dummy.next is not None:
            f.write(str("dummyhead -> " + str(self.dummy.next.key) + ";" + '\n' + str(self.dummy.next.key) +
                        " -> dummyhead;" + '\n'))
            self.dotread(f)
        f.write("}")
        f.close()

    def dotread(self, file):
        node = self.dummy.next
        file.write(str(node.key) + str("[label=" + '"' + str(node.value) + '"' + "];" + '\n'))
        node = node.next
        while node is not None:
            file.write(str(node.key) + str("[label=" + '"' + str(node.value) + '"' + "];" + '\n' + str(node.back.key) + " -> " +
                                           str(node.key) + ';' + '\n' + str(node.key) + " -> " + str(node.back.key)
                                           + ';' + '\n'))
            node = node.next
        return True


def createLinkedChain():
    return DGL()
