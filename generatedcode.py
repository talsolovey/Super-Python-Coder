class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def kth_smallest(root, k):
    stack = []
    current = root
    count = 0

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        count += 1

        if count == k:
            return current.value

        current = current.right

    return None


def test_kth_smallest():
    # Create sample binary search tree
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    assert kth_smallest(root, 1) == 2
    assert kth_smallest(root, 2) == 3
    assert kth_smallest(root, 3) == 4
    assert kth_smallest(root, 4) == 5
    assert kth_smallest(root, 5) == 6
    assert kth_smallest(root, 6) == 7
    assert kth_smallest(root, 7) == 8
    assert kth_smallest(root, 0) is None
    assert kth_smallest(root, 8) is None
    assert kth_smallest(None, 1) is None


test_kth_smallest()  
