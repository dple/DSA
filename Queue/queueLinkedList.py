"""
Implement a queue using linked list
"""

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None 

class Queue:
    def __init__(self):
        self.front = None 
        self.rear = None 

    def __str__(self):
        res = ""
        cur_node = self.front 

        while cur_node: 
            res += str(cur_node.data) + "->"
            cur_node = cur_node.next

        return res[:-2] 
    
    def is_empyty(self):
        return self.front == None and self.rear == None 
    
    def enqueue(self, new_data):
        node = Node(new_data)
        if self.rear == None:
            self.front = node 
            self.rear = node 
        else:
            self.rear.next = node 
            self.rear = node 
        
    def dequeue(self):
        if self.is_empyty():
            raise Exception("Queue is empty!")
        
        res = self.front.data
        self.front = self.front.next 

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


