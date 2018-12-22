
class Pointer:
    def __init__(self, target):
        self.target = target

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def createQueue():
    global Front
    Front = Pointer(None)
    global Back
    Back = Pointer(None)

def destroyQueue():
    Front.target = None


def isEmpty():
    if Front.target is None:
        return True
    else:
        return False

def enqueue(value):
    newNode = Node(value)
    Last = Back.target
    if Front.target is None:
        Front.target = newNode
        Back.target = newNode
        return True
    else:
        Last.next = newNode
        Back.target = newNode
        return True


def dequeue():
    First = Front.target
    Front.target = First.next
    First.next = None
    return First.value, True


def getFront():
    return Front.target.value, True

if __name__ == '__main__':
    createQueue()
    enqueue(10)
    print(getFront())
    print(dequeue())