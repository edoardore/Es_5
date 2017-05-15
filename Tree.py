Black = "Black"
Red = "Red"


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
class AABR:
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

    def find_del(self, key, color=0):
        return self.findNode_delete(self.root, key, color)

    def findNode_delete(self, currentNode, key, color):
        if currentNode is None:
            return False
        elif key == currentNode.key and color == currentNode.color:
            return currentNode
        elif key < currentNode.key:
            return self.findNode_delete(currentNode.left, key, color)
        else:
            return self.findNode_delete(currentNode.right, key, color)

    def delete(self, key):
        if self.root is None:
            print "Lista Vuota"
        else:
            currentNode = self.find_del(key)
            if currentNode is False:
                return -1
            self._delete(currentNode)

    def _delete(self, currentNode):
        if currentNode.left is None:
            self.transplant(currentNode, currentNode.right)
        elif currentNode.right is None:
            self.transplant(currentNode, currentNode.left)
        else:
            y = self._min(currentNode.right)
            if y.dad is not currentNode:
                self.transplant(y, y.right)
                y.right = currentNode.right
                y.right.dad = y
            self.transplant(currentNode, y)
            y.left = currentNode.left
            y.left.dad = y

    def transplant(self, u, v):
        if u.dad is None:
            self.root = v
        elif u is u.dad.left:
            u.dad.left = v
        else:
            u.dad.right = v
        if v is not None:
            v.dad = u.dad


# Albero Red Black
class RRB:
    def __init__(self):
        self.nil = Node(None)
        self._root = self.nil

    def insert(self, data):
        if (self._root is None):
            self._root = Node(data, self.nil, Black)
        else:
            self._insert(Node(data, self.nil, Black))

    def _insert(self, z):
        y = self.nil
        x = self._root
        while (x is not self.nil):
            y = x
            if (z.key < x.key):
                x = x.left
            else:
                x = x.right
        z.dad = y
        if (y is self.nil):
            self.root = z
        elif (z.key < y.key):
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = Red
        self._insertFix(z)

    def _insertFix(self, z):
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
                    z.dad.dad.color = Red
                    self.rotateRight(z.dad.dad)
            else:
                y = z.dad.dad.left
                if (y.color is Red):
                    z.dad.color = Black
                    y.color = Black
                    z.dad.dad.color = Red
                    z = z.dad.dad
                else:
                    if (z == z.dad.left):
                        z = z.dad
                        self.rotateRight(z)
                    z.dad.color = Black
                    z.dad.dad.color = Red
                    self.rotateLeft(z.dad.dad)
        self._root.color = Black

    def find(self, key, color=Black):
        return self.findNode(self._root, key, color)

    def findNode(self, currentNode, key, color):
        if currentNode is None:
            return False
        elif key == currentNode.key and color == currentNode.color:
            return True
        elif key < currentNode.key:
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

    def inorder(self):
        def _inorder(v):
            if (v is None):
                return
            if (v.left is not None):
                _inorder(v.left)
            print v.key
            if (v.right is not None):
                _inorder(v.right)

        _inorder(self._root)


