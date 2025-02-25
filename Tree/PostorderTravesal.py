import math 

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None 
        self.right = None 

class Tree:
    def __init__(self, node=None) -> None:
        self.root = node
        self.max_path = float('-inf')

    def __str__(self) -> str:
        res = []
        self.postorder_travesal(self.root, res)
        return ' '.join(str(x) for x in res)

    def postorder_travesal(self, node, res):
        if node == None:
            return 
        self.postorder_travesal(node.left, res)
        self.postorder_travesal(node.right, res)

        # Print the current node
        #print(node.data, end=' ')
        res.append(node.data)

    def max_path_sum(self):
        self.max_path_sum_util(self.root)
        return self.max_path

    def max_path_sum_util(self, node):
        if node == None:
            return 0
        
        l = self.max_path_sum_util(node.left)
        r = self.max_path_sum_util(node.right)
        self.max_path = max(self.max_path, l + r + node.data)

        return max(l, r) + node.data 


if __name__ == '__main__':        
    # Representation of input binary tree:
    #             10
    #          /     \
    #         5      -10
    #       /  \     /  \
    #     -5    1   50  20
    
    root = Node(10)
    root.left = Node(5)
    root.right = Node(-10)
    root.left.left = Node(-5)
    root.left.right = Node(1)
    root.right.left = Node(50)
    root.right.right = Node(20)

    tree = Tree(root)
    print(tree)
    print("Max Path Sum of the tree:", tree.max_path_sum())
