
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # This operation inserts items at the end of the linked list
    # So we have to manipulate the tail node in O(1) running time
    def insert_end(self, data):
        new_node = Node(data)
        #when the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        #there is atleast 1 item in the data structure
        # we keep inserting items at the end of the linked list
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # We can traverse doubly linked list in both directions
    def traverse_forward(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):

        actual_node = self.tail

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.previous

dll = DoublyLinkedList()

dll.insert_end(1)
dll.insert_end(2)
dll.insert_end(3)

dll.traverse_forward()
print("----------------------")
dll.traverse_backward()
