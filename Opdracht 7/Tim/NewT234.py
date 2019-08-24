def keyinitem(key, items):
    for i in range(len(items)):
        if items[i].key == key:
            return True

def sortkey(item):
    return item.key

class TreeItem:
    def __init__(self, key, item):
        self.key = key
        self.item = item


class T234Node:
    def __init__(self, items=[], children=[], parent=None):
        self.items = items
        self.children = children
        self.parent = parent

    def __getsiblings(self,location):
        if location == 0:
            return [self.parent.children[1]]
        elif location == len(self.parent.children)-1:
            return [self.parent.children[location-1]]
        else:
            return [self.parent.children[location-1], self.parent.children[location+1]]

    def __childsetter(self):
        for i in self.children:
            i.parent = self

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
                if len(self.children) != 0:
                    self.parent.children[1].children = [self.children.pop(2), self.children.pop(2)]
                    self.parent.children[1].children[0].parent = self.parent.children[1]
                    self.parent.children[1].children[1].parent = self.parent.children[1]
            elif self.parent.children[1] == self:
                self.parent.items.append(self.items.pop(1))
                self.parent.children.insert(1, T234Node([self.items.pop(0)], [], self.parent))
                if len(self.children) != 0:
                    self.parent.children[1].children = [self.children.pop(0), self.children.pop(0)]
                    self.parent.children[1].children[0].parent = self.parent.children[1]
                    self.parent.children[1].children[1].parent = self.parent.children[1]
        elif len(self.parent.items) == 2:
            if self.parent.children[0] == self:
                self.parent.items.insert(0,self.items.pop(1))
                self.parent.children.insert(1,
                                            T234Node([self.items.pop(1)], [],
                                                     self.parent))
                if len(self.children) != 0:
                    self.parent.children[1].children = [self.children.pop(2), self.children.pop(2)]
                    self.parent.children[1].children[0].parent = self.parent.children[1]
                    self.parent.children[1].children[1].parent = self.parent.children[1]
            elif self.parent.children[1] == self:
                self.parent.items.insert(1,self.items.pop(1))
                self.parent.children.insert(2,
                                            T234Node([self.items.pop(1)], [],
                                                     self.parent))
                if len(self.children) != 0:
                    self.parent.children[2].children = [self.children.pop(2), self.children.pop(2)]
                    self.parent.children[2].children[0].parent = self.parent.children[2]
                    self.parent.children[2].children[1].parent = self.parent.children[2]
            elif self.parent.children[2] == self:
                self.parent.items.append(self.items.pop(1))
                self.parent.children.append(T234Node([self.items.pop(1)], [], self.parent))
                if len(self.children) != 0:
                    self.parent.children[3].children = [self.children.pop(2), self.children.pop(2)]
                    self.parent.children[3].children[0].parent = self.parent.children[3]
                    self.parent.children[3].children[1].parent = self.parent.children[3]

    def __inorder(self, number):
        start = self.items[number]
        target = self.children[number]
        while target.children:
            target.__fixnode()
            for i in range(len(target.items) - 1, -1, -1):
                if target.items[i].key < start.key:
                    target = target.children[i+1]
                    break
                #target = target.children[-1]
        target.__fixnode()
        return target

    def __calcposition(self):
        for i in range(len(self.parent.children)):
            if self.parent.children[i] == self:
                return i

    def __keyposition(self, key):
        for i in range(len(self.items)):
            if self.items[i].key == key:
                return tuple((i, self.items[i]))

    def __parentsibling2node(self, sibling):
        self.items.append(self.parent.children[sibling].items[0])
        if self.parent.children[sibling].children:
            if sibling != 0:
                self.children.extend(self.parent.children[1].children)
            else:
                self.parent.children[sibling].children.extend(self.children)
                self.children = self.parent.children[sibling].children

    def __fixnode(self):
        if self.parent is not None and len(self.items) == 1:
            location = self.parent.children.index(self)
            siblings = self.__getsiblings(location)
            if len(siblings[0].items) > 1 or (len(siblings) == 2 and len(siblings[1].items) > 1):
                if location-1 >= 0 and len(self.parent.children[location-1].items) > 1:
                    self.items.insert(0, self.parent.items.pop(location-1))
                    self.parent.items.insert(location-1, self.parent.children[location-1].items.pop(-1))
                    if self.children:
                        self.children.insert(0, self.parent.children[location-1].children.pop(-1))
                        self.children[0].parent = self
                elif location+1 <= 3 and len(self.parent.children[location+1].items) > 1:
                    self.items.append(self.parent.items.pop(location))
                    self.parent.items.insert(location, self.parent.children[location+1].items.pop(0))
                    if self.children:
                        self.children.append(self.parent.children[location+1].children.pop(0))
                        self.children[-1].parent = self
            elif len(siblings[0].items) == 1 and (len(siblings) == 1 or (len(siblings) == 2 and len(siblings[1].items) == 1))\
                    and len(self.parent.items) > 1:
                if location-1 >= 0:
                    self.items.insert(0, self.parent.items.pop(location-1))
                    self.items.insert(0, siblings[0].items.pop(0))
                    self.children = siblings[0].children + self.children
                    self.__childsetter()
                    self.parent.children.remove(siblings[0])
                elif location == 0:
                    self.items.append(self.parent.items.pop(0))
                    self.items.append(siblings[0].items.pop(0))
                    self.children = self.children + siblings[0].children
                    self.__childsetter()
                    self.parent.children.remove(siblings[0])
            else:
                newitems = [siblings[0].items.pop(0), self.parent.items.pop(0), self.items[0]]
                newitems.sort(key = sortkey)
                self.items = newitems
                if(location > 0):
                    self.children = siblings[0].children + self.children
                else:
                    self.children = self.children + siblings[0].children
                self.__childsetter()
                self.parent.children.remove(siblings[0])
                self.parent = None



    def T234delete(self, key):
        #if len(self.children) == 2:
            #self.__fixnode()
        itemcount = len(self.items)

        self.__fixnode()
        if self.parent is None and len(self.items) == 0:
            self = self.children[0]

        if keyinitem(key, self.items):
            if len(self.children) != 0:
                target = self.__keyposition(key)
                inorderPredecessor = self.__inorder(target[0])
                if self.parent is None and len(self.items) == 0:
                    self = self.children[0]
                if not keyinitem(key, self.items): #or self.items[target[0]] != target[1]:
                    return self.T234delete(key)
                elif len(self.children) == 0:
                    del self.items[self.__keyposition(key)[0]]
                    return
                else:
                    target = self.__keyposition(key)
                    temp = self.items[target[0]]
                    self.items[target[0]] = inorderPredecessor.items[-1]
                    inorderPredecessor.items[-1] = temp
                    del inorderPredecessor.items[-1]
                    return
                #del inorderPredecessor.items[inorderPredecessor.__keyposition(key)]
            else:
                for i in range(len(self.items)):
                    if self.items[i].key == key:
                        del self.items[i]
                        return

        if key < self.items[0].key:
            self.children[0].T234delete(key)
        elif (len(self.items) == 1 and key > self.items[0].key) or key < self.items[1].key:
            self.children[1].T234delete(key)
        elif (len(self.items) == 2 and key > self.items[1].key) or key < self.items[2].key:
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
        if len(self.root.items) == 0:
            old = self.root
            if self.root.children:
                self.root = self.root.children[0]
                old.children = None
                del old
            else:
                return

