Black = 0
Red = 1


class Node:
    def __init__(self, key, dad=None, color=Black):
        self.key = key
        self.left = None
        self.right = None
        self.dad = dad
        self.color = color

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

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color


# Albero binario di ricerca
class ABR:
    def __init__(self):
        self.root = None

    def setRoot(self, key, dad, color):
        self.root = Node(key, dad, color)

    def insert(self, key):
        if (self.root is None):
            self.setRoot(key, None, Black)
        else:
            self.insertNode(Node(key, None, Black))

    def insertNode(self, z):
        y = None
        x = self.root
        while (x is not None):
            y = x
            if (z.key < x.key):
                x = x.left
            else:
                x = x.right
        z.dad = y
        if (y is None):
            self.root = z
        elif (z.key < y.key):
            y.left = z
        else:
            y.right = z

    def find(self, key, color=Black):
        return self.findNode(self.root, key, color)

    def findNode(self, currentNode, key, color):
        if (currentNode is None):
            return False
        elif key == currentNode.key and color == currentNode.color:
            return True
        elif (key < currentNode.key):
            return self.findNode(currentNode.left, key, color)
        else:
            return self.findNode(currentNode.right, key, color)

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


# Albero Red Black
class RB:
    def __init__(self):
        self._root = None

    def setRoot(self, key, dad, color):
        self.root = Node(key, dad, color)

    def insert(self, key):
        if (self._root is None):
            self.setRoot(key, None, Black)
        else:
            self.insertNode(Node(key, None, Black))

    def insertNode(self, z):
        y = None
        x = self._root
        while (x is not None):
            y = x
            if (z.key < x.key):
                x = x.left
            else:
                x = x.right
        z.dad = y
        if (y is None):
            self._root = z
        elif (z.key < y.key):
            y.left = z
        else:
            y.right = z
        z.left = None
        z.right = None
        z.color = Red
        self.insertFix(z)

    def insertFix(self, z):
        while (z.dad.color == Red):
            if (z.dad == z.dad.dad.left):
                y = z.dad.dad.right
                if (y.color == Red):
                    z.dad.color = Black
                    y.color = Black
                    z.dad.dad.color = Red
                    z = z.dad.dad
                else:
                    if (z == z.dad.right):
                        z = z.dad
                        self.rotateLeft(z)
                    z.dad.color = Black
                    z.dad.dad = Red
                    self.rotateRight(z.dad.dad)
            else:
                y = z.dad.dad.left
                if (y.color is Red):
                    z.parent.color = Black
                    y.color = Black
                    z.dad.dad.color = Red
                    z = z.dad.dad
                else:
                    if (z == z.dad.left):
                        z = z.dad
                        self.rotateRight(z)
                    z.dad.color = Black
                    z.dad.dad = Red
                    self.rotateLeft(z.dad.dad)
        self._root.color = Black

    def find(self, key, color=Black):
        return self.findNode(self._root, key, color)

    def findNode(self, currentNode, key, color):
        if (currentNode is None):
            return False
        elif key == currentNode.key and color == currentNode.color:
            return True
        elif (key < currentNode.key):
            return self.findNode(currentNode.left, key, color)
        else:
            return self.findNode(currentNode.right, key, color)

    def rotateLeft(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.dad = x
        y.dad = x.dad
        if x.dad is None:
            self._root = y
        elif x == x.dad.left:
            x.dad.left = y
        else:
            x.dad.right = y
        y.left = x
        x.dad = y

    def rotateRight(self, y):
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.dad = y
        x.dad = y.dad
        if y.dad is None:
            self._root = x
        elif y == y.dad.right:
            y.dad.right = x
        else:
            y.dad.left = x
        x.right = y
        y.dad = x


