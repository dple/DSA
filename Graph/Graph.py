class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None 
        self.right = None


class BinaryTree:
    def __init__(self, node=None) -> None:
        self.root = node 
    
    def add_node(self, value, temp_root):        
        
        if self.root is None:
            self.root = Node(value)
            return 
        
        if temp_root is None:
            temp_root = Node(value)
            return 
        
        if value <= temp_root.data:
            self.add_node(value, temp_root.left)
        else:
            self.add_node(value, temp_root.right)
            
        return 
    
    def print_tree(self, temp_root):
        if temp_root is None:
            return 
        
        self.print_tree(temp_root.left)
        if temp_root is not None:
            print(temp_root.data, ' ')
        self.print_tree(temp_root.right)

        return 
    
if __name__ == '__main__':
    btree = BinaryTree()

    btree.add_node(-17, btree.root)
    
    btree.add_node(-10, btree.root)
    btree.add_node(10, btree.root)
    '''
    btree.add_node(1, btree.root)
    btree.add_node(8, btree.root)
    btree.add_node(-25, btree.root)
    btree.add_node(-28, btree.root)
    btree.add_node(-26, btree.root)
    '''
    btree.print_tree(btree.root)