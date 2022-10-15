# FIFO first item we insert is the first item we remove

class Queue:

    def __init__(self):
        self.queue = []

    # O(1) running time
    def is_empty(self):
        return self.queue == []

    #  this operation has O(1) running time
    def enqueue(self, data):
        self.queue.append(data)

    # O(N) linear running time. How to solve this problem? Doubly Linked List
    def dequeue(self):
        if self.size_queue() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return -1

    # O(1) running time
    def peek(self):
        return self.queue[0]

    #O(1) running time
    def size_queue(self):
        return len(self.queue)

    def display(self):
        return self.queue

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(f"size: {queue.size_queue()}")
print(f"Queue: {queue.display()}")
queue.dequeue()
queue.dequeue()
print(f"size: {queue.size_queue()}")
print(f"Queue: {queue.display()}")