class RB:
    def __init__(self):
        self.nil = Node(None)
        self.root = self.nil

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, self.nil, 0)
        else:
            self._insert(Node(data, self.nil, 0))

    def _insert(self, currentNode):
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            if currentNode.key < x.key:
                x = x.left
            else:
                x = x.right
        currentNode.dad = y
        if y is self.nil:
            self.root = currentNode
        elif currentNode.key < y.key:
            y.left = currentNode
        else:
            y.right = currentNode
        currentNode.left = self.nil
        currentNode.right = self.nil
        currentNode.color = 1
        self._insertFix(currentNode)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.dad = x
        y.dad = x.dad
        if x.dad is self.nil:
            self.root = y
        elif x is x.dad.left:
            x.dad.left = y
        else:
            x.dad.right = y
        y.left = x
        x.dad = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right is not self.nil:
            x.right.dad = y
        x.dad = y.dad
        if y.dad is self.nil:
            self.root = x
        elif y is y.dad.right:
            y.dad.right = x
        else:
            y.dad.left = x
        x.right = y
        y.dad = x

    def _insertFix(self, currentNode):
        while currentNode.dad.color is 1:
            if currentNode.dad is currentNode.dad.dad.left:
                y = currentNode.dad.dad.right
                if y.color is 1:
                    currentNode.dad.color = 0
                    y.color = 0
                    currentNode.dad.dad.color = 1
                    currentNode = currentNode.dad.dad
                else:
                    if currentNode is currentNode.dad.right:
                        currentNode = currentNode.dad
                        self.left_rotate(currentNode)
                    currentNode.dad.color = 0
                    currentNode.dad.dad.color = 1
                    self.right_rotate(currentNode.dad.dad)
            else:
                y = currentNode.dad.dad.left
                if y.color is 1:
                    currentNode.dad.color = 0
                    y.color = 0
                    currentNode.dad.dad.color = 1
                    currentNode = currentNode.dad.dad
                else:
                    if currentNode is currentNode.dad.left:
                        currentNode = currentNode.dad
                        self.right_rotate(currentNode)
                    currentNode.dad.color = 0
                    currentNode.dad.dad.color = 1
                    self.left_rotate(currentNode.dad.dad)
        self.root.color = 0

    def find(self, key, color=0):
        return self.findNode(self.root, key, color)

    def findNode(self, currentNode, key, color):
        if currentNode is None:
            return False
        elif key == currentNode.key and color == currentNode.color:
            return True
        elif key < currentNode.key:
            return self.findNode(currentNode.left, key, color)
        else:
            return self.findNode(currentNode.right, key, color)


class ABR:
    def __init__(self):
        self.root = None

    def setRoot(self, key):
        self.root = Node(key)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key, None, 0)

        else:
            self.insertNode(Node(key, None, 0))

    def insertNode(self, currentNode):
        y = None
        x = self.root
        while x is not None:
            y = x
            if currentNode.key < y.key:
                x = x.left
            else:
                x = x.right
        currentNode.dad = y
        if y is None:
            self.root = currentNode
        elif currentNode.key < y.key:
            y.left = currentNode
        else:
            y.right = currentNode

    def find(self, key, color=0):
        return self.findNode(self.root, key, color)

    def findNode(self, currentNode, key, color):
        if currentNode is None:
            return False
        elif key == currentNode.key and color == currentNode.color:
            return True
        elif key < currentNode.key:
            return self.findNode(currentNode.left, key, color)
        else:
            return self.findNode(currentNode.right, key, color)

    def find_delete(self, key, color=0):
        return self.findNode_delete(self.root, key, color)

    def findNode_delete(self, currentNode, key, color):
        if currentNode is None:
            return False
        elif key == currentNode.key and color == currentNode.color:
            return currentNode
        elif key < currentNode.key:
            return self.findNode_delete(currentNode.left, key, color)
        else:
            return self.findNode_delete(currentNode.right, key, color)

    def inorder(self):
        def _inorder(v):
            if v is None:
                return
            if v.left is not None:
                _inorder(v.left)
            print v.key
            if v.right is not None:
                _inorder(v.right)
            print v.key

        _inorder(self.root)

    def min(self):
        print "il valore minimo e': ", self._min(self.root)

    def _min(self, currentNode):
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.get()

    def max(self):
        print "il valore minimo e': ", self._max(self.root)

    def _max(self, currentNode):
        while currentNode.right is not None:
            currentNode = currentNode.right
        return currentNode.get()

    def transplant(self, u, v):
        if u.dad is None:
            self.root = v
        elif u is u.dad.left:
            u.dad.left = v
        else:
            u.dad.right = v
        if v is not None:
            v.dad = u.dad

    def delete(self, key):
        if self.root is None:
            print "lista vuota"
        else:
            currentNode = self.find_delete(key)
            if currentNode is False:
                return -1
            self._delete(currentNode)

    def _delete(self, currentNode):
        if currentNode.left is None:
            self.transplant(currentNode, currentNode.right)
        elif currentNode.right is None:
            self.transplant(currentNode, currentNode.left)
        else:
            y = self._min(currentNode.right)
            if y.dad is not currentNode:
                self.transplant(y, y.right)
                y.right = currentNode.right
                y.right.dad = y
            self.transplant(currentNode, y)
            y.left = currentNode.left
            y.left.dad = y