"""
Implement stack by using dequee
"""

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque() 
        self.size = 0

    def __str__(self):
        res = '->'.join(map(str, self.stack))

        return res

    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def push(self, value):
        self.stack.append(value)
        self.size += 1

    def pop(self):
        res = self.stack.pop()
        self.size -= 1

        return res 
    
if __name__ == '__main__':
    stack = Stack()

    stack.push("Geek")
    stack.push("for")
    stack.push("Geeks")

    print("Stack: ", stack)
    



    