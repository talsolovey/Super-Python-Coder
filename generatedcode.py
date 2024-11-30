class TreeNode:
    """Class for a node in a binary search tree."""
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.left_size = 0

class BST:
    """Binary Search Tree class."""

    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the binary search tree."""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        """Helper method to insert a value recursively."""
        if value < node.value:
            node.left_size += 1
            if node.left:
                node.left = self._insert(node.left, value)
            else:
                node.left = TreeNode(value)
        else:
            if node.right:
                node.right = self._insert(node.right, value)
            else:
                node.right = TreeNode(value)
        return node

    def kth_smallest(self, k):
        """Find the k-th smallest element in the binary search tree."""
        return self._kth_smallest(self.root, k)

    def _kth_smallest(self, node, k):
        """Helper method to find the k-th smallest element recursively."""
        if not node:
            return None
        left_size = node.left_size
        if k <= left_size:
            return self._kth_smallest(node.left, k)
        if k == left_size + 1:
            return node.value
        return self._kth_smallest(node.right, k - left_size - 1)

def test_kth_smallest():
    """Unit tests for the kth smallest function."""
    bst = BST()
    for v in [5, 3, 7, 2, 4, 6, 8]:
        bst.insert(v)

    assert bst.kth_smallest(1) == 2
    assert bst.kth_smallest(2) == 3
    assert bst.kth_smallest(3) == 4
    assert bst.kth_smallest(4) == 5
    assert bst.kth_smallest(5) == 6
    assert bst.kth_smallest(6) == 7
    assert bst.kth_smallest(7) == 8
    assert bst.kth_smallest(8) is None

    bst_empty = BST()
    assert bst_empty.kth_smallest(1) is None

    bst_single = BST()
    bst_single.insert(10)
    assert bst_single.kth_smallest(1) == 10
    assert bst_single.kth_smallest(2) is None

    bst_duplicates = BST()
    for v in [5, 3, 5, 7, 4, 5, 5]:
        bst_duplicates.insert(v)
    assert bst_duplicates.kth_smallest(1) == 3
    assert bst_duplicates.kth_smallest(2) == 4
    assert bst_duplicates.kth_smallest(3) == 5
    assert bst_duplicates.kth_smallest(5) == 5

    print("All tests passed.")

test_kth_smallest()