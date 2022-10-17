class Queue:
    def __init__(self):
        self.stack = []

    def enqueue(self, data):
        self.stack.append(data)

    def dequeue(self):
        if len(self.stack)==1:
            return self.stack.pop()

        item = self.stack.pop()
        dequeue_item = self.dequeue()

        self.stack.append(item)
        return dequeue_item


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())

queue.enqueue(40)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())