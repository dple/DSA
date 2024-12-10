"""
Implementation of circular queue using linked list 
"""
MAX_SIZE = 100

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None 


class CircularQueue:
    def __init__(self, n=MAX_SIZE):
        self.capacity = n
        self.size = 0
        self.front = None 
        self.rear = None 

    def __str__(self):
        res = ""
        cur_node = self.front 

        while cur_node.next is not self.front: 
            res += str(cur_node.data) + "->"
            cur_node = cur_node.next

        res += str(cur_node.data)
        return res 
    
    def is_empty(self):
        return self.front == None and self.rear == None
    
    def is_full(self):
        return self.size == self.capacity
    
    def enqueue(self, new_data):
        node = Node(new_data)        
        if self.is_full():
            raise Exception("Queue is full!")
        
        self.size += 1

        if self.is_empty():
            self.front = self.rear = node 
            self.rear.next = self.front 
        
        else:
            self.rear.next = node 
            self.rear = node 
            self.rear.next = self.front
    

    def dequeue(self):
        if self.is_empty():
            raise Exception("Trying to get an element from an empty queue!")
        
        res = self.front.data 
        self.front = self.front.next 
        self.rear.next = self.front 
        self.size -= 1

        return res 
    
    # Get the front item but don't delete the front node  
    def get_front(self):
        if self.is_empty():
            raise Exception("Trying to get an element from an empty queue!")
        
        res = self.front.data 

        return res
        
    # Get the rear item but don't delete the rear 
    def get_rear(self):
        if self.is_empty():
            raise Exception("Trying to get an element from an empty queue!")
        
        res = self.rear.data 
        """
        # This code is for removing the rear
        if self.front == self.rear:     # only 1 node 
            self.front = self.rear = None 
            
        else: 
            last_node = self.front
            while last_node.next is not self.rear:
                last_node = last_node.next 

            last_node.next = self.front
            self.rear = last_node
        """

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
        