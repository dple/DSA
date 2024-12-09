"""
Implement a stack using LIFO Queue
"""

from queue import LifoQueue

class Stack:
    def __init__(self):
        self.stack = LifoQueue()
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def push(self, value):
        self.stack.put(value)
        self.size += 1

    def pop(self):
        self.stack.get_nowait()
        self.size -= 1

if __name__ == '__main__':
    stack = Stack()

    stack.push("Geek")
    stack.push("for")
    stack.push("Geeks")

    print("Stack: ", stack)
    