
class TreeItem:
    def __init__(self, item, key):
        self.item = item
        self.key = key


class T234:
    def __init__(self, item1, item2, item3, left, mleft, mright, right, parent):
        self.parent = parent
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.left = left
        self.mleft = mleft
        self.mright = mright
        self.right = right

    def __iter__(self):  # todo check
        self.index = 0
        return self

    def __next__(self): #todo check
        size = self.size()
        if size > self.index:
            x = self.getIndex(self.index)
            self.index += 1
            return (x[0].key, x[0].item)
        else:
            raise StopIteration

    def change(self):
        while self.parent is not None:
            self = self.parent

    def isEmpty(self):
        if self.item1 is None and self.item2 is None and self.item3 is None and self.left is None:
            return True
        return False

    def destroyNode(self):
        self.left = None
        self.mleft = None
        self.mright = None
        self.right = None
        self.item1 = None
        self.item2 = None
        self.item3 = None
        self.parent = None

    def split(self):
        if self.parent is None: #als we in de root zitten
            if self.left is None:#als de root geen kinderen heeft
                self.left = T234(self.item1, None, None, None, None, None, None, self)
                self.mleft = T234(self.item3, None, None, None, None, None, None, self)
                self.item1 = self.item2
                self.item2 = None
                self.item3 = None
                return True
            else: #als de root wel kinderen heeft
                self.left.parent = None
                self.mleft.parent = None
                self.mright.parent = None
                self.right.parent = None
                self.left = T234(self.item1, None, None, self.left, self.mleft, None, None, self)
                self.mleft = T234(self.item3, None, None, self.mright, self.right, None, None, self)
                self.left.left.parent = self.left
                self.left.mleft.parent = self.left
                self.mleft.left.parent = self.mleft
                self.mleft.mleft.parent = self.mleft
                self.item1 = self.item2
                self.item2 = None
                self.item3 = None
                self.mright = None
                self.right = None
                return True
        else: #als we niet de root zitten
            if self.parent.mright is None: #als de parent maar 2 kinderen heeft
                if self.parent.left == self: #als we het over het linker kind hebben
                    self.parent.item2 = self.parent.item1
                    self.parent.item1 = self.item2
                    self.parent.mright = self.parent.mleft
                    if self.left is not None:#als we kinderen hebben
                        self.parent.mleft = T234(self.item3, None, None, self.mright, self.right, None, None, self.parent)
                        self.mright.parent = self.parent.mleft
                        self.right.parent = self.parent.mleft
                        self.mright = None
                        self.right = None
                        self.item3 = None
                        self.item2 = None
                        return True
                    else:
                        self.parent.mleft = T234(self.item3, None, None, None, None, None, None, self.parent)
                        self.item3 = None
                        self.item2 = None
                        return True
                else:
                    self.parent.item2 = self.item2
                    self.parent.mright = self
                    if self.left is not None:
                        self.parent.mleft = T234(self.item1, None, None, self.left, self.mleft, None, None, self.parent)
                        self.left.parent = self.parent.mleft
                        self.mleft.parent = self.parent.mleft
                        self.left = self.mright
                        self.mleft = self.right
                        self.mright = None
                        self.right = None
                        self.item1 = self.item3
                        self.item2 = None
                        self.item3 = None
                        return True
                    else:
                        self.parent.mleft = T234(self.item1, None, None, None, None, None, None, self.parent)
                        self.item1 = self.item3
                        self.item2 = None
                        self.item3 = None
                        return True
            else: #als de parent 3 kinderen heeft
                if self.parent.left == self: #als we het linker kind zijn
                    self.parent.item3 = self.parent.item2
                    self.parent.item2 = self.parent.item1
                    self.parent.item1 = self.item2
                    self.parent.right = self.parent.mright
                    self.parent.mright = self.parent.mleft
                    if self.left is not None: #als de node kinderen heeft
                        self.parent.mleft = T234(self.item3, None, None, self.mright, self.right, None, None, self.parent)
                        self.mright.parent = self.parent.mleft
                        self.right.parent = self.parent.mleft
                        self.item3 = None
                        self.item2 = None
                        self.mright = None
                        self.right = None
                        return True
                    else:
                        self.parent.mleft = T234(self.item3, None, None, None, None, None, None,
                                                  self.parent)
                        self.item3 = None
                        self.item2 = None
                        return True
                elif self.parent.mleft == self:
                    self.parent.item3 = self.parent.item2
                    self.parent.item2 = self.item2
                    self.parent.right = self.parent.mright
                    if self.left is not None:
                        self.parent.mright = T234(self.item3, None, None, self.mright, self.right, None, None, self.parent)
                        self.mright.parent = self.parent.mright
                        self.right.parent = self.parent.mright
                        self.item3 = None
                        self.item2 = None
                        self.mright = None
                        self.right = None
                        return True
                    else:
                        self.parent.mright = T234(self.item3, None, None, None, None, None, None,
                                                   self.parent)
                        self.item3 = None
                        self.item2 = None
                        return True
                else:
                    self.parent.item3 = self.item2
                    self.parent.right = self
                    if self.left is not None:
                        self.parent.mright = T234(self.item1, None, None, self.left, self.mleft, None, None,
                                                   self.parent)
                        self.item1 = self.item3
                        self.item2 = None
                        self.item3 = None
                        self.left.parent = self.parent.mright
                        self.mleft.parent = self.parent.mright
                        self.mleft = self.mright
                        self.left = self.right
                        self.mright = None
                        self.right = None
                        return True
                    else:
                        self.parent.mright = T234(self.item1, None, None, None, None, None, None,
                                                   self.parent)
                        self.item1 = self.item3
                        self.item2 = None
                        self.item3 = None
                        return True


    def T234Insert(self, treeitem):
        if self.isEmpty():
            self.item1 = treeitem
            return True
        if self.item1 is not None and self.item2 is not None and self.item3 is not None:
            self.split()
            if self.parent is not None:
                self = self.parent
        if self.left is None:
            if self.item2 is not None:
                if treeitem.key < self.item1.key:
                    self.item3 = self.item2
                    self.item2 = self.item1
                    self.item1 = treeitem
                    return True
                elif treeitem.key < self.item2.key:
                    self.item3 = self.item2
                    self.item2 = treeitem
                    return True
                else:
                    self.item3 = treeitem
                    return True
            else:
                if treeitem.key < self.item1.key:
                    self.item2 = self.item1
                    self.item1 = treeitem
                    return True
                else:
                    self.item2 = treeitem
                    return True
        elif treeitem.key < self.item1.key:
            self.left.T234Insert(treeitem)
        elif self.item2 is None or treeitem.key > self.item1.key and treeitem.key < self.item2.key:
            self.mleft.T234Insert(treeitem)
        elif self.item3 is None or treeitem.key > self.item2.key and treeitem.key < self.item3.key:
            self.mright.T234Insert(treeitem)
        elif treeitem.key > self.item3.key:
            self.right._234TInsert(treeitem)

    def inorder1(self):
        target = self.mleft
        while target.left is not None:
            target = target.left
        return target

    def inorder2(self):
        target = self.mright
        while target.left is not None:
            target = target.left
        return target

    def inorder3(self):
        target = self.right
        while target.left is not None:
            target = target.left
        return target

    def redistributeleft(self):
        self.item1 = self.parent.item1
        self.parent.item1 = self.parent.mleft.item1
        self.parent.mleft.item1 = self.parent.mleft.item2
        self.parent.mleft.item2 = None
        if self.parent.mleft.item3 is not None:
            self.parent.mleft.item2 = self.parent.mleft.item3
            self.parent.mleft.item3 = None

    def redistributeright(self):
        self.item1 = self.parent.item3
        if self.parent.mright.item3 is None:
            self.parent.item3 = self.parent.mright.item2
            self.parent.mright.item2 = None
        else:
            self.parent.item3 = self.parent.mright.item3
            self.parent.mright.item3 = None

    def redistributemleft(self, sibling):
        if sibling == self.parent.left:
            self.item1 = self.parent.item1
            if self.parent.left.item3 is None:
                self.parent.item1 = self.parent.left.item2
                self.parent.left.item2 = None
            else:
                self.parent.item1 = self.parent.left.item3
                self.parent.left.item3 = None
        else:
            self.item1 = self.parent.item2
            if self.parent.mright.item3 is None:
                self.parent.item2 = self.parent.mright.item1
                self.parent.mright.item1 = self.parent.mright.item2
                self.parent.mright.item2 = None
            else:
                self.parent.item2 = self.parent.mright.item1
                self.parent.mright.item1 =self.parent.mright.item2
                self.parent.mright.item2 = self.parent.mright.item3
                self.parent.mright.item3 = None

    def redistributemright(self, sibling):
        if sibling == self.parent.mleft:
            self.item1 = self.parent.item2
            if self.parent.mleft.item3 is None:
                self.parent.item2 = self.parent.mleft.item2
                self.parent.mleft.item2 = None
            else:
                self.parent.item2 = self.parent.mleft.item3
                self.parent.mleft.item3 = None
        else:
            self.item1 = self.parent.item3
            if self.parent.right.item3 is None:
                self.parent.item3 = self.parent.right.item1
                self.parent.right.item1 = self.parent.right.item2
                self.parent.right.item2 = None
            else:
                self.parent.item3 = self.parent.right.item1
                self.parent.right.item1 = self.parent.right.item2
                self.parent.right.item2 = self.parent.right.item3
                self.parent.mright.item3 = None

    def redistributeInternalleft(self):
        self.item1 = self.parent.item1
        self.parent.item1 = self.parent.mleft.item1
        self.parent.mleft.item1 = self.parent.mleft.item2
        self.mleft = self.parent.mleft.left
        self.parent.mleft.left.parent = self
        self.parent.mleft.left = self.parent.mleft.mleft
        self.parent.mleft.mleft = self.parent.mleft.mright
        if self.parent.mleft.item3 is None:
            self.parent.mleft.item2 = None
            self.parent.mleft.mright = None
        else:
            self.parent.mleft.item2 = self.parent.mleft.item3
            self.parent.mleft.item3 = None
            self.parent.mleft.mright = self.parent.mleft.right
            self.parent.mleft.right = None

    def redistributeInternalmleft(self, sibling):
        if sibling == self.parent.left:
            self.item1 = self.parent.item1
            self.mleft = self.left
            if self.parent.left.item3 is None:
                self.parent.item1 = self.parent.left.item2
                self.parent.left.item2 = None
                self.left = self.parent.left.mright
                self.parent.left.mright.parent = self
                self.parent.left.mright = None
            else:
                self.parent.item1 = self.parent.left.item3
                self.parent.left.item3 = None
                self.left = self.parent.left.right
                self.parent.left.right.parent = self
                self.parent.left.right = None
        else:
            self.item1 = self.parent.item2
            self.parent.item2 = self.parent.mright.item1
            self.parent.mright.item1 = self.parent.mright.item2
            self.mleft = self.parent.mright.left
            self.parent.mright.left.parent = self
            self.parent.mright.left = self.parent.mright.mleft
            self.parent.mright.mleft = self.parent.mright.mright
            if self.parent.mright.item3 is None:
                self.parent.mright.item2 = None
                self.parent.mright.mright = None
            else:
                self.parent.mright.item2 = self.parent.mright.item3
                self.parent.mright.item3 = None
                self.parent.mright.mright = self.parent.mright.right
                self.parent.mright.right = None

    def redistributeInternalmright(self, sibling):
        if sibling == self.parent.mleft:
            self.item1 = self.parent.item2
            self.mleft = self.left
            if self.parent.mleft.item3 is None:
                self.parent.item1 = self.parent.mleft.item2
                self.parent.mleft.item2 = None
                self.left = self.parent.mleft.mright
                self.parent.mleft.mright.parent = self
                self.parent.mleft.mright = None
            else:
                self.parent.item1 = self.parent.mleft.item3
                self.parent.mleft.item3 = None
                self.left = self.parent.mleft.right
                self.parent.mleft.right.parent = self
                self.parent.mleft.right = None
        else:
            self.item1 = self.parent.item3
            self.parent.item1 = self.parent.right.item1
            self.parent.right.item1 = self.parent.right.item2
            self.mleft = self.parent.right.left
            self.parent.right.left.parent = self
            self.parent.right.left = self.parent.right.mleft
            self.parent.right.mleft = self.parent.right.mright
            if self.parent.right.item3 is None:
                self.parent.right.item2 = None
                self.parent.right.mright = None
            else:
                self.parent.right.item2 = self.parent.right.item3
                self.parent.right.item3 = None
                self.parent.right.mright = self.parent.right.right
                self.parent.right.right = None

    def redistributeInternalright(self):
        self.item1 = self.parent.item3
        self.mleft = self.left
        if self.parent.mright.item3 is None:
            self.parent.item3 = self.parent.mright.item2
            self.parent.mright.item2 = None
            self.left = self.parent.mright.mright
            self.parent.mright.mright.parent = self
            self.parent.mright.mright = None
        else:
            self.parent.item3 = self.parent.mright.item3
            self.parent.mright.item3 = None
            self.left = self.parent.mright.right
            self.parent.mright.right.parent = self
            self.parent.mright.right = None

    def mergeitemleft(self):
        self.parent.mleft.item2 = self.parent.mleft.item1
        self.parent.mleft.item1 = self.parent.item1
        self.parent.item1 = None
        self.parent.left = self.parent.mleft
        self.parent.mleft = None
        if self.parent.item2 is not None:
            self.parent.item1 = self.parent.item2
            self.parent.item2 = None
            self.parent.mleft = self.parent.mright
            self.parent.mright = None
        if self.parent.item3 is not None:
            self.parent.item2 = self.parent.item3
            self.parent.item3 = None
            self.parent.mright= self.parent.right
            self.parent.right = None

    def mergeitemmleft(self, sibling, parent):
        sibling.item2 = parent.item1
        parent.item1 = None
        parent.mleft = None
        if parent.item2 is not None:
            parent.item1 = parent.item2
            parent.item2 = None
            parent.mleft = parent.mright
            parent.mright = None
        if parent.item3 is not None:
            parent.item2 = parent.item3
            parent.item3 = None
            parent.mright = parent.right
            parent.right = None

    def mergeitemmright(self):
        self.parent.mleft.item2 = self.parent.item2
        self.parent.item2 = None
        self.mright = None
        if self.parent.item3 is not None:
            self.parent.item2 = self.parent.item3
            self.parent.item3 = None

    def mergeitemright(self):
        self.parent.mright.item2 = self.parent.item3
        self.parent.item3 = None
        self.parent.right = None

    def mergeInternalLeft(self):
        self.parent.mleft.item2 = self.parent.mleft.item1
        self.parent.mleft.item1 = self.parent.item1
        self.parent.item1 = None
        self.parent.left = self.parent.mleft
        self.parent.mleft = None
        self.parent.left.mright = self.parent.left.mleft
        self.parent.left.mleft = self.parent.left.left
        self.parent.left.left = self.left
        if self.parent.item2 is not None:
            self.parent.item1 = self.parent.item2
            self.parent.item2 = None
            self.parent.mleft = self.parent.mright
            self.parent.mright = None
        if self.parent.item3 is not None:
            self.parent.item2 = self.parent.item3
            self.parent.item3 = None
            self.parent.mright = self.parent.right
            self.parent.right = None

    def mergeInternalmleft(self):
        self.parent.left.item2 = self.parent.item1
        self.parent.item1 = None
        self.left.parent = self.parent.left
        self.parent.left.mright = self.left
        self.left = None
        self.parent.mleft = None
        if self.parent.item2 is not None:
            self.parent.item1 = self.parent.item2
            self.parent.item2 = None
            self.parent.mleft = self.parent.mright
            self.parent.mright = None
        if self.parent.item3 is not None:
            self.parent.item2 = self.parent.item3
            self.parent.item3 = None
            self.parent.mright = self.parent.right
            self.parent.right = None

    def mergeInternalmright(self):
        self.parent.mleft.item2 = self.parent.item2
        self.parent.item2 = None
        self.left.parent = self.parent.mleft
        self.parent.mleft.mright = self.left
        self.left = None
        self.mright = None
        if self.parent.item3 is not None:
            self.parent.item2 = self.parent.item3
            self.parent.item3 = None
            self.parent.mright = self.parent.right
            self.parent.right = None

    def mergeInternalright(self):
        self.parent.mright.item2 = self.parent.item2
        self.parent.item2 = self.parent.item3
        self.parent.item3 = None
        self.left.parent = self.parent.mright
        self.parent.mright.mleft = self.left
        self.left = None
        self.parent.right = None

    def fixtree(self):
        if self.parent is None and self.left is None and self.item1 is None:
            return True
        if self.parent is None:
            self.item1 = self.left.item1
            self.left.item1 = None
            self.left.mleft.parent = self
            self.mleft = self.left.mleft
            self.left.mleft = None
            if self.left.item2 is not None:
                self.item2 = self.left.item2
                self.left.item2 = None
                self.left.mright.parent = self
                self.mright = self.left.mright
                self.left.mright = None

            if self.left.item3 is not None:
                self.item3 = self.left.item3
                self.left.item3 = None
                self.left.right.parent = self
                self.right = self.left.right
                self.left.right = None
            self.left.left.parent = self
            temp = self.left
            self.left = self.left.left
            temp.left = None

        else:

            if self.parent.left is not None and self == self.parent.left and self.parent.mleft.item2 is not None:
                if self.left is None:
                    self.redistributeleft()
                else:
                    self.redistributeInternalleft()

            elif self.parent.mleft is not None and self == self.parent.mleft and (self.parent.left.item2 is not None
                                                                             or (self.parent.mright is not None and
                                                                                 self.parent.mright.item2
                                                                                 is not None)):
                if self.left is None:
                    if self.parent.left.item2 is not None:
                        self.redistributemleft(self.parent.left)
                    elif self.parent.mright is not None and self.parent.mright.item2 is not None:
                        self.redistributemleft(self.parent.mright)
                else:
                    if self.parent.left.item2 is not None:
                        self.redistributeInternalmleft(self.parent.left)
                    elif self.parent.mright is not None and self.parent.mright.item2 is not None:
                        self.redistributeInternalmleft(self.parent.mright)

            elif self.parent.mright is not None and self == self.parent.mright and (self.parent.mleft.item2 is not None
                                                                                    or (self.parent.right is not None
                                                                                        and self.parent.right.item2
                                                                                        is not None)):
                if self.left is None:
                    if self.parent.mleft is not None:
                        self.redistributemright(self.parent.mleft)
                    elif self.parent.right is not None and self.parent.right.item2 is not None:
                        self.redistributemright(self.parent.right)
                else:
                    if self.parent.mleft.item2 is not None:
                        self.redistributemright(self.parent.mleft)
                    elif self.parent.right is not None and self.parent.right.item2 is not None:
                        self.redistributeInternalmright(self.parent.right)

            elif self.parent.right is not None and self == self.parent.right and self.parent.mright.item2 is not None:
                if self.left is None:
                    self.redistributeright()
                else:
                    self.redistributeInternalright()
            else:
                if self.parent.left == self:
                    if self.left is not None:
                        self.mergeInternalLeft()
                    else:
                        self.mergeitemleft()
                elif self.parent.mleft == self:
                    if self.left is not None:
                        self.mergeInternalmleft()
                    else:
                        self.mergeitemmleft(self.parent.left, self.parent)
                elif self.parent.mright == self:
                    if self.left is not None:
                        self.mergeInternalmright()
                    else:
                        self.mergeitemmright()
                elif self.parent.right == self:
                    if self.left is not None:
                        self.mergeInternalright()
                    else:
                        self.mergeitemmright()

                parent = self.parent
                self.parent = None
                if parent.item1 is None:
                    parent.fixtree()
                del self


    def T234Delete(self, key):
        if self.item1.key == key:
            if self.left is None:
                if self.item2 is None:
                    self.item1 = None
                elif self.item3 is not None:
                    self.item1 = self.item2
                    self.item2 = self.item3
                    self.item3 = None
                else:
                    self.item1 = self.item2
                    self.item2 = None
            else:
                inordernode = self.inorder1()
                temp = self.item1
                self.item1 = inordernode.item1
                inordernode.item1 = temp
                inordernode.T234Delete(key)

            if self.item1 is None:
                self.fixtree()

        elif self.item2 is not None and self.item2.key == key:
            if self.left is None:
                if self.item3 is not None:
                    self.item2 = self.item3
                    self.item3 = None
                else:
                    self.item2 = None
            else:
                inordernode = self.inorder2()
                temp = self.item2
                self.item2 = inordernode.item1
                inordernode.item1 = temp
                inordernode.T234Delete(key)

        elif self.item3 is not None and self.item3.key == key:
            if self.left is None:
                self.item3 = None
            else:
                inordernode = self.inorder3()
                temp = self.item2
                self.item2 = inordernode.item1
                inordernode.item1 = temp
                inordernode.T234Delete(key)
        elif key < self.item1.key:
            self.left.T234Delete(key)

        elif self.item2 is None or key < self.item2.key:
            self.mleft.T234Delete(key)

        elif self.item3 is None or key < self.item3.key:
            self.mright.T234Delete(key)

        else:
            self.right.T234Delete(key)

    def retrieve(self, key):
        if self.item1 is not None and self.item1.key == key:
            return (True, self.item1.item)
        elif self.item2 is not None and self.item2.key == key:
            return (True, self.item2.item)
        elif self.item3 is not None and self.item3.key == key:
            return (True, self.item3.item)
        elif self.left is not None and key < self.item1.key:
            return self.left.retrieve(key)

        elif self.mleft is not None and (self.item2 is None or key < self.item2.key):
            return self.mleft.retrieve(key)

        elif self.mright is not None and (self.item3 is None or key < self.item3.key):
            return self.mright.retrieve(key)

        elif self.right is not None:
            return self.right.retrieve(key)

        else:
            return (False, None)

    def getRoot(self):
        if self.item1 is None:
            return
        elif self.item2 is None:
            return tuple(self.item1)
        elif self.item3 is None:
            return tuple(self.item1, self.item2)
        else:
            return tuple(self.item1, self.item2, self.item3)

    def print(self, nummer):
        f = open("234-" + str(nummer) + ".dot", "w")
        f.write("digraph 234{")
        f.write(str("node [shape=record];") + '\n')
        f.write(str("edge[splines=" + "line" + "];" + '\n'))
        if self.isEmpty():
            self.dotread(f)
        f.write("}")
        f.close()

    def dotread(self, file):
        if self.item3 is not None:
            file.write(str(self.item1.key) + str("[label=" + '"' + "<left> " + str(self.item1.key) +
                                                 "|<middle> " + str(self.item2.key) + "|<right> " + str(self.item3.key) +
                                                 '"' + "];") + '\n')
        elif self.item2 is not None:
            file.write(str(self.item1.key) + str("[label=" + '"' + "<left> " + str(self.item1.key) +
                                                 "|<middle> " + str(self.item2.key) + '"' + "];") + '\n')
        elif self.item1 is not None:
            file.write(str(self.item1.key) + str("[label=" + '"' + "<left> " + str(self.item1.key) + '"' + "];") + '\n')
        else:
            return

        if self.left is not None:
            self.left.dotread(file)
            file.write(str(self.item1.key) + " -> " + str(self.left.item1.key) + ";" + '\n')

        if self.mleft is not None:
            self.mleft.dotread(file)
            file.write(str(self.item1.key) + " -> " + str(self.mleft.item1.key) + ";" + '\n')

        if self.mright is not None:
            self.mright.dotread(file)
            file.write(str(self.item1.key) + " -> " + str(self.mright.item1.key) + ";" + '\n')

        if self.right is not None:
            self.right.dotread(file)
            file.write(str(self.item1.key) + "-> " + str(self.right.item1.key) + ";" + '\n')

    def destroySearchtree(self):
        if self.left is not None:
            self.left.destroySearchtree()

        if self.mleft is not None:
            self.mleft.destroySearchtree()

        if self.mright is not None:
            self.mright.destroySearchtree()

        if self.right is not None:
            self.right.destroySearchtree()

        return self.destroyNode()

    def traverse(self, visit, key=None):
        self.inorderTraversal(visit, key)

    def inorderTraversal(self, visit, key=None):
        if self.left is not None:
            self.left.inorderTraversal(visit, key)
        if self.item1 is not None:
            visit(self.item1.item, key)
        if self.mleft is not None:
            self.mleft.inorderTraversal(visit, key)
        if self.item2 is not None:
            visit(self.item2.item, key)
        if self.mright is not None:
            self.mright.inorderTraversal(visit, key)
        if self.item3 is not None:
            visit(self.item3.item, key)
        if self.right is not None:
            self.right.inorderTraversal(visit, key)

    def preorderTraversal(self, visit, key=None):
        if self.item1 is not None:
            visit(self.item1.item, key)
        if self.left is not None:
            self.left.preorderTraversal(visit, key)
        if self.mleft is not None:
            self.mleft.preorderTraversal(visit, key)
        if self.item2 is not None:
            visit(self.item2.item, key)
        if self.mright is not None:
            self.mright.preorderTraversal(visit, key)
        if self.item3 is not None:
            visit(self.item3.item, key)
        if self.right is not None:
            self.right.preoderTraversal(visit, key)

    def postorderTraversal(self, visit, key=None):
        if self.left is not None:
            self.left.postorderTraversal(visit, key)
        if self.mleft is not None:
            self.mleft.postorderTraversal(visit, key)
        if self.mright is not None:
            self.mright.postorderTraversal(visit, key)
        if self.right is not None:
            self.right.postorderTraversal(visit, key)
        if self.item3 is not None:
            visit(self.item3.item, key)
        if self.item2 is not None:
            visit(self.item2.item, key)
        if self.item1 is not None:
            visit(self.item1.item, key)

    def getIndex(self, index):  #todo recheck
        temp = index
        if self.item1 is not None:
            if index == 0:
                return (self.item1, index)
            temp = index - 1
        if self.item2 is not None:
            if index == 1:
                return (self.item2, index)
            temp -= 1
        if self.item3 is not None:
            if index == 2:
                return (self.item3, index)
            temp -= 1
        index = temp
        if self.left != None:
            returned = self.left.getIndex(index)
            index = returned[1]
            if returned[0] != None:
                return returned
        if self.mleft != None:
            returned = self.mleft.getIndex(index)
            index = returned[1]
            if returned[0] != None:
                return returned
        if self.mright != None:
            returned = self.mright.getIndex(index)
            index = returned[1]
            if returned[0] != None:
                return returned
        if self.right != None:
            returned = self.right.getIndex(index)
            index = returned[1]
            if returned[0] != None:
                return returned
        return (None, index)

    def size(self):
        size = 0
        if self.item3 is not None:
            size = 3
        elif self.item2 is not None:
            size = 2
        elif self.item1 is not None:
            size = 1
        if self.left is not None:
            size += self.left.size()
        if self.mleft is not None:
            size += self.mleft.size()
        if self.mright is not None:
            size += self.mright.size()
        if self.right is not None:
            size += self.right.size()
        return size


def createSearchTree():
    return T234(None, None, None, None, None, None, None, None)
