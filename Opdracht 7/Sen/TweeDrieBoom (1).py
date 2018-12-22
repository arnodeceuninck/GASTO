


class TweeDrieBoom():
    def __init__(self):
        self.root = []
        self.childrenLeft = None
        self.childrenRight = None
        self.childrenMiddle = None
        self.childrenMiddle2 = None
        self.parent = None
    def create23T(self):
        self.__init__()
    def destroy23T(self):
        pass
    def isEmpty(self):
        if len(self.root) == 0 and self.childrenLeft == self.childrenMiddle == self.childrenRight == self.parent == None:
            return True
    def insertItem(self, TreeItem):
        if len(self.root) == 0 and self.parent == None:
            self.root.append(TreeItem)
        elif len(self.root) == 0:
            self.root.append(TreeItem)
            self.parent = self
        elif len(self.root) == 1:
            if self.childrenLeft != None and self.childrenRight != None:
                if TreeItem.key > self.root[0].key:
                    self.childrenRight.insertItem(TreeItem)
                else:
                    self.childrenLeft.insertItem(TreeItem)
            else:
                if TreeItem.key > self.root[0].key:
                    self.root.append(TreeItem)
                else:
                    self.root.insert(0, TreeItem)
        elif len(self.root) == 2:
            if self.childrenLeft != None or self.childrenMiddle != None or self.childrenRight != None:
                if TreeItem.key > self.root[1].key:
                    self.childrenRight.insertItem(TreeItem)
                elif self.root[0].key < TreeItem.key < self.root[1].key:
                    self.childrenMiddle.insertItem(TreeItem)
                else:
                    self.childrenLeft.insertItem(TreeItem)
            else:
                if TreeItem.key > self.root[1].key:
                    self.root.append(TreeItem)
                    self.split()
                elif self.root[0].key < TreeItem.key < self.root[1].key:
                    self.root.insert(1, TreeItem)
                    self.split()
                else:
                    self.root.insert(0, TreeItem)
                    self.split()
    def split(self):
        if self.parent == None:
            NodeLeft = TweeDrieBoom()
            NodeRight = TweeDrieBoom()
            NodeLeft.childrenLeft = self.childrenLeft
            self.childrenLeft = NodeLeft
            NodeRight.childrenRight = self.childrenRight
            self.childrenRight = NodeRight
            NodeLeft.parent = self
            NodeRight.parent = self
            NodeLeft.root.append(self.root[0])
            NodeRight.root.append(self.root[2])
            self.root.remove(self.root[0])
            self.root.remove(self.root[1])
            if self.childrenMiddle != None and self.childrenMiddle2 != None:
                NodeLeft.childrenRight = self.childrenMiddle2
                NodeRight.childrenLeft = self.childrenMiddle
                NodeLeft.childrenRight.parent = NodeLeft
                NodeLeft.childrenLeft.parent = NodeLeft
                NodeRight.childrenLeft.parent = NodeRight
                NodeRight.childrenRight.parent = NodeRight
                self.childrenMiddle = None
                self.childrenMiddle2 = None
        else:
            if len(self.parent.root) == 1:
                NodeMiddle = TweeDrieBoom()
                self.parent.childrenMiddle = NodeMiddle
                NodeMiddle.parent = self.parent
                if self == self.parent.childrenLeft:
                    self.parent.root.insert(0, self.root[1])
                    NodeMiddle.root.append(self.root[2])

                    self.root.remove(self.root[1])
                    self.root.remove(self.root[1])

                    if self.childrenMiddle2 != None:
                        NodeMiddle.childrenLeft = self.childrenMiddle
                        NodeMiddle.childrenRight = self.childrenRight
                        self.childrenRight = self.childrenMiddle2
                        self.childrenMiddle = None
                        self.childrenMiddle2 = None

                elif self == self.parent.childrenRight:
                    self.parent.root.append(self.root[1])
                    NodeMiddle.root.append(self.root[0])

                    self.root.remove(self.root[0])
                    self.root.remove(self.root[0])

                    if self.childrenMiddle2 != None:
                        NodeMiddle.childrenLeft = self.childrenLeft
                        NodeMiddle.childrenRight = self.childrenMiddle2
                        self.childrenLeft = self.childrenMiddle
                        self.childrenMiddle = None
                        self.childrenMiddle2 = None

            elif len(self.parent.root) == 2:
                NodeMiddle = TweeDrieBoom()
                if self == self.parent.childrenLeft:
                    self.parent.root.insert(0, self.root[1])
                    self.root.remove(self.root[1])
                    if self.childrenMiddle2 != None:
                        NodeMiddle.root.append(self.root[1])

                        NodeMiddle.childrenLeft = self.childrenMiddle
                        NodeMiddle.childrenRight = self.childrenRight
                        self.root.remove(self.root[1])
                        self.childrenMiddle = None
                        self.childrenRight = self.childrenMiddle2
                        self.childrenMiddle2 = None

                        NodeMiddle.parent = self.parent
                        self.parent.childrenMiddle = NodeMiddle
                        self.parent.split()
                    else:
                        NodeMiddle.root.append(self.root[1])
                        self.root.remove(self.root[1])
                        self.parent.childrenMiddle2 = NodeMiddle
                        NodeMiddle.parent = self.parent
                        self.parent.split()
                elif self == self.parent.childrenMiddle:
                    self.parent.root.insert(1, self.root[1])
                    self.root.remove(self.root[1])

                    if self.childrenMiddle2 != None:
                        NodeMiddle.root.append(self.root[0])

                        NodeMiddle.childrenLeft = self.childrenLeft
                        NodeMiddle.childrenRight = self.childrenMiddle2
                        self.root.remove(self.root[0])
                        self.childrenMiddle2 = None
                        self.childrenLeft = self.childrenMiddle
                        self.childrenMiddle = None

                        NodeMiddle.parent = self.parent
                        self.parent.childrenMiddle2 = NodeMiddle
                        self.parent.split()
                    else:
                        NodeMiddle.root.append(self.root[0])
                        self.root.remove(self.root[0])
                        self.parent.childrenMiddle2 = NodeMiddle
                        self.parent.split()
                else:
                    self.parent.root.append(self.root[1])
                    self.root.remove(self.root[1])

                    if self.childrenMiddle2 != None:
                        NodeMiddle.root.append(self.root[0])

                        NodeMiddle.childrenLeft = self.childrenLeft
                        NodeMiddle.childrenRight = self.childrenMiddle2
                        self.root.remove(self.root[0])
                        self.childrenMiddle2 = None
                        self.childrenLeft = self.childrenMiddle
                        self.childrenMiddle = None

                        NodeMiddle.parent = self.parent
                        self.parent.childrenMiddle2 = self.parent.childrenMiddle
                        self.parent.childrenMiddle = NodeMiddle
                        self.parent.split()
                    else:
                        NodeMiddle.root.append(self.root[0])
                        self.root.remove(self.root[0])
                        self.parent.childrenMiddle2 = self.parent.childrenMiddle
                        NodeMiddle.parent = self.parent
                        self.parent.childrenMiddle = NodeMiddle
                        self.parent.split()
    def delete(self, key):
        if key == self.root[0].key:
            TreeItem = self.root[0]
        elif key == self.root[1].key:
            TreeItem = self.root[1]
        if TreeItem in self.root:
            if self.childrenRight == self.childrenMiddle == self.childrenMiddle2 == self.childrenLeft == None:
                self.root.remove(TreeItem)
                self.fix()
            else:
                # if len(self.root) == 1:
                #     self.root.remove(TreeItem)
                #     self.fix()
                # else:
                    if TreeItem == self.root[0]:
                        self.root[0] = self.inorder_successor(TreeItem)
                    else:
                        self.root[1] = self.inorder_successor(TreeItem)
        else:
            if key < self.root[0].key:
                self.childrenLeft.delete()
            else:
                if len(self.root) == 1:
                    self.childrenRight.delete()
                else:
                    if key < self.root[1].key:
                        self.childrenMiddle.delete()
                    else:
                        self.childrenRight.delete()
    def fix(self):
        if len(self.root) == 0:
            if self.childrenLeft != None and self.childrenRight != None:
                self.root.append(self.root.childrenLeft)
                self.root.append(self.root.childrenRight)
                self.childrenRight = self.childrenRight.childrenRight
                self.childrenLeft = self.childrenLeft.childrenLeft
                self.childrenMiddle = self.childrenRight
            else:
                self.root = self.childrenRight
                self.childrenRight.parent = None
                self.childrenRight.childrenLeft.parent = self.root
                self.childrenRight.childrenRight.parent = self.root
                self.childrenRight.childrenMiddle.parent = self.root
        else:
            if self.parent.childrenRight == self:
                if len(self.parent.root) == 1:
                    self.root.append(self.parent.root[0])
                    self.parent.root.remove(self.parent.root[0])
                    self.parent.fix()
                else:
                    self.root.append(self.parent.root[1])
                    self.parent.root[1] = self.parent.inorder_successor(self.parent.root[1])
            elif self.parent.childrenMiddle == self:
                if len(self.parent.childrenLeft) == 2:
                    self.root.append(self.parent.root[0])
                    self.parent.root[0] = self.parent.inorder_successor(self.parent.root[0])
                elif len(self.parent.childrenRight) == 2:
                    self.root.append(self.parent.root[1])
                    self.parent.root[1] = self.parent.inorder_successor(self.parent.root[1])
                else:
                    self.parent.childrenMiddle = None
                    self.childrenLeft.append(self.parent.root[0])
                    self.parent.remove(self.parent.root[0])
            else:
                if len(self.parent.root) == 1:
                    self.root.append(self.parent.root[0])
                    self.parent.root.remove(self.parent.root[0])
                    self.parent.fix()
                else:
                    self.root.append(self.parent.root[0])
                    self.parent.root[0] = self.parent.inorder_successor(self.parent.root[0])

    def inorder(self):
        if self.childrenLeft != None:
            self.childrenLeft.inorder()
        if self.childrenMiddle != None:
            self.childrenMiddle.inorder()
        if self.childrenRight != None:
            self.childrenRight.inorder()
    def inorder_successor(self, TreeItem):
        if len(self.root) == 1:
            successor = self.successor()
            return successor
        else:
            if TreeItem == self.root[0]:
                successor = self.childrenLeft.successor()
                return successor
            else:
                successor = self.childrenMiddle.succssor()
                return successor
    def successor(self):
        if self.childrenRight == None:
            if len(self.root) == 1:
                successor = self.root[0]
                self.root.remove(successor)
                # if self.parent.parent != None:
                #     self.fix()
                return successor
            else:
                successor = self.root[1]
                self.root.remove(successor)
                return successor
        else:
            self.childrenRight.successor()


