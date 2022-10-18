
class Node:
    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):

        # we have to go to the left subtree
        if data < node.data:
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)
        # we have to go to the right subtree
        else:
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):

        if node.leftChild:
            self.traverse_in_order(node.leftChild)

        print(node.data)

        if node.rightChild:
            self.traverse_in_order(node.rightChild)

    def traverse_preorder(self):
        if self.root is not None:
            self.traverse_pre_order(self.root)

    def traverse_pre_order(self, node):
        print(node.data)
        if node.leftChild:
            self.traverse_pre_order(node.leftChild)

        if node.rightChild:
            self.traverse_pre_order(node.rightChild)

    def traverse_postorder(self):
        if self.root is not None:
            self.traverse_post_order(self.root)

    def traverse_post_order(self, node):

        if node.leftChild:
            self.traverse_post_order(node.leftChild)

        if node.rightChild:
            self.traverse_post_order(node.rightChild)

        print(node.data)

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        # using iteration method
        actual = self.root

        while actual.rightChild is not None:
            actual = actual.rightChild

        return actual.data

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        # using recursion method
        if node.leftChild:
            return self.get_min(node.leftChild)

        return node.data

    def remove_node(self, data, node):
        if node is None:
            return
        if data < node.data:
            self.remove_node(data, node.leftChild)
        elif data > node.data:
            self.remove_node(data, node.rightChild)
        else:

            if node.leftChild is None and node.rightChild is None:
                print("Removing a leaf node...%d" % node.data)
                parent = node.parent
                if parent is not None and parent.leftChild == node:
                    parent.leftChild = None
                if parent is not None and parent.rightChild == node:
                    parent.rightChild = None

                if parent is None:
                    self.root = None

                del node

            elif node.leftChild is None and node.rightChild is not None:
                print("Removing a node with single right child...")
                parent = node.parent
                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                else:
                    self.root = node.rightChild

                node.rightChild.parent = parent
                del node

            elif node.rightChild is None and node.leftChild is not None:
                print("Removing a node with single left child...")
                parent = node.parent
                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.leftChild
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild
                else:
                    self.root = node.leftChild

                node.leftChild.parent = parent
                del node

            else:
                print("Removing node with two children...")

                predecessor = self.get_predecessor(node.leftChild)
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.rightChild:
            return self.get_predecessor(node.rightChild)
        return node

    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)

class TreeComparator(object):

    def compare_tree(self, node1, node2):
        if not node1 or not node2:
            return node1 == node2

        if node1.data is not node2.data:
            return False

        return self.compare_tree(node1.leftChild,node2.leftChild) and self.compare_tree(node1.rightChild,node2.rightChild)

bst = BinarySearchTree()

bst.insert(12)
bst.insert(4)
bst.insert(1)
bst.insert(8)
bst.insert(20)
bst.insert(16)
bst.insert(27)

print(f"Max item: {bst.get_max_value()}")
print(f"Min item: {bst.get_min_value()}")
bst.traverse()
print("--------------")
bst.traverse_preorder()
print("-------")
bst.traverse_postorder()
print("-------")
bst.remove(12)
bst.traverse()

bst1 = BinarySearchTree()
bst1.insert(12)
bst1.insert(4)
bst1.insert(1)
bst1.insert(8)
bst1.insert(20)
bst1.insert(16)
bst1.insert(27)

bst2 = BinarySearchTree()
bst2.insert(12)
bst2.insert(4)
bst2.insert(1)
bst2.insert(8)
bst2.insert(20)
bst2.insert(16)
bst2.insert(27)

comp = TreeComparator()
print(comp.compare_tree(bst1.root,bst2.root))












