class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LL:
    def __init__(self):
        self.start = Node(None, None)

    def vrije_node(self, current_node):
        self.current = current_node
        if self.current.next == None:
            return self.current
        return None

    def insert(self, key, value):
        self.node = Node(key, value)
        if self.start.value == None and self.start.key == None:
            self.start = self.node
        else:
            while self.start.next != None:
                if self.start.next == None:
                    self.start.next = self.node
                else:
                    self.start.next = self.start.next.next


    def show(self):
        while self.start.next != None:
            print(self.start)
            self.start = self.start.next

ll = LL()
ll.insert(5, 4)
ll.insert(3, 7)
ll.insert(77, 23)
ll.insert(1, 88)
ll.insert(4, 0)
ll.insert(56, 34)
ll.insert(2, 2)
ll.show()
input()