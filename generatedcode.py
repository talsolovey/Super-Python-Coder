class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def kth_smallest(root, k):
    stack = []
    current = root
    count = 0

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        count += 1
        
        if count == k:
            return current.val
        
        current = current.right
    return None

# Unit tests
def test_kth_smallest():
    # Create the binary search tree
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
    
    # Edge Case: k is greater than number of nodes
    assert kth_smallest(root, 10) is None
    
    # Edge Case: Empty tree
    assert kth_smallest(None, 1) is None
    
    # Edge Case: k is zero
    assert kth_smallest(root, 0) is None
    
    # Single node tree
    single_node = TreeNode(1)
    assert kth_smallest(single_node, 1) == 1
    assert kth_smallest(single_node, 2) is None
    
    # Two node tree
    two_node_root = TreeNode(2)
    two_node_root.left = TreeNode(1)
    assert kth_smallest(two_node_root, 1) == 1
    assert kth_smallest(two_node_root, 2) == 2
    assert kth_smallest(two_node_root, 3) is None

test_kth_smallest()