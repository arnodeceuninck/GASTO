
class Pointer:
    def __init__(self, target):
        self.target = target

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def createQueue(self):
        self.Front = Pointer(None)
        self.Back = Pointer(None)
        return self

    def destroyQueue(self):
        self.Front.target = None


    def isEmpty(self):
        if self.Front.target is None:
            return True
        else:
            return False

    def enqueue(self, value):
        newNode = Node(value)
        self.Last = self.Back.target
        if self.Front.target is None:
            self.Front.target = newNode
            self.Back.target = newNode
            return True
        else:
            Last.next = newNode
            Back.target = newNode
            return True


    def dequeue(self):
        First = self.Front.target
        self.Front.target = First.next
        First.next = None
        return First.value, True


    def getFront(self):
        if not self.isEmpty():
            return True, self.Front.target.value
        return False, None

    def getLenght(self):
        size = 0
        node = self.getFront()
        while node is not None:
            size += 1
            node = node.next


if __name__ == '__main__':
    q = Queue()
    q.createQueue()
    q.enqueue(10)
    print(q.getFront())
    print(q.dequeue())