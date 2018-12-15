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
        if len(self.root_value) == len(self.childrenLeft) == len(self.childrenMiddle) == len(self.childrenRight) == 0 and self.parent == None:
            return True
    def insertItem(self, TreeItem):
        if len(self.root) == 0 and self.parent == None:
            self.root.append(TreeItem)
        elif len(self.root) == 0:
            self.root.append(TreeItem)
            self.parent = self
        elif len(self.root) == 1:
            if self.childrenLeft != None or self.childrenRight != None:
                if TreeItem.value > self.root[0].value:
                    self.childrenRight.insertItem(TreeItem)
                else:
                    self.childrenLeft.insertItem(TreeItem)
            else:
                if TreeItem.value > self.root[0].value:
                    self.root.append(TreeItem)
                else:
                    self.root.insert(0, TreeItem)
        elif len(self.root) == 2:
            if self.childrenLeft != None or self.childrenMiddle != None or self.childrenRight != None:
                if TreeItem.value > self.root[1].value:
                    self.childrenRight.insertItem(TreeItem)
                elif self.root[0].value < TreeItem.value < self.root[1].value:
                    self.childrenMiddle.insertItem(TreeItem)
                else:
                    self.childrenLeft.insertItem(TreeItem)
            else:
                if TreeItem.value > self.root[1].value:
                    self.root.append(TreeItem)
                    self.split()
                elif self.root[0].value < TreeItem.value < self.root[1].value:
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
                        NodeMiddle.childrenLeft = self.childrenMiddle
                        NodeMiddle.childrenRight = self.childrenRight
                        self.childrenRight = self.childrenMiddle2
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
                        self.parent.childrenMiddle2 = NodeMiddle
                        self.parent.split()







class TreeItem(object):
    def __init__(self, value, key):
        self.key = key
        self.value = value


test = TweeDrieBoom()
test.create23T()
test.insertItem(TreeItem(20, 5))
test.insertItem(TreeItem(40, 6))
test.insertItem(TreeItem(30, 7))
test.insertItem(TreeItem(50, 8))
test.insertItem(TreeItem(10, 9))
test.insertItem(TreeItem(60, 10))
test.insertItem(TreeItem(5, 11))
test.insertItem(TreeItem(1, 12))
test.insertItem(TreeItem(15, 13))


