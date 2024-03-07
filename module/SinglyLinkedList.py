class Node:
    def __init__(self,data):
        self.data = data
        self.pointer = None
        

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def add(self,data):
        Newnode = Node(data)
        
        if self.head is None:
            self.head = Newnode
        
        else:
            cur = self.head
            while cur.pointer is not None:
                cur = cur.pointer
            
            cur.pointer = Newnode
    
    def print(self):
        cur  = self.head
        
        while cur is not None:
            print(cur.data,end= ' ')
            cur = cur.pointer
        print()
    
    def remove(self,data):
        
        
        if self.head is not None:
            if (self.head.data == data):
                self.head = self.head.pointer
            else:
                cur =self.head
                while cur.pointer is not None and cur.pointer.data!=data:
                    cur = cur.pointer
                if cur.pointer is not None:
                    cur.pointer = cur.pointer.pointer
                    
        else:
            print('linked list is empty!')
        

# test code
ll = LinkedList()

ll.add(20)
ll.add('string')
ll.add(50)


ll.print()
