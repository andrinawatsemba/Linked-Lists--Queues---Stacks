class Node:
    def create_node(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def create_list(self):
        self.head = None

def insert_at_end(self,data):
    new_node = Node()
    new_node.create_node(data)

    if not hasattr(self, 'head') or self.head is None:
        self.head = new_node
        return
    temp = self.head
    while temp.next:
        temp = temp.next
                      
    temp.next = new_node
    new_node.prev = temp

def delete_node(self, key):
    temp = self.head
    while temp:
        if temp.data == key:
            if temp.prev:
                temp.prev.next = temp.prev
                return
            temp = temp.next
def search_node(self, key):
    temp =  self.head
    while temp: 
        if temp.data == key:
            return True
        temp = temp.next
        return False
def display_list(self):
    temp = self.head
    while temp:
        print(temp.data, end=' <-> ')
        temp = temp.next
        print('None') 


###test the implementation

dll =DoublyLinkedList()
dll.create_list() #initialize the list

dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)

dll.display_list() 