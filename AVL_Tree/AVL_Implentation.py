class Node:

    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)
                node.height = max(self.calc_height(node.leftChild), self.calc_height(node.rightChild)) + 1

        else:
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)
                node.height = max(self.calc_height(node.leftChild), self.calc_height(node.rightChild)) + 1

        # After every insertion we have to check whether the AVL conditions are hold true
        self.handle_violation(node)

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.leftChild)
        elif data > node.data:
            self.remove_node(data, node.rightChild)
        else:
            # We have found the node
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
                # After every removal we have to check whether the AVL conditions are hold true
                self.handle_violation(parent)

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
                # After every removal we have to check whether the AVL conditions are hold true
                self.handle_violation(parent)

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
                # After every removal we have to check whether the AVL conditions are hold true
                self.handle_violation(parent)

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

    def handle_violation(self, node):
        # check the nodes from the node we have inserted up to root node
        while node is not None:
            node.height = max(self.calc_height(node.leftChild), self.calc_height(node.rightChild)) + 1
            self.violation_helper(node)
            node = node.parent

    def violation_helper(self, node):
        balance = self.calculate_balance(node)
        # Ok, we know the tree is left heavy but is it left-right heavy or left-left heavy
        if balance > 1:
            # left right heavy situation: left rotation on parent + right rotation on grandparent
            if self.calculate_balance(node.leftChild) < 0:
                self.rotate_left(node.leftChild)
            # this is the right rotation on grandparent (if left-left heavy, that's single right rotation)
            self.rotate_right(node)

        # Ok, we know the tree is right heavy but is it right-left heavy or right-right heavy
        if balance < -1:
            # right left heavy situation: right rotation on parent + left rotation on grandparent
            if self.calculate_balance(node.rightChild) > 0:
                self.rotate_right(node.rightChild)
            # this is the right rotation on grandparent (if left-left heavy, that's single right rotation)
            self.rotate_left(node)

    def calc_height(self, node):
        # this is when the node is a Null
        if node is None:
            return -1

        return node.height

    def calculate_balance(self, node):
        if node is None:
            return 0

        return self.calc_height(node.leftChild) - self.calc_height(node.rightChild)

    def rotate_right(self, node):
        print("Rotating to the right on node ", node.data)
        temp_left_node = node.leftChild
        # print(node.data)
        t = temp_left_node.rightChild
        temp_left_node.rightChild = node
        node.leftChild = t

        if t is not None:
            t.parent = None

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.leftChild == node:
            temp_left_node.parent.leftChild = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.rightChild == node:
            temp_left_node.parent.rightChild = temp_left_node

        if node == self.root:
            self.root = temp_left_node

        node.height = max(self.calc_height(node.leftChild), self.calc_height(node.rightChild)) + 1
        temp_left_node.height = max(self.calc_height(temp_left_node.leftChild),
                                    self.calc_height(temp_left_node.rightChild)) + 1

    def rotate_left(self, node):
        print("Rotating to the left on node ", node.data)
        temp_right_node = node.rightChild
        t = temp_right_node.leftChild
        temp_right_node.leftChild = node
        node.rightChild = t

        if t is not None:
            t.parent = None

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.leftChild == node:
            temp_right_node.parent.leftChild = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.rightChild == node:
            temp_right_node.parent.rightChild = temp_right_node

        if node == self.root:
            self.root = temp_right_node

        node.height = max(self.calc_height(node.leftChild), self.calc_height(node.rightChild)) + 1
        temp_right_node.height = max(self.calc_height(temp_right_node.leftChild),
                                     self.calc_height(temp_right_node.rightChild)) + 1

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):

        if node.leftChild:
            self.traverse_in_order(node.leftChild)

        l = ''
        r = ''
        p = ''
        if node.leftChild is not None:
            l = node.leftChild.data
        else:
            l = 'NULL'

        if node.rightChild is not None:
            r = node.rightChild.data
        else:
            r = 'NULL'

        if node.parent is not None:
            p = node.parent.data
        else:
            p = 'NULL'

        print("%s left: %s right: %s parent: %s height: %s" % (node.data, l, r, p, node.height))

        if node.rightChild:
            self.traverse_in_order(node.rightChild)


avl = AVLTree()
avl.insert(32)
avl.insert(16)
avl.insert(48)
avl.insert(8)
avl.insert(24)
avl.insert(40)
avl.insert(56)
avl.insert(36)
avl.insert(44)
avl.insert(52)
avl.insert(60)
avl.insert(4)
avl.insert(58)
avl.insert(62)
avl.remove(4)

avl.traverse()


