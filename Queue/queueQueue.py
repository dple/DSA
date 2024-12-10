"""
Implement Queue using Queue built-in class, supporting two functions: put() & get()
"""
from queue import Queue

MAX_SIZE = 100
class QueueQueue:
    def __init__(self, n = MAX_SIZE):
        self.capacity = n
        self.queue = Queue()
        self.size = 0

    def __str__(self):
        res = '->'.join(map(str, self.queue.queue))
        return res 
    
    def is_full(self):
        return self.size == self.capacity
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size

    def enqueue(self, value):
        if self.is_full():
            raise Exception("The queue is full")
        
        self.queue.put(value)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Could not get an element as the queue is empty!")
        
        res = self.queue.get()
        self.size -= 1

        return res
    
if __name__ == '__main__':
    queue = QueueQueue(3)

    queue.enqueue("Geek")
    queue.enqueue("for")
    queue.enqueue("Geeks")
    print("Initial queue: ", queue)

    queue.enqueue("Exception")
    queue.dequeue()


    print("Queue after pop 1 value: ", queue)
