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
        if self.childrenLeft == None:
            if self.childrenMiddle != None:
                self.childrenMiddle.destroy23T()
            elif self.childrenRight != None:
                self.childrenRight.destroy23T()
            else:
                self.root.clear()
                if self.parent == None and self.childrenLeft == self.childrenRight == self.childrenMiddle == None:
                    del self
                elif self == self.parent.childrenLeft:
                    self.parent.childrenLeft = None
                    return self.parent.destroy23T()
                elif self == self.parent.childrenRight:
                    self.parent.childrenRight = None
                    return self.parent.destroy23T()
                else:
                    self.parent.childrenMiddle = None
                    return self.parent.destroy23T()
        else:
            return self.childrenLeft.destroy23T()
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
                        NodeMiddle.childrenLeft.parent = NodeMiddle
                        NodeMiddle.childrenRight.parent = NodeMiddle
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
                        NodeMiddle.childrenLeft.parent = NodeMiddle
                        NodeMiddle.childrenRight.parent = NodeMiddle
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
                        NodeMiddle.childrenLeft.parent = NodeMiddle
                        NodeMiddle.childrenRight.parent = NodeMiddle
                        self.root.remove(self.root[1])
                        self.childrenMiddle = None
                        self.childrenRight = self.childrenMiddle2
                        self.childrenMiddle2 = None

                        NodeMiddle.parent = self.parent
                        self.parent.childrenMiddle2 = NodeMiddle    #todo check
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
                        NodeMiddle.childrenLeft.parent = NodeMiddle
                        NodeMiddle.childrenRight.parent = NodeMiddle
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
                        NodeMiddle.childrenLeft.parent = NodeMiddle
                        NodeMiddle.childrenRight.parent = NodeMiddle
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
        check = self.zoek(key, False)   #checkt of het element in de 23T zit
        if check[0] == False:
            return False
        Treeitem = None
        if key == self.root[0].key:
            Treeitem = self.root[0]
        elif len(self.root) == 2 and self.root[1].key == key:
            Treeitem = self.root[1]
        if Treeitem != None:
            if self.childrenLeft == None:
                self.root.remove(Treeitem)
                self.fix()
            else:
                successor = self.inorder_successor(Treeitem)
                if len(self.root) == 1:
                    self.root.clear()
                    self.root.append(successor.root[0])
                    successor.root.remove(successor.root[0])
                    successor.fix()
                else:
                    if self.root[0] == Treeitem:
                        self.root.insert(0, successor.root[0])
                    else:
                        self.root.append(successor.root[0])
                    self.root.remove(Treeitem)
                    successor.root.remove(successor.root[0])
                    successor.fix()
        else:
            if key < self.root[0].key:
                self.childrenLeft.delete(key)
            else:
                if len(self.root) == 1:
                    self.childrenRight.delete(key)
                else:
                    if key < self.root[1].key:
                        self.childrenMiddle.delete(key)
                    else:
                        self.childrenRight.delete(key)
    def fix(self):
        if len(self.root) == 0:
            if self.parent == None:
                self.root = self.childrenMiddle.root
                self.childrenLeft = self.childrenMiddle.childrenLeft
                self.childrenRight = self.childrenMiddle.childrenRight
                self.childrenMiddle = self.childrenMiddle.childrenMiddle
                if self.childrenLeft != None or self.childrenMiddle != None:
                    self.childrenLeft.parent = self
                    self.childrenMiddle.parent = self
                    self.childrenRight.parent = self
            elif self.childrenMiddle != None:
                nodemiddle = TweeDrieBoom()
                nodemiddle.parent = self.parent
                if self == self.parent.childrenLeft:
                    nodemiddle.root.append(self.parent.root[0])
                    if len(self.parent.root) == 1:
                        nodemiddle.root.append(self.parent.childrenRight.root[0])
                        nodemiddle.childrenLeft = self.childrenMiddle
                        nodemiddle.childrenMiddle = self.parent.childrenRight.childrenLeft
                        nodemiddle.childrenRight = self.parent.childrenRight.childrenRight
                        self.childrenMiddle.parent = nodemiddle
                        self.parent.childrenRight.childrenLeft.parent = nodemiddle
                        self.parent.childrenRight.childrenRight.parent = nodemiddle
                        self.parent.root.clear()
                        self.parent.childrenMiddle = nodemiddle
                        self.parent.childrenLeft = None
                        self.parent.childrenRight = None
                    else:
                        nodemiddle.root.append(self.parent.childrenMiddle.root[0])
                        self.parent.root.remove(self.parent.root[0])
                        nodemiddle.childrenLeft = self.childrenMiddle
                        nodemiddle.childrenMiddle = self.parent.childrenMiddle.childrenLeft
                        nodemiddle.childrenRight = self.parent.childrenMiddle.childrenRight
                        self.childrenMiddle.parent = nodemiddle
                        self.parent.childrenMiddle.childrenLeft.parent = nodemiddle
                        self.parent.childrenMiddle.childrenRight.parent = nodemiddle
                        self.parent.childrenMiddle = None
                        self.parent.childrenLeft = nodemiddle
                elif self == self.parent.childrenRight:
                    if len(self.parent.root) == 1:
                        nodemiddle.root.append(self.parent.root[0])
                        nodemiddle.root.insert(0, self.parent.childrenLeft.root[0])
                        nodemiddle.childrenLeft = self.parent.childrenLeft.childrenLeft
                        nodemiddle.childrenMiddle = self.parent.childrenLeft.childrenRight
                        nodemiddle.childrenRight = self.childrenMiddle
                        self.childrenMiddle.parent = nodemiddle
                        self.parent.childrenRight.childrenLeft.parent = nodemiddle
                        self.parent.childrenRight.childrenRight.parent = nodemiddle
                        self.parent.root.clear()
                        self.parent.childrenMiddle = nodemiddle
                        self.parent.childrenLeft = None
                        self.parent.childrenRight = None
                    else:
                        nodemiddle.root.append(self.parent.root[1])
                        nodemiddle.root.insert(0, self.parent.childrenMiddle.root[0])
                        self.parent.root.remove(self.parent.root[1])
                        nodemiddle.childrenLeft = self.parent.childrenMiddle.childrenLeft
                        nodemiddle.childrenMiddle = self.parent.childrenMiddle.childrenRight
                        nodemiddle.childrenRight = self.childrenMiddle
                        self.childrenMiddle.parent = nodemiddle
                        self.parent.childrenMiddle.childrenLeft.parent = nodemiddle
                        self.parent.childrenMiddle.childrenRight.parent = nodemiddle
                        self.parent.childrenMiddle = None
                        self.parent.childrenRight = nodemiddle
                else:
                    if len(self.parent.childrenLeft.root) == 2 or len(self.parent.childrenRight.root) == 2:
                        if len(self.parent.childrenLeft.root) == 2:
                            self.root.append(self.parent.root[0])
                            self.parent.root.remove(self.parent.root[0])
                            self.parent.root.insert(0, self.parent.childrenLeft.root[1])
                            self.parent.childrenLeft.root.remove(self.parent.childrenLeft.root[1])
                            self.childrenRight = self.childrenMiddle
                            self.childrenMiddle = None
                            self.childrenLeft = self.parent.childrenLeft.childrenRight
                            self.childrenLeft.parent = self
                            self.parent.childrenLeft.childrenRight = self.parent.childrenLeft.childrenMiddle
                            self.parent.childrenLeft.childrenMiddle = None
                        else:
                            self.root.append(self.parent.root[1])
                            self.parent.root.remove(self.parent.root[1])
                            self.parent.root.append(self.parent.childrenRight.root[0])
                            self.parent.childrenRight.root.remove(self.parent.childrenRight.root[0])
                            self.childrenLeft = self.childrenMiddle
                            self.childrenMiddle = None
                            self.childrenRight = self.parent.childrenRight.childrenLeft
                            self.childrenRight.parent = self
                            self.parent.childrenRight.childrenLeft = self.parent.childrenRight.childrenMiddle
                            self.parent.childrenRight.childrenMiddle = None
                    else:
                        nodemiddle.root.append(self.parent.childrenLeft.root[0])
                        nodemiddle.root.append(self.parent.root[0])
                        self.parent.root.remove(self.parent.root[0])
                        nodemiddle.childrenLeft = self.parent.childrenLeft.childrenLeft
                        nodemiddle.childrenMiddle = self.parent.childrenLeft.childrenRight
                        nodemiddle.childrenRight = self.childrenMiddle
                        nodemiddle.childrenLeft.parent = nodemiddle
                        nodemiddle.childrenMiddle.parent = nodemiddle
                        nodemiddle.childrenRight.parent = nodemiddle
                        self.parent.childrenMiddle = None
                        self.parent.childrenLeft = nodemiddle
                self.parent.fix()

            else:   #base case fix
                if self == self.parent.childrenLeft and len(self.parent.childrenRight.root) == 2 and len(self.parent.root) == 1:
                    self.root.append(self.parent.root[0])
                    self.parent.root.clear()
                    self.parent.root.append(self.parent.childrenRight.root[0])
                    self.parent.childrenRight.root.remove(self.parent.childrenRight.root[0])
                elif self == self.parent.childrenRight and len(self.parent.childrenLeft.root) == 2 and len(self.parent.root) == 1:
                    self.root.append(self.parent.root[0])
                    self.parent.root.clear()
                    self.parent.root.append(self.parent.childrenRight.root[0])
                    self.parent.childrenRight.root.remove(self.parent.childrenRight.root[0])
                elif self == self.parent.childrenLeft and self.parent.childrenMiddle != None and (len(self.parent.childrenRight.root) == 2 or len(self.parent.childrenMiddle.root) == 2) and len(self.parent.root) == 2:
                    if len(self.parent.childrenRight.root) == 2:
                        self.root.append(self.parent.root[0])
                        self.parent.childrenMiddle.root.append(self.parent.root[1])
                        self.parent.root.clear()
                        self.parent.root.append(self.parent.childrenMiddle.root[0])
                        self.parent.root.append(self.parent.childrenRight.root[0])
                        self.parent.childrenRight.root.remove(self.parent.childrenRight.root[0])
                        self.parent.childrenMiddle.root.remove(self.parent.childrenMiddle.root[0])
                    else:
                        self.root.append(self.parent.root[0])
                        self.parent.root.remove(self.parent.root[0])
                        self.parent.root.insert(0, self.parent.childrenMiddle.root[0])
                        self.parent.childrenMiddle.root.remove(self.parent.childrenMiddle.root[0])
                elif self == self.parent.childrenRight and self.parent.childrenMiddle != None and (len(self.parent.childrenLeft.root) == 2 or len(self.parent.childrenMiddle.root) == 2)and len(self.parent.root) == 2:
                    if len(self.parent.childrenLeft.root) == 2:
                        self.root.append(self.parent.root[1])
                        self.parent.childrenMiddle.root.append(self.parent.root[0])
                        self.parent.root.clear()
                        self.parent.root.append(self.parent.childrenLeft.root[1])
                        self.parent.root.append(self.parent.childrenMiddle.root[0])
                        self.parent.childrenRight.root.remove(self.parent.childrenLeft.root[1])
                        self.parent.childrenMiddle.root.remove(self.parent.childrenMiddle.root[0])
                    else:
                        self.root.append(self.parent.root[1])
                        self.parent.root.remove(self.parent.root[1])
                        self.parent.root.append(self.parent.childrenMiddle.root[1])
                        self.parent.childrenMiddle.root.remove(self.parent.childrenMiddle.root[1])
                elif self == self.parent.childrenMiddle and (len(self.parent.childrenLeft.root) == 2 or len(self.parent.childrenRight.root) == 2) and len(self.parent.root) == 2:
                    if len(self.parent.childrenRight.root) == 2:
                        self.root.append(self.parent.root[0])
                        self.parent.root.remove(self.parent.root[0])
                        self.parent.root.insert(0, self.parent.childrenLeft.root[1])
                        self.parent.childrenLeft.root.remove(self.parent.childrenLeft.root[1])
                    if len(self.parent.childrenLeft.root) == 2:
                        self.root.append(self.parent.root[1])
                        self.parent.root.remove(self.parent.root[1])
                        self.parent.root.insert(0, self.parent.childrenRight.root[0])
                        self.parent.childrenRight.root.remove(self.parent.childrenRight.root[0])
                else:
                    nodemiddle = TweeDrieBoom()
                    nodemiddle.parent = self.parent
                    if self == self.parent.childrenLeft:
                        nodemiddle.root.append(self.parent.root[0])
                        nodemiddle.root.append(self.parent.childrenRight.root[0])
                        self.parent.root.clear()
                        self.parent.childrenMiddle = nodemiddle
                        self.parent.childrenLeft = None
                        self.parent.childrenRight = None
                    else:
                        self.parent.root.insert(0, self.parent.childrenLeft.root[0])
                        self.parent.childrenLeft = None
                        self.parent.childrenRight = None
                    self.parent.fix()
        else:
            pass
    def inorder_successor(self, TreeItem):
        if len(self.root) == 1:
            successor = self.childrenRight.LeftElement()
            return successor
        else:
            if TreeItem == self.root[0]:
                successor = self.childrenMiddle.LeftElement()
                return successor
            else:
                successor = self.childrenRight.LeftElement()
                return successor
    def LeftElement(self):
        node = self
        while(node.childrenLeft != None):
            node = node.childrenLeft
        return node
    def zoek(self, key, gevonden):
        if len(self.root) == 1 and self.childrenLeft == self.childrenRight == None and self.root[0].key != key:
            result = (gevonden, None)
            return result
        elif len(self.root) == 2 and self.childrenLeft == self.childrenRight == self.childrenMiddle == None and self.root[0].key != key and self.root[1] != key:
            result = (gevonden, None)
            return result
        if key == self.root[0].key:
            gevonden = True
            result = (gevonden, self.root[0])
            return result
        elif len(self.root) == 2 and self.root[1].key:
            gevonden = True
            result = (gevonden, self.root[1])
            return result
        elif key < self.root[0].key:
            return self.childrenLeft.zoek(key, gevonden)
        else:
            if len(self.root) == 1:
                return self.childrenRight.zoek(key, gevonden)
            else:
                if key < self.root[1].key:
                    return self.childrenMiddle.zoek(key, gevonden)
                else:
                    return self.childrenRight.zoek(key, gevonden)

    def retrieve(self, key):
        result = self.zoek(key, False)
        if result[0] == False:
            return False
        else:
            return result
