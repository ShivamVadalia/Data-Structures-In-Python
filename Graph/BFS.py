class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def breadth_first_search(start_node):
    # FIFO- First In First Out
    queue = [start_node]

    # we keep iterating(considering the neighbors) until queue becomes empty
    while queue:
        # remove and return the first item we have inserted into the list
        actual_node = queue.pop(0)
        actual_node.visited = True
        print(actual_node.name)

        for n in actual_node.adjacency_list:
            if not n.visited:
                queue.append(n)


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
breadth_first_search(node1)
