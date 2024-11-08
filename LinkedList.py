class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    #def __init__(self):
    #    self.head = None
    
    def __init(self, node=None):
        self.head = node

    def addNode(self, node):
        previous = self.head
        tmp = self.head
        while (tmp):
            previous = tmp
            tmp = tmp.next
        
        previous.next = node

    def add(self, data):
        node = Node(data)
        previous = self.head
        tmp = self.head
        while (tmp):
            previous = tmp
            tmp = tmp.next
        previous.next = node

    def insert_at_front(self, data):
        tmp = self.head
        self.head = Node(data)
        self.head.next = tmp

    def insertNode_at_front(self, node):
        tmp = self.head
        self.head = node
        self.head.next = tmp
    
    def insert_at_position(self, index, data):
        if index == 0:
            self.insert_at_front(data)
        else:
            i = 1
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

    # Insert a value 'data' after the node having a value 'key' in the list 
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

    def len(self):
        i = 0
        curr = self.head
        while (curr):
            i += 1
            curr = curr.next

    def len_recursive(self):
        if 
    def print_list(self):
        curr = self.head
        while(curr):
            print(curr.data, end = ' ')
            curr = curr.next
        print()

if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third

    llist.print_list()

    llist.insert_before(1, -3)
    llist.print_list()
    llist.insert_before(3, 2.5)
    llist.print_list()
    llist.insert_before(6, 7)
    llist.print_list()
    llist.add(4)
    llist.addNode(Node(5))
    llist.print_list()

    if llist.search_key_recursive(llist.head, 2):
        print('Yes')
    else:
        print('No')

    llist.insert_at_front(0)
    llist.print_list()

    llist.insert_at_position(0, -1)
    llist.print_list()
    llist.insert_at_position(9, 9)
    llist.print_list()
    llist.insert_at_position(5, 10)
    llist.print_list()
    llist.insert_after(3, 11)
    llist.print_list()
    llist.insert_after(0, -2)
    llist.print_list()