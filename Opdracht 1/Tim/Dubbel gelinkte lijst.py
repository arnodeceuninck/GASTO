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

    def isEmpty(self):
        if self.dummy.next is None:
            return True
        else:
            return False

    def getLength(self):
        node = self.dummy
        counter = 0
        while node.next != None:
            counter += 1
            node = node.next
        return counter

    def traverse(self):
        values = []
        node = self.dummy.next
        while dummy.next != None:
            values.append(node.value)
            node = node.next
        return values

    def insert(self, newnode):
        node = self.dummy
        while True:
            if node.next is None:
                node.next = newnode
                newnode.back = node
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
            if node.next is None:
                return False
            elif node.key == key:
                if node.next is None:
                    node.back.next = None
                    node.back = None
                    return True
                else:
                    node.back.next = node.next
                    node.next.back = node.back
                    node.next = None
                    node.back = None
                    return True
            else:
                node = node.next

    def retrieve(self, key):
        node = self.dummy.next
        if node is None:
            return False

        while True:
            if node.key == key:
                return node.value
            elif node.next is None:
                return False
            else:
                node = node.next

    





def createLinkedChain():
    return DGL