class TreeItem:
    def __init__(self, key, item):
        self.key = key
        self.item = item


class T234Node:
    def __init__(self, items=[], children=[], parent=None):
        self.items = items
        self.children = children
        self.parent = parent

    def dotread(self, file):
        itemcount = len(self.items)
        if itemcount == 3:      #voor elk item in de node schrijven we waar het staat met de left middle right
            file.write(str(self.items[0].key) + str("[label=" + '"' + "<left> " + str(self.items[0].key) +
                                                 "|<middle> " + str(self.items[1].key) + "|<right> " + str(self.items[2].key) +
                                                 '"' + "];") + '\n')
        elif itemcount == 2:
            file.write(str(self.items[0].key) + str("[label=" + '"' + "<left> " + str(self.items[0].key) +
                                                 "|<middle> " + str(self.items[1].key) + '"' + "];") + '\n')
        elif itemcount == 1:
            file.write(str(self.items[0].key) + str("[label=" + '"' + "<left> " + str(self.items[0].key) + '"' + "];") + '\n')
        else:
            return

        childrencount = len(self.children)

        if childrencount >= 2:       # voor elke connectie word er een -> tussen de nodes gezet
            self.children[0].dotread(file)
            file.write(str(self.items[0].key) + " -> " + str(self.children[0].items[0].key) + ";" + '\n')
            self.children[1].dotread(file)
            file.write(str(self.items[0].key) + " -> " + str(self.children[1].items[0].key) + ";" + '\n')

        if childrencount >= 3:
            self.children[2].dotread(file)
            file.write(str(self.items[0].key) + " -> " + str(self.children[2].items[0].key) + ";" + '\n')

        if childrencount == 4:
            self.children[3].dotread(file)
            file.write(str(self.items[0].key) + "-> " + str(self.children[3].items[0].key) + ";" + '\n')

    def insert(self, item):
        itemcount = len(self.items)
        if itemcount == 0:
            self.items.append(item)
            return True
        if itemcount == 3:
            self.split()
            if self.parent is not None:
                return self.parent.insert(item)
        if len(self.children) != 0:
            if item.key < self.items[0].key:
                self.children[0].insert(item)
            elif itemcount == 1 or item.key < self.items[1].key:
                self.children[1].insert(item)
            elif itemcount == 2 or item.key < self.items[2].key:
                self.children[2].insert(item)
            else:
                self.children[3].insert(item)
        else:
            if item.key < self.items[0].key:
                self.items.insert(0, item)
            elif itemcount == 1 or (itemcount == 2 and item.key < self.items[1].key):
                self.items.insert(1, item)
            else:
                self.items.append(item)

    def split(self):
        if self.parent is None:
            self.parent = T234Node([self.items.pop(1)], [self, T234Node([self.items.pop(1)], [])])
            self.parent.children[1].parent = self.parent
            if self.children:
                self.parent.children[1].children = [self.children.pop(2), self.children.pop(2)]
                self.parent.children[1].children[0].parent = self.parent.children[1]
                self.parent.children[1].children[1].parent = self.parent.children[1]
        elif len(self.parent.items) == 1:
            if self.parent.children[0] == self:
                self.parent.items.insert(0, self.items.pop(1))
                self.parent.children.insert(1, T234Node([self.items.pop(1)], [], self.parent))
                if self.children:
                    self.parent.children[1].children = [self.children.pop(2), self.children.pop(2)]
            elif self.parent.children[1] == self:
                self.parent.items.append(self.items.pop(1))
                self.parent.children.insert(1, T234Node([self.items.pop(0)], [], self.parent))
                if self.children:
                    self.parent.children[1].children = [self.children.pop(0), self.children.pop(0)]
        elif len(self.parent.items) == 2:
            if self.parent.children[0] == self:
                self.parent.items.insert(self.items.pop(1))
                self.parent.children.insert(1,
                                            T234Node([self.items.pop(1)], [],
                                                     self.parent))
                if self.children:
                    self.parent.children[1].children = [self.children.pop(2), self.children.pop(2)]
            elif self.parent.children[1] == self:
                self.parent.items.insert(self.items.pop(1))
                self.parent.children.insert(2,
                                            T234Node([self.items.pop(1)], [],
                                                     self.parent))
                if self.children:
                    self.parent.children[2].children = [self.children.pop(2), self.children.pop(2)]
            elif self.parent.children[2] == self:
                self.parent.items.append(self.items.pop(1))
                self.parent.children.append(
                    T234Node([self.items.pop(1)], [], self.parent))
                if self.children:
                    self.parent.children[3].children = [self.children.pop(2), self.children.pop(2)]

    def __inorder(self, number):
        target = self.children[number + 1]
        while target.children:
            target = target.children[0]
        temp = self.items[number]
        self.items[number] = target.item[0]
        target.item[0] = temp
        return target

    def __calcposition(self):
        for i in range(len(self.parent.children)):
            if self.parent.children[i] == self:
                return i

    def __parentsibling2node(self, sibling):
        self.items.append(self.parent.children[sibling].items[0])
        if self.parent.children[sibling].children:
            if sibling != 0:
                self.children.extend(self.parent.children[1].children)
            else:
                self.parent.children[sibling].children.extend(self.children)
                self.children = self.parent.children[sibling].children

    def __fixnode(self):
        if self.parent:
            numberself = self.calcposition()

        if len(self.parent.children) == 2 and len(self.parent.children[0].children) == 2 and len(self.parent.children[1].children):
            if numberself == 0:
                self.__parentsibling2node(1)
            else:
                self.__parentsibling2node(0)

    def T234delete(self, key):
        #if len(self.children) == 2:
            #self.__fixnode()
        itemcount = len(self.items)

        if self.items[0].key == key:
            if self.children:
                self.__inorder(0).T234delete(key)
            else:
                self.items.pop(0)

        elif itemcount >= 2 and self.items[1].key == key:
            if self.children:
                self.__inorder(1).T234delete(key)
            else:
                self.items.pop(1)

        elif itemcount == 3 and self.items[2].key == key:
            if self.children:
                self.__inorder(2).T234delete(key)
            else:
                self.items.pop(2)

        elif key < self.items[0].key:
            if len(self.children[0].items) == 1 and len(self.children[1].items) == 2:
                self.children[0].items.append(self.items.pop(0))
                self.items.append(self.children[1].items.pop(1))
            elif len(self.children[0].items) == 1 and len(self.children[1].items) == 1:
                self.children[0].items.append(self.items.pop(0))
                self.children[0].items.append(self.children[1].items.pop(0))
                if self.children[1].children:
                    self.children.extend(self.children[1].children)
                self.children.remove(1)


            self.children[0].T234delete(key)
        elif key < self.items[1].key:
            self.children[1].T234delte(key)
        elif key < self.items[2].key:
            self.children[2].T234delete(key)
        else:
            self.children[3].T234delete(key)

class T234:
    def __init__(self):
        self.root = T234Node([], [], None)

    def insert(self, key, item=None):
        if item is None:
            item = key
        self.root.insert(TreeItem(key, item))
        while self.root.parent is not None:
            self.root = self.root.parent

    def print(self, nummer):
        f = open(nummer, "w")  # we opennen een nieuwe bestand met als naam de variabele nummer
        f.write("digraph 234{")  # we zetten het begin klaar
        f.write(str("node [shape=record];") + '\n')
        f.write(str("edge[splines=" + "line" + "];" + '\n'))
        if self.root.items:
            self.root.dotread(f)
        f.write("}")
        f.close()

    def delete(self, key):
        self.root.T234delete(key)
