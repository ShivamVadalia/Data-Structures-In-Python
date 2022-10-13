
class Stack:

    def __init__(self):
        self.stack = []

    # insert item into the stack // O(1)
    def push(self, data):
        self.stack.append(data)

    # remove and return the last items we have inserted (LIFO) // O(1)
    def pop(self):
        if len(self.stack) < 1:
            return -1

        data = self.stack[-1]
        del self.stack[-1]
        return data

    # peek: it returns the last item without removing it // O(1)
    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)

my_stack = Stack()
my_stack.push(7)
my_stack.push(8)
my_stack.push(9)
print(my_stack.is_empty())
print(my_stack.stack_size())
my_stack.display()
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack.stack_size())
print(my_stack.is_empty())