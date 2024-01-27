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
    
    def print(self):
        temp = self.head
        res_str = ""
        while temp!=None:
            res_str += f"{temp.val}-->"
            temp = temp.next
        return res_str
    