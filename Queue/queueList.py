"""
Implement Queue using List
"""

MAX_SIZE = 100

class Queue:
    def __init__(self, n = MAX_SIZE):
        self.capacity = n
        self.queue = []
        self.size = 0

    def __str__(self):
        res = '->'.join(map(str, self.queue))
        return res
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        self.size == self.capacity

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
        
        res = self.queue.pop(0)
        return res

if __name__ == '__main__':
    queue = Queue()

    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    print("Initial queue: ", queue)
    print("\nElements dequeued from queue")
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print("\nQueue after removing elements")
    print(queue)