class TreeItem(object):
    def __init__(self, value, key):
        self.key = key
        self.value = value




def dot(current, parent, file):

    if current.parent != None:
        # schrijf dotcode voor parent naar current_node node met als ID's:  current_count en parent_count
        if len(current.root) == 1:
            file.write(str(parent.root[0].key) + " -> " + str(current.root[0].key) + "\n")
        else:
            parentKeys = ""
            currentKeys = ""
            for keyNode in parent.root:
                parentKeys += str(keyNode.key)
                parentKeys += "|"
            parentKeys = parentKeys[:-1]
            for keyNode in current.root:
                currentKeys += str(keyNode.key)
                currentKeys += "|"
            currentKeys = currentKeys[:-1]
            file.write(str(parentKeys) + " -> " + str(currentKeys) + "\n")

    if current.childrenLeft != None:
        dot(current.childrenLeft, current, file)

    if current.childrenMiddle != None:
        dot(current.childrenMiddle, current, file)

    if current.childrenRight != None:
        dot(current.childrenRight, current, file)

def write_dot(tree):
    dotFile = open("tree.dot", "w")
    dotFile.write("digraph finite_state_machine { \n")
    dotFile.write("size=8.5\n")
    global globalCounter
    dot(tree, None, dotFile)
    dotFile.write("}")

