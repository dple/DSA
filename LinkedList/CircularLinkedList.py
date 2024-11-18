class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self, node = None):
        self.last = node
        self.last.next = self.last

    # Insert a node at the end of list
    def insert_at_last(self, new_node):
        if self.last is None:
            self.last = new_node
            self.last.next = self.last
        else:                       
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node

    # Insert a node at the beginning of the list
    def insert_at_front(self, new_node):
        if self.last is None:
            self.last = new_node
            self.last.next = self.last
            return 
        
        new_node.next = self.last.next 
        self.last.next = new_node

    # Insert a node at a specific position 
    def insert_at_position(self, pos, new_node):
        # Insert at front
        if pos == 1:
            self.insert_at_front()

        prev_node = self.last 
        curr_node = self.last.next 
        k = 1
        while curr_node is not self.last or k < pos:
            k += 1
            prev_node = curr_node
            curr_node = curr_node.next 

        if curr_node is self.last.next:
            print("Out of bounds!")
            return 
        
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    
    # Delete the first node
    def delete_at_front(self):
        if self.last is None or self.last.next is self.last:
            self.last = None
            return 
        temp = self.last.next         
        self.last.next = self.last.next.next 
        temp = None 

    
    # Delete at last
    def delete_at_last(self):
        if self.last is None or self.last is self.last.next:
            self.last = None 
            return 
        curr_node = self.last.next
        prev_node = self.last 
        while curr_node is not self.last:
            prev_node = curr_node
            curr_node = curr_node.next 
        
        prev_node.next = curr_node.next 
        self.last = prev_node
        curr_node = None 


    # Delete at a specific position 
    def delete_at_position(self, pos):
        if pos == 1:
            self.delete_at_front()
            return 
        k = 1
        prev_node = self.last 
        curr_node = self.last.next  
        while k < pos and curr_node is not self.last:
            k += 1
            prev_node = curr_node
            curr_node = curr_node.next 
        
        if k < pos: 
            print("Out of bounds!")
            return 
        
        if k == pos and curr_node is self.last:
            temp = self.last 
            prev_node.next = self.last.next 
            self.last = prev_node
            temp = None 
        
        prev_node.next = curr_node.next 
        curr_node = None 
        
    def print_list(self):
        if self.last is None:
            return 
        
        curr_node = self.last.next 
        while curr_node is not self.last:
            print(curr_node.data, end=' ')
            curr_node = curr_node.next
        print(curr_node.data)

    # Search a node with data = target 
    def search(self, target):
        curr_node = self.last.next 
        pos = 1
        while curr_node is not self.last:
            if curr_node.data == target:
                print("Found", target, "at node position", pos)
                return 
            pos += 1
            curr_node = curr_node.next 
        if self.last.data == target:
            print("Found key at the end of list!")
        else:            
            print("There is no node with data = ", target)

    # Get the nth node
    def get_nth_node(self, n):
        if self.last is None:
            print("Out of bounds!")
            return None 
        
        curr_node = self.last.next 
        count = 1
        while curr_node is not self.last and count < n:
            count += 1
            curr_node = curr_node.next 
        
        if count == n:
            return curr_node
        
        print("Out of bounds!")
        return None 
    
    # Get nth node from back by using two pointers: ref_ptr and curr_ptr
    def get_nth_node_from_last(self, n):
        if self.last is None:
            return None 
        
        ref_ptr = self.last.next 
        curr_ptr = self.last.next

        for i in range(n - 1):
            if curr_ptr is self.last:
                return None 
            curr_ptr = curr_ptr.next 

        while curr_ptr is not self.last:
            curr_ptr  = curr_ptr.next 
            ref_ptr = ref_ptr.next 
        
        return ref_ptr


    # Check if it is circular linked list
    def is_circular(self):
        curr_node = self.last
        while curr_node is not None and curr_node.next is not self.last:
            curr_node = curr_node.next

        if curr_node is None or curr_node.next is None:
            return False
        
        return True 
    
    def is_circular_two_pointers(self):
        slow_pointer = self.last.next 
        fast_pointer = self.last.next 
        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next 
            fast_pointer = fast_pointer.next.next 
            if fast_pointer is slow_pointer:
                return True
            
        return False 

    # Reverse a circular linked list
    def reverse(self):
        if self.last is None or self.last.next is self.last:
            return 
        
        prev_node = self.last.next
        curr_node = self.last.next.next 
        # Head will become the last. Make it point to the last (i.e., new head) and assign it as the last
        prev_node.next = self.last 
        self.last = prev_node
        while curr_node is not self.last:
            # swap two nodes 
            next_node = curr_node.next 
            curr_node.next = prev_node

            # move to the next node
            prev_node = curr_node
            curr_node = next_node
    
    def reverse_k_nodes(self, k):
        return 




if __name__ == '__main__':
    cllist = CircularLinkedList(Node(1))        
    cllist.insert_at_last(Node(2))
    cllist.insert_at_last(Node(3))
    cllist.insert_at_last(Node(4))
    cllist.insert_at_last(Node(6))
    cllist.insert_at_position(5, Node(5))
    cllist.insert_at_front(Node(0))
    cllist.search(6)    
    #cllist.delete_at_position(7)
    #cllist.delete_at_front()
    cllist.print_list()
    #cllist.reverse()
    #cllist.print_list()
    print(cllist.is_circular_two_pointers())
    node = cllist.get_nth_node_from_last(3)
    if node is not None:
        print("3rd node is: ", node.data)