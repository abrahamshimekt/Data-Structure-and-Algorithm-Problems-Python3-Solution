class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev


class DoublyLinkedList:
    def __init__(self):
        head = Node('__head__')
        self.head = head
        self.tail = head

    def get_node(self, data):
        curr = self.head
        while curr:
            if curr.get_data() == data:
                return curr
            else:
                curr = curr.get_next()
        return None

    def append(self, data):
        new_tail = Node(data)
        self.tail.set_next(new_tail)
        new_tail.set_prev(self.tail)
        self.tail = new_tail

    def delete(self, data):
        del_node = self.get_node(data)
        if del_node:
            prev_node = del_node.get_prev()
            next_node = del_node.get_next()
            prev_node.set_next(next_node)
            if next_node:
                next_node.set_prev(prev_node)
            else:
                self.tail = prev_node

    def size(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.get_next()
        return count

    def printList(self):
        curr = self.head
        while curr:
            print(curr.get_data())
            curr = curr.get_next()

    def traverse_backwards(self):
        curr = self.tail
        while curr:
            print(curr.get_data())
            curr = curr.get_prev()


l = DoublyLinkedList()
for pet in ["bird","cat","dog","Ox"]:
    l.append(pet)

l.delete('bird')
l.printList()
l.traverse_backwards()
print(l.size())

