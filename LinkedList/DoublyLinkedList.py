class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None 
        self.prev = None 

class DoublyLinkedList:

    def __init__(self, node = None) -> None:
        self.head = node 
        self.tail = node 

    def forward_traversal(self):
        curr = self.head
        print("Show list from the head: ", end= '')
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.next

        print()
    
    def backward_traversal(self):
        curr = self.tail
        print("Show list from the tail: ", end= '')
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.prev

        print()

    # Find the length of the list
    def len(self):
        curr = self.head
        l = 0
        while curr is not None:
            l += 1
            curr = curr.next
        return l

    # Add a node as a new tail
    def insert_end(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return 
        
        if self.tail is not None:
            self.tail.next = node              
        
        node.prev = self.tail
        self.tail = node

    # Add a node with data = data as a new tail
    def insert_end_data(self, data):
        if self.head == None:
            self.head = node
            self.tail = node
            return 
        
        node = Node(data)
        if self.tail is not None:
            self.tail.next = node
        
        node.prev = self.tail
        self.tail = node

    # Insert a new node into the beginning of the list
    def insert_at_front(self, node):
        
        if self.head is not Node:
            self.head.prev = node
        node.next = self.head
        self.head = node

    # Insert a new node into a specific position 
    def insert_at_position(self, node, index):

        if (self.len() < index):
            print("Position is out of bound!")
            return 

        if index == 1:
            self.insert_at_front(node)
            return 
        
        curr = self.head 
        i = 1
        while (i < index):
            i += 1
            pre_node = curr
            curr = curr.next 
        
        node.next = curr
        curr.prev = node
        pre_node.next = node
        node.prev = pre_node

    # Delete the head of the doubly linked list
    def delete_head(self):
        if self.head is None:
            return 
        
        if self.head == self.tail:
            self.head = None
            self.tail = None 
        
        self.head = self.head.next
        self.head.prev = None         

    # Delete the tail of the doubly linked list
    def delete_tail(self):
        if self.tail is None:
            return 
        
        if self.head == self.tail:
            self.head = None 
            self.tail = None 
        
        self.tail = self.tail.prev
        self.tail.next = None 
        
    # Delete a node at a specific position of the doubly linked list
    def delete_at_position(self, index):
        curr = self.head        
        i = 1
        while curr is not None and i < index:
            i += 1
            pre_node = curr
            curr = curr.next 

        if curr is None:
            print("Position is out of bound!")
            return 
        
        if curr is self.tail:
            self.tail = pre_node
            self.tail.next = None 
        else:
            pre_node.next = curr.next
            curr.next.prev = pre_node

    def reserve_from_head(self):
        if self.head is None or self.head.next is None:
            return
        
        # Get the head and convert it to tail
        currNode = self.head        
        prevNode = currNode.prev            
        currNode.prev = currNode.next
        currNode.next = prevNode

        # first element, thus become new tail
        self.tail = currNode

        # Move to next node in the list, currNode.next is now currNode.prev
        currNode = currNode.prev


        while (currNode is not None):
            prevNode = currNode.prev            
            currNode.prev = currNode.next
            currNode.next = prevNode
        
            # Move to next node in the list, currNode.next is now currNode.prev
            currNode = currNode.prev
        
        self.head = prevNode.prev        

    def reverse_from_tail(self):

        if self.tail is None or self.tail.prev is None:
            return 
        
        # Get the tail and convert it to head
        currNode = self.tail
        nextNode = currNode.next
        currNode.next = currNode.prev
        currNode.prev = nextNode

        # Make it head as the first element in the list
        self.head = currNode

        # Move to the next node from tail
        currNode = currNode.next 

        while currNode is not None:
            nextNode = currNode.next
            currNode.next = currNode.prev
            currNode.prev = nextNode

            # Move to the next node from tail
            currNode = currNode.next 
        
        # Assign the new tail
        self.tail = nextNode.next

# Reverse the linked list using recursion 
def reverse(dllist):
    node = dllist.tail    
    ret = DoublyLinkedList(node)    
    while (node.prev is not None):
        node = node.prev
        ret.insert_end_data(node.data)        

    return ret        


if __name__ == '__main__':
    dllist = DoublyLinkedList()
    
    node = Node(5)
    dllist.insert_end(node)    
    dllist.insert_end(Node(10))        
    dllist.insert_end(Node(11))    
    dllist.insert_end(Node(12))    
    dllist.insert_end(Node(13))    
    print("List before reversing. ", end='')
    dllist.forward_traversal()
    dllist.reserve_from_head()    
    print("List after resversing. ", end='')    
    dllist.forward_traversal()
    dllist.reverse_from_tail()
    print("List after resversing again. ", end='')    
    dllist.forward_traversal()
    #dllist.backward_traversal()
    dllist.insert_at_front(Node(3))
    dllist.insert_at_position(Node(7), 2)    
    #dllist.backward_traversal()
    #dllist.delete_head()    
    #dllist.forward_traversal()
    #dllist.delete_tail()    
    #dllist.forward_traversal()
    #dllist.delete_at_position(4)
    #dllist.forward_traversal()
    #reserved_list = reverse(dllist)    
    #reserved_list.forward_traversal()
    #dllist.reserve_from_head()
    #dllist.forward_traversal()

    print("Length of the doubly linked list is: ", dllist.len())
