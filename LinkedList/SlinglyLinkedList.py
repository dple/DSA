class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:

    #def __init__(self):
    #    self.head = None
    
    def __init(self, node=None):
        self.head = node

    # Insert a 'node' to the end of the singly linked list
    def addNode(self, node):
        if self.head == None:
            self.head = node
        else:        
            tmp = self.head
            # Travel a long of the list till the end
            while (tmp.next):            
                tmp = tmp.next
            
            tmp.next = node

    # Insert a node with its data = 'data' to the end of the singly linked list
    def add(self, data):
        node = Node(data)
        previous = self.head
        tmp = self.head
        while (tmp.next):            
            tmp = tmp.next
        tmp.next = node

    # Insert a node with its data = 'data' as a new head
    def insert_at_front(self, data):
        tmp = self.head
        self.head = Node(data)
        self.head.next = tmp

    # Insert a node as a new head
    def insertNode_at_front(self, node):
        tmp = self.head
        self.head = node
        self.head.next = tmp
    
    # Insert a node to the position 'index'
    def insert_at_position(self, index, data):
        if index < 1 or index > self.len() + 1:
            print("Out of bounds!")
            return 

        if index == 1:
            self.insert_at_front(data)
        else:
            i = 2
            new_node = Node(data)
            tmp = self.head
            while (tmp.next and i < index):
                i += 1
                tmp = tmp.next
            # Insert at the end if the index is out of bounds
            if tmp.next == None:
                tmp.next = new_node
            else:
                new_node.next = tmp.next                
                tmp.next = new_node

    # Insert a value 'data' before the node having a value 'key' in the list 
    def insert_before(self, key, data):
        curr = self.head
        
        # Insert in an empty list
        if curr == None:
            self.head = Node(data)
            return

        # Insert in front of the head
        if self.head.data == key:
            new_head = Node(data)
            new_head.next = self.head
            self.head = new_head
        
        else: # Insert in the middle of the list if found the element. If not insert at the end of the list
            new_node = Node(data)
            while (curr.next is not None and curr.next.data != key):
                curr = curr.next
            
            new_node.next = curr.next
            curr.next = new_node
        
    # Insert a value 'data' after the node having a value 'key' in the list 
    def insert_after(self, key, data):
        curr = self.head

        if curr == None:
            self.head = Node(data)

        while (curr.data != key and curr.next != None):
            curr = curr.next

        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node

    # Look for an element whose data == key using a iterative method
    # Return 'True' or 'False'
    def search_key(self, key):
        curr = self.head

        while (curr and curr.data != key):
            curr = curr.next

        if curr is None:
            return False
        else:
            return True

    def search_key_recursive(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        
        return self.search_key_recursive(node.next, key)

    # Return the length of the singly linked list
    def len(self):
        i = 0
        curr = self.head
        while (curr):
            i += 1
            curr = curr.next
        return i

    # Get the length of list using recursion method 
    def len_recursive(self, node):
        if (node == None):
            return 0
        return 1 + self.len_recursive(node.next)

    # Delete head
    def delete_head(self):
        tmp = self.head
        self.head = tmp.next
        tmp = None 
    
    # Delete the last element of the list
    def delete_end(self):
        if self.head == None:
            return
        previous = self.head 
        curr = previous.next
        if curr != None:
            while (curr.next != None):
                previous = curr
                curr = curr.next
            previous.next = None
            curr = None
        else:
            self.head = None

    # Delete the first node where its data = data
    def delete_node(self, data):
        curr = self.head
        
        while (curr and curr.data != data):
            previous = curr
            curr = curr.next
        
        if curr == None:
            print("There is no node whose data is: ", data, " to delete!")
        else:
            previous.next = curr.next
            curr = None

    # Print data of the list
    def print_list(self):
        currNode = self.head
        while currNode is not None:
            print(currNode.data, end = ' ')
            currNode = currNode.next
        print()

    # Find the nth node from the end of the list. Using two pointers whose distance is n - 1, 
    # so when one pointer reaces to the end, the other one is at the nth position from the end
    def find_node_from_end(self, n):
        main_ptr = self.head
        ref_ptr = self.head
        
        for i in range(n):
            if ref_ptr is None:
                print("Out of bounds!")
                return None
            ref_ptr = ref_ptr.next
        
        while ref_ptr is not None:
            ref_ptr = ref_ptr.next
            main_ptr = main_ptr.next
        
        return main_ptr

    # Print the last k nodes of the linked list 
    def print_last_k_nodes(self, k):
        ref_ptr = self.find_node_from_end(k)        
        while ref_ptr is not None:
            print(ref_ptr.data, end = ' ')
            ref_ptr = ref_ptr.next
        # Print a new line
        print()

    # Reverse the list 
    def reverse(self):
        # List has no more than one element 
        if self.head is None or self.head.next is None:
            return
        
        prevNode = self.head
        currNode = self.head.next 
        # Assign the next node of this new tail to Null. If not the new list will have a circular sub-list of last two elements
        prevNode.next = None

        while currNode is not None:
            # swap two elements 
            nextNode = currNode.next
            currNode.next = prevNode

            # Move to the next node 
            prevNode = currNode
            currNode = nextNode
        
        self.head = prevNode

    # Reverse k nodes of the list 
    def reverse_k_nodes(self, groupHead, k):
        
        prevNode = None
        currNode = groupHead
        nextNode = None
        count = 0

        while currNode is not None and count < k:
            count += 1
            # swap two element 
            nextNode = currNode.next
            currNode.next = prevNode
            # Move to the next node
            prevNode = currNode
            currNode = nextNode
        
        # Print reversed group
        currNode = prevNode
        for i in range(k):
            print(currNode.data, end = ' ')
            currNode = currNode.next
        print()

        return prevNode


    # Reverse the list in groups of a given size k. Using a recursive approach
    def reverse_in_groups(self, groupHead, k):

        # If list is empty or only one element, return the list
        if groupHead is None:
            return groupHead
        
        temp = groupHead
        count = 0
        #print("Group head's data: ", groupHead.data)

        while temp is not None and count < k:
            temp = temp.next
            count += 1

        newGroupHead = self.reverse_k_nodes(groupHead, k)
        #print("New group head's data: ", newGroupHead.data)

        # Recursion for the next group
        groupHead.next = self.reverse_in_groups(temp, k)

        return newGroupHead

    # Reverse a list in groups using an iterative approach 
    def reverse_in_groups_iterative(self, k):
        if self.head is None or self.head.next is None:
            return

        temp = self.head
        oldGroupHead = self.head
        count = 0

        while temp is not None and count < k:
            count += 1        
            temp = temp.next
            

        self.head = self.reverse_k_nodes(self.head, k)
        #print("Old head's data", oldGroupHead.data)
        #groupHead.next = temp
        newGroupHead = temp
        
        while newGroupHead is not None:
            reversedGroupHead = self.reverse_k_nodes(newGroupHead, k)
            oldGroupHead.next = reversedGroupHead
            count = 0
            while temp is not None and count < k:
                count += 1
                temp = temp.next
            
            newGroupHead = temp

        



if __name__ == '__main__':
    llist = SinglyLinkedList()

    llist.head = Node(3)
    #llist.delete_end()
    #llist.print_list()
    second = Node(6)
    third = Node(8)
    llist.addNode(second)
    llist.addNode(third)

    #llist.print_list()

    llist.insert_after(3, 4)
    #llist.print_list()
    llist.insert_before(8, 7)
    #llist.print_list()
    llist.insert_before(6, 5)
    #llist.print_list()
    llist.add(9)
    llist.addNode(Node(10))
    #llist.print_list()

    if llist.search_key_recursive(llist.head, 2):
        print('Yes')
    else:
        print('No')

    llist.insert_at_front(2)
    #llist.print_list()

    llist.insert_at_position(1, 1)
    #llist.print_list()
    llist.insert_at_position(11, 11)
    #llist.print_list()
    llist.insert_after(11, 12)
    #llist.print_list()
    llist.insert_after(12, 13)
    #llist.print_list()

    #llist.delete_head()
    #llist.delete_end()
    #llist.delete_node(2)
    llist.print_list()

    #node = llist.find_node_from_end(5)
    #if node is not None:
    #    print("5th element from the end of the list is: ", node.data)

    #print("Last 6 elements of the list are: ", end = '')
    #llist.print_last_k_nodes(6)

    #llist.head = llist.reverse_in_groups(llist.head, 3)
    llist.reverse_in_groups_iterative(3)
    print("Reverse in groups list: ", end='')
    llist.print_list()
    print("Length of the list = ", llist.len_recursive(llist.head))