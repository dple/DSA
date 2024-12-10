"""
Implement a circular queue using an array (i.e., built-in List in Python)
"""

MAX_SIZE = 100

class CircularQueue:

    def __init__(self, n = MAX_SIZE):
        self.capacity = n
        self.size = 0
        self.queue = [None for _ in range(n)]
        self.front = self.rear = -1

    def __str__(self):
        i = self.front
        res = "" 
        while i != self.rear:
            res += str(self.queue[i]) + '->' 
            i = (i + 1) % self.capacity
        
        res += str(self.queue[self.rear])

        return res 
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def enqueue(self, new_data):
        if self.is_full():
            raise Exception("Queue is full!")
        
        if self.is_empty():
            self.front = 0
        
        self.rear = (self.rear + 1)  % self.capacity
        self.queue[self.rear] = new_data
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty!")

        res = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        return res 


if __name__ == '__main__':
    queue = CircularQueue(5)
    queue.enqueue(14)
    queue.enqueue(22)
    queue.enqueue(13)
    queue.enqueue(-6)
    print("Initial circular queue is: ", queue)
    print ("Deleted value = ", queue.dequeue())
    print ("Deleted value = ", queue.dequeue())
    print("Circular queue after two dequeues is: ", queue)
    queue.enqueue(9)
    queue.enqueue(20)
    queue.enqueue(5)
    print("Final circular queue is: ", queue)