class TreeItem(object):
    def __init__(self, value, key):
        self.key = key
        self.value = value




def dot(current, parent, file):

    if current.parent != None:
        # schrijf dotcode voor parent naar current_node node met als ID's:  current_count en parent_count
        if len(current.root) == 1:
            if len(parent.root) > 1:
                parentKeys = ""
                for keyNode in parent.root:
                    parentKeys += str(keyNode.key)
                    parentKeys += "|"
                parentKeys = parentKeys[:-1]
                file.write("\t\""+str(parentKeys) + "\" -> \"" + str(current.root[0].key) + "\";\n")
            else:
                file.write("\t\""+str(parent.root[0].key) + "\" -> \"" + str(current.root[0].key) + "\";\n")
        elif len(parent.root) > 1:
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
            file.write("\t\""+str(parentKeys) + "\" -> \"" + str(currentKeys) + "\";\n")
        else:
            currentKeys = ""
            for keyNode in current.root:
                currentKeys += str(keyNode.key)
                currentKeys += "|"
            currentKeys = currentKeys[:-1]
            file.write("\t\""+str(parent.root[0].key) + "\" -> \"" + str(currentKeys) + "\";\n")

    if current.childrenLeft != None:
        dot(current.childrenLeft, current, file)

    if current.childrenMiddle != None:
        dot(current.childrenMiddle, current, file)

    if current.childrenRight != None:
        dot(current.childrenRight, current, file)

def write_dot(file, tree):
    dotFile = open(file, "w")
    dotFile.write("digraph Two_Three_Tree { \n")
    dotFile.write("\t"+"size=8.5\n")
    global globalCounter
    dot(tree, tree.parent, dotFile)
    dotFile.write("}")

test = TweeDrieBoom()
test.create23T()
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
test.delete(8)
test.insertItem(TreeItem(1, 8))
test.delete(16)
test.insertItem(TreeItem(1, 16))
# test.delete(27)
# test.delete(30)
# test.delete(29)
# print(test.delete(50))
# print(str(test.retrieve(36)[0]))
# test.destroy23T()
write_dot("23Tree.dot", test)




