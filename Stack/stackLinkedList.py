"""
Implement stack using singly linked list
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class Stack:
    def __init__(self):
        self.head = Node("Head")
        self.size = 0

    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def __str__(self):
        res = ""
        cur_node = self.head.next 

        while cur_node: 
            res += str(cur_node.value) + "->"
            cur_node = cur_node.next

        return res[:-2] 
        
    def push(self, value):
        node = Node(value)

        node.next = self.head.next 
        self.head.next = node 
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Poping from a empty stack!")
                
        node = self.head.next 
        self.head.next = node.next 
        self.size -= 1

        return node.value  


if __name__ == '__main__':
    stack = Stack()

    stack.push("Geek")
    stack.push("for")
    stack.push("Geeks")

    print("Stack: ", stack)
    


    