test = TweeDrieBoom()
test.create23T()
# lijst_elements = []
# value_lijst = []
# for x in range(100):
#     key = random.randint(2, 101)
#     value = random.randint(2, 101)
#     while(key in lijst_elements):
#         key = random.randint(2, 101)
#     while(value in value_lijst):
#         value = random.randint(2, 101)
#     lijst_elements.append(key)
#     value_lijst.append(value)
#
#     test.insertItem(TreeItem(value, key))

# test.delete(6)
test.insertItem(TreeItem(1, 8))
test.insertItem(TreeItem(1, 9))
test.insertItem(TreeItem(1, 10))
test.insertItem(TreeItem(1, 11))
test.insertItem(TreeItem(1, 12))
test.insertItem(TreeItem(1, 13))
test.insertItem(TreeItem(1, 14))
test.insertItem(TreeItem(1, 15))
test.insertItem(TreeItem(1, 16))
test.insertItem(TreeItem(1, 17))
test.insertItem(TreeItem(1, 18))
test.insertItem(TreeItem(1, 19))
test.insertItem(TreeItem(1, 20))
test.insertItem(TreeItem(1, 21))
test.insertItem(TreeItem(1, 22))
test.insertItem(TreeItem(1, 23))
test.insertItem(TreeItem(1, 24))
test.insertItem(TreeItem(1, 25))
test.insertItem(TreeItem(1, 26))
test.insertItem(TreeItem(1, 27))
test.insertItem(TreeItem(1, 28))
test.insertItem(TreeItem(1, 29))
test.insertItem(TreeItem(1, 30))
test.insertItem(TreeItem(1, 40))
test.insertItem(TreeItem(1, 31))
test.insertItem(TreeItem(1, 32))
test.insertItem(TreeItem(1, 33))
test.insertItem(TreeItem(1, 34))
test.insertItem(TreeItem(1, 35))
test.insertItem(TreeItem(1, 36))
write_dot(test)

# successor = test.inorder()



