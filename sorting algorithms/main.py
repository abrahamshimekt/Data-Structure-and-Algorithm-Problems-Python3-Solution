class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begining(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    def insert_after(self,prev,data):
        if prev is None:
            return
        else:
            newNode = Node(data)
            newNode.next = prev.next
            prev.next = newNode
    def insert_end(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        last = self.head
        while last.next:
            last  = last.next
        last.next = newNode

    def deleting_node(self,position):
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next
    def search(self,data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    def sortLinkedList(self,head):
        current = head
        index = Node(None)
        if head is None:
            return
        else:
            while current:
                index = current.next
                while index:
                    if current.data > index.data:
                        current.data,index.data = index.data, current.data
                    index = index.next
                current = current.next
    def traverse(self):
        temp = self.head
        while temp:
            print(f'{temp.data} >')
            temp = temp.next


l = LinkedList()
for i in range(5):
    l.insert_begining(i)
prev = Node(3)
head = Node(1)
l.sortLinkedList(head)
l.deleting_node(3)
l.insert_end(8)
l.insert_after(prev,6)
l.traverse()
print(l.search(6))

