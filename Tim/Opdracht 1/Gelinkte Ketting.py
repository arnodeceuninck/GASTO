
class Pointer:
    def __init__(self):
        self.next = None

class Node:
    def __init__(self, value, key):
        self.value = value
        self.next = None
        self.back = None
        self.key = key


def createLinkedChain():
    global head
    head = Pointer
    global dummyhead
    dummyhead = Node(None, None)
    dummyhead.index = 0
    head.next = dummyhead


def destroyChain():
    node = head.next
    for i in range(getLength()):
        while node.next is not None:
            node = node.next
            print("test", node.value)

        node = node.back
        print("test", node.value)
        del node.next



def isEmpty():
    if dummyhead.next is None:
        return True
    else:
        return False


def getLength():
    node = dummyhead
    amoutOfElements = 1
    while node.next != None:
        amoutOfElements += 1
        node = node.next
    return amoutOfElements


def traverse():
    value = []
    node = head.next
    while node != None:
        if node.value != None:
            value.append(node.value)
        node = node.next
    return value


def goback(self):
    node = self
    while node !=None:
        if node.value != None:
            print(node.value)
            node = node.back


def insert(valueinput, key):
    node = head.next
    nextNode = node.next
    newnode = Node(valueinput, key)
    while node.next != None:
        node = node.next
    node.next = newnode
    newnode.index = node.index + 1
    newnode.back = node



def delete(index):
    node = head.next
    nextnode = node.next
    while nextnode.index != index:
        node = node.next
        nextnode = node.next
        if node.next is None:
            return False
    if nextnode.next is not None:
        node.next = nextnode.next
        node = nextnode.next
        nieuweback = nextnode.next
        node.back = nieuweback.back
    else:
        node.next = None
    del nextnode
    return True


def retrieve(key):
    node = head.next
    while node.key != key:
        node = node.next
        if node is None:
            return False
    return node.value, True


def sort():
    node = dummyhead.next
    vorigeNode = node.back
    volgendeNode = node.next
    laatsteNode = 0
    temp = 0
    highest = 1
    i = 0
    if getLength() == 2:
        return
    for d in range(0, getLength()):
        highest = 0
        node = dummyhead.next
        for i in range(1, (getLength()-d)):
            if node.key > highest:
                highest = node.key
            laatsteNode = node.back
            node = node.next
        node = dummyhead.next
        while node.key != highest:
            node = node.next
            vorigeNode = node.back
            volgendeNode = node.next
        if node.next is not None:
            vorigeNode.next = volgendeNode
        node.next = None
        node.back = laatsteNode
        laatsteNode.next = node
        if volgendeNode is not None:
            volgendeNode.back = vorigeNode


def sortNew():
    node = dummyhead.next
    CopyDummy = Node(None, None)
    CopyPointer = Pointer
    CopyPointer.next = CopyDummy
    CopyBackPointer = Pointer
    CopyBackPointer.next = CopyDummy
    if getLength() == 2:
        return
    for d in range(getLength()):
        lowest = dummyhead.next.key
        node = dummyhead.next
        for i in range(getLength()-d):
            if node.key < lowest:
                node.key = lowest
        node = dummyhead.next
        while node.key != lowest:
            node = node.next
        if node.next is not None:
            node.next.back = node.back
            node.back.next = node.next
        CopyBackPointer.next.next = node
        node.back = CopyBackPointer.next
        CopyBackPointer.next = node
        node.next = None
    node = dummyhead.next
    while node.next is not None:
        node = node.next
    print("Test")
    while node.value is not None:
        node = node.back
        del node.next
    print("Test")
    dummyhead.next = CopyDummy.next
    del CopyDummy, CopyPointer, CopyBackPointer



if __name__ == '__main__':

    createLinkedChain()
    insert(20, 1)
    insert(10, 5)
    insert(40, 4)
    insert(5, 6)
    insert(60, 2)
    print(traverse())
    destroyChain()
    traverse()

    traverse()
    print("is de lijst leeg? ", isEmpty())
    print("de lengte is ", getLength())
    destroyChain()
    print("test")
    traverse()
    createLinkedChain()
    insert(100, 3)
    traverse()


