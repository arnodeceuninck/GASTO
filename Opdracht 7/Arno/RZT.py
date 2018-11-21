class RoodZwartBoom:

    def __init__(self):

        # Variabelen ivm de rootgegevens
        self.root_key = None
        self.root_value = None

        # Variabelen ivm de linkerdeelboom
        self.left_tree = None
        self.left_connection = None

        # Variabelen ivm de rechterdeelboom
        self.right_tree = None
        self.right_connection = None

        self.parent = None

        self.createRBT()

    def createRBT(self):

        self.root_key = None
        self.root_value = None

        self.left_tree = None
        self.left_connection = None

        self.right_tree = None
        self.right_connection = None

        self.parent = None

    def destroyRBT(self):

        self.root_key = None
        self.root_value = None

        # TODO: Delete all items in the subtrees
        self.left_tree = None
        self.left_connection = None

        self.right_tree = None
        self.right_connection = None

        self.parent = None

        del self

    def isEmpty(self):
        if self.root_key is None:
            return True

    def insert(self, newItem):
        # TODO: make newitem with key and value
        if self.root_key == None:
            self.root_key == newItem.key
            self.root_value == newItem.root
        return True
