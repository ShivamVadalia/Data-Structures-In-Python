class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

def depth_first_search(start_node):

    # We need a LIFO structure
    stack = [start_node]

    # Let's iterate until stack becomes empty
    while stack:
        actual_node = stack.pop()
        actual_node.visited = True
        print(actual_node.name)

        for n in actual_node.adjacency_list:
            if not n.visited:
                stack.append(n)

# we can create the nodes or vertices
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

# we have to handle the neighbors
node1.adjacency_list.append(node2)
node1.adjacency_list.append(node3)
node2.adjacency_list.append(node4)
node4.adjacency_list.append(node5)

# run the bfs
depth_first_search(node1)

