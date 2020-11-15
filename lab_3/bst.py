class BinarySearchTree:
    class _BSTNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.right = None
            self.left = None

    def __init__(self):
        self._size = 0
        self._root = None

    def add(self, key, value):
        z = self._BSTNode(key, value)
        y = None
        x = self._root
        while (x != None):
            y = x
            if (key < x.key):
                x = x.left
            else:
                x = x.right
        if y == None:
            self._root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        self._size += 1

    def size(self):
        return self._size

    def inorder_walk(self):
        nodes = []
        self._inorder_walk(self._root, nodes)
        return nodes

    def _inorder_walk(self, subtree: _BSTNode, nodes: []):
        if subtree:
            self._inorder_walk(subtree.left, nodes)
            nodes.append(subtree.key)
            self._inorder_walk(subtree.right, nodes)

    def postorder_walk(self):
        nodes = []
        self._postorder_walk(self._root, nodes)
        return nodes

    def _postorder_walk(self, subtree: _BSTNode, nodes: []):
        if subtree:
            self._postorder_walk(subtree.left, nodes)
            self._postorder_walk(subtree.right, nodes)
            nodes.append(subtree.key)

    def preorder_walk(self):
        nodes = []
        self._preorder_walk(self._root, nodes)
        return nodes

    def _preorder_walk(self, subtree: _BSTNode, nodes: []):
        if subtree:
            nodes.append(subtree.key)
            self._preorder_walk(subtree.left, nodes)
            self._preorder_walk(subtree.right, nodes)

    def search(self, key):
        return self._search(self._root, key)

    def _search(self, subtree, key):
        if subtree is None:
            return False
        if subtree.key == key:
            return subtree.value
        if subtree.key < key:
            return self._search(subtree.right, key)
        return self._search(subtree.left, key)

    def remove(self, key):
        return self._remove(self._root, key)

    def _remove(self, subtree, key):
        if subtree is None:
            return subtree
        if key < subtree.key:
            subtree.left = self._remove(subtree.left, key)
        elif key > subtree.key:
            subtree.right = self._remove(subtree.right, key)
        else:
            if subtree.left is None:
                temp = subtree.right
                subtree = None
                return temp
            elif subtree.right is None:
                temp = subtree.left
                subtree = None
                return temp
            temp = self._smallest(subtree.right)
            subtree.key = temp.key
            subtree.right = self._remove(subtree.right, temp.key)
            self._size -= 1
        return subtree

    def smallest(self):
        temp = self._smallest(self._root)
        return (temp.key, temp.value)

    def _smallest(self, subtree):
        if subtree.left is None:
            return subtree
        return self._smallest(subtree.left)

    def largest(self):
        temp = self._largest(self._root)
        return (temp.key, temp.value)

    def _largest(self, subtree):
        if subtree.right is None:
            return subtree
        return self._largest(subtree.right)
