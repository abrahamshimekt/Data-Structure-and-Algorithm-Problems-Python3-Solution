class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class SinglyLinkedList:
    def __init__(self):
        self.head = Node()

    def get_node(self, data):
        curr = self.head
        while curr:
            if curr.get_data() == data:
                return curr
            curr = curr.get_next()
        return None

    def delete(self, data):
        curr = self.head
        prev = None
        while curr:
            if curr.get_data() == data:
                prev.set_next(curr.get_next())
            else:
                prev = curr
                curr = curr.get_next()

    def append(self, data):
        curr = self.head
        while curr.get_next():
            curr = curr.get_next()
        curr.set_next(Node(data))

    def size(self):
        length = 0
        curr = self.head
        while curr.get_next():
            length += 1
            curr = curr.get_next()
        return length - 1

    def printList(self):
        curr = self.head.get_next()
        while curr:
            print(curr.get_data())
            curr = curr.get_next()


l = SinglyLinkedList()
for pet in ["cat","bird","fish","dog","cow"]:
    l.append(pet)

l.printList()
print(l.size())
print(l.get_node('cow'))

