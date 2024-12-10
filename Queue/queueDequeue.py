"""
Implement stack by using dequee supporting two functions: 
    - append(): add a new element into the right of the dequeue
    - popleft(): pop out the first element from the left
"""

from collections import deque

MAX_SIZE = 100

class Queue:
    def __init__(self, n = MAX_SIZE):
        self.capacity = n
        self.queue = deque() 
        self.size = 0

    def __str__(self):
        res = '->'.join(map(str, self.queue))

        return res

    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def get_size(self):
        return self.size
    
    def enqueue(self, value):
        if self.is_full():
            raise Exception("The queue is full")
        
        self.queue.append(value)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        
        res = self.queue.popleft()
        self.size -= 1

        return res 
    
if __name__ == '__main__':
    queue = Queue()

    queue.enqueue("Geek")
    queue.enqueue("for")
    queue.enqueue("Geeks")
    print("Initial queue: ", queue)

    queue.dequeue()

    print("Queue after pop 1 value: ", queue)
    



    