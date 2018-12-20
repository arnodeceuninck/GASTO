class Node:
    def __init__(self, value):
        self.value = value
        self.below = None


class stack:
    def __init__(self):
            self.stackpointer = None

    def push(self, new):
        new.below = self.stackpointer
        self.stackpointer = new
        return

    def pop(self):
        if self.stackpointer is None:
            return False
        temp = self.stackpointer
        self.stackpointer = self.stackpointer.below
        return temp.value

    def getTop(self):
        return self.stackpointer.value

def createstack():
    return stack()

test = createstack()
test.push(Node(70))
test.push(Node(80))
test.push(Node(45))
test.pop()
test.push(Node(90))
print(test.pop())
test.pop()
print("End")
