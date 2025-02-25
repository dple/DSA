"""
https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/
"""


class Node:
    # Constructor to initialize a new node
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def maxPathSumUtil(root):
    global max_path_sum
    
    if root is None:
        return 0

    # Calculate maximum path sums for left and right subtrees
    l = maxPathSumUtil(root.left)
    r = maxPathSumUtil(root.right)

    # Update 'max_path_sum' with the maximum path sum passing through the current node
    max_path_sum = max(max_path_sum, l + r + root.data)

    # Return the maximum path sum rooted at this node
    return root.data + max(l, r)

def maxPathSum(root):    
    global max_path_sum
    # Compute maximum path sum and store it in 'res'
    maxPathSumUtil(root)

    return max_path_sum

if __name__ == "__main__":
    # Representation of input binary tree:
    #             10
    #          /     \
    #         5      -10
    #       /  \     /  \
    #     -5    1   50  20
    max_path_sum = float('-inf')
    root = Node(10)
    root.left = Node(5)
    root.right = Node(-10)
    root.left.left = Node(-5)
    root.left.right = Node(1)
    root.right.left = Node(50)
    root.right.right = Node(20)
    
    print(maxPathSum(root))