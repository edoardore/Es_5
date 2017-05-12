class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.dad = None

    def get(self):
        return self.key

    def set(self, key):
        self.key = key

    def getChildren(self):
        children = []
        if (self.left != None):
            children.append(self.left)
        if (self.right != None):
            children.append(self.right)

    def getDad(self):
        return self.dad

    def setDad(self, dad):
        self.dad = dad


class ABR:
    def __init__(self):
        self.root = None

    def setRoot(self, key):
        self.root = Node(key)

    def insert(self, key):
        if (self.root is None):
            self.setRoot(key)
        else:
            self.insertNode(self.root, key)

    def insertNode(self, currentNode, key):
        if (key <= currentNode.key):
            if (currentNode.left):
                self.insertNode(currentNode.left, key)
            else:
                currentNode.left = Node(key)
        elif (key > currentNode.key):
            if (currentNode.right):
                self.insertNode(currentNode.right, key)
            else:
                currentNode.right = Node(key)
        y = None
        x = currentNode
        while x != None:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        currentNode.setDad(y)

    def find(self, key):
        return self.findNode(self.root, key)

    def findNode(self, currentNode, key):
        if (currentNode is None):
            return False
        elif (key == currentNode.key):
            return True
        elif (key < currentNode.key):
            return self.findNode(currentNode.left, key)
        else:
            return self.findNode(currentNode.right, key)

    def inorder(self):
        def _inorder(v):
            if (v is None):
                return
            if (v.left is not None):
                _inorder(v.left)
            print v.key
            if (v.right is not None):
                _inorder(v.right)

        _inorder(self.root)

    def min(self):
        print "Valore minimo :", self._min(self.root)

    def _min(self, currentNode):
        while currentNode.left != None:
            currentNode = currentNode.left
        return currentNode.get()

    def max(self):
        print "Valore massimo:", self._max(self.root)

    def _max(self, currentNode):
        while currentNode.right != None:
            currentNode = currentNode.right
        return currentNode.get()

    def successor(self):
        self._successor(self.root)

    def _successor(self, currentNode):
        if currentNode.right != None:
            return self._min(currentNode.right)
        y = currentNode.dad
        while y != None and currentNode == y.right:
            currentNode = y
            y = y.dad
        return y


Black = "Nero"
Red = "Rosso"


class ABRN(ABR):
    def __init__(self):
        self.color = Black

    def setColor(self, string):
        self.color = string

    def getColor(self):
        return self.color


tree = ABR()
tree.insert(1000)
tree.insert(5)
tree.insert(-100)
for x in range(20, 10, -1):
    tree.insert(x)
print tree.find(5)
print tree.find(2)
tree.inorder()
tree.min()
tree.max()
