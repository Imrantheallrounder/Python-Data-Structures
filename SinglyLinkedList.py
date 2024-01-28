class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_begining(self, val):
        node = Node(val, self.head)
        self.head = node
    
    def insert_at_end(self, val):
        if not self.head:
            self.head = Node(val, None)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(val, None)

    def insert_values(self, data):
        temp = self.head
        for val in data:
            self.insert_at_end(val)

    def size(self):
        temp = self.head
        sz = 0
        while temp:
            temp = temp.next
            sz += 1
        return sz
    
    def remove_at(self, idx):
        """
        Remove en element from linked list at a given index.
        """
        if idx<0 or idx>=self.size():
            raise Exception("Invalid Index")
        
        if idx==0:
            self.head = self.head.next
            return
        
        count = 0
        temp = self.head
        while count!=idx-1:
            temp = temp.next
            count+=1
        temp.next = temp.next.next

    def insert_at(self, idx, val):
        if idx == 0:
            self.head = Node(val, self.head)
            return
        temp = self.head
        count = 0
        while count!=idx-1:
            temp = temp.next
            count+=1
        temp.next = Node(val, temp.next)

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurence of data_after in Linked list values
        # Now insert data_to_insert after data_after node.
        temp = self.head
        while temp:
            if temp.val == data_after:
                temp.next = Node(data_to_insert, temp.next)
                return
            temp = temp.next
        return f"{data_after} Not Found in List"

    def remove_by_value(self, value):
        # Remove that specific node that contains this value
        temp = self.head
        if temp.val == value:
            self.head = self.head.next
            return
        while temp.next:
            if temp.next.val == value:
                temp.next = temp.next.next
                return
            temp = temp.next
        print("Element Not Found")
            
    
    def reverse(self):
        # Reverse the Linked List
        temp = self.head
        while temp:
            curr_val = temp.val
            self.remove_by_value(curr_val)
            self.insert_at_begining(curr_val)
            temp = temp.next
        # Right now this func is not optimized. Will optimize it later

    def print(self):
        temp = self.head
        res_str = ""
        while temp!=None:
            res_str += f"{temp.val}-->"
            temp = temp.next
        return res_str
    
    