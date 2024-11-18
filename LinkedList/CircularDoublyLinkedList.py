class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None 
        self.prev = None 

class CircularDLL:
    def __init__(self, node = None) -> None:
        self.last = node 
        self.last.next = node 
        self.last.prev = node 
    
    def insert_at_front(self):
        return 
    

if __name__ == '__main__':
    print("Hello Doubly Circular Linked List")