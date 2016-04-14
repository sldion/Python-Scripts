
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    root = None

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, value):

        if(self.root) is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if(value < node.value):
            if(node.left is not None):
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if(node.right is not None):
                self._add(value, node.right)
            else:
                node.right = Node(value)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):

        if (value == node.value):
            return node
        elif(value < node.value and node.left is not None):
            self._find(value, node.left)
        elif(value > node.value and node.right is not None):
            self._find(value,node.right)

    def deleteTree(self):
        self.root = None

    # Traverse the tree currentNode, left Node ,right Node
    def preOrder(self):
        if (self.root is not None):
            self._preOrder(self.root)

    def _preOrder(self, node):
        print node.value
        if (node.left is not None):
            self._preOrder(node.left)
        if (node.right is not None):
            self._preOrder(node.right)

    def inOrder(self):
        if(self.root is not None):
            self._inOrder(self.root)

    def _inOrder(self, node):

        if(node.left is not None):
            self._inOrder(node.left)
        print(node.value)
        if(node.right is not None):
            self._inOrder(node.right)

    def postOrder(self):
        if(self.root is not None):
            self._postOrder(self.root)

    def _postOrder(self, value):
        if(node.left is not None):
            self._inOrder(node.left)
        if(node.right is not None):
            self._inOrder(node.right)

        print(node.value)


tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)

#tree.preOrder()
tree.inOrder()
