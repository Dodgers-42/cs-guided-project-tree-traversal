class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            # the new value, must go left
            if self.left in None:
                #create a new node as a left child of current node
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        else:
            # the value mjust go right
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # let the right hand Node figure it out
                self.right.insert(value)

    def print_tree_dft(self):
        # Evalutate the current node
        print(self.value)

        if self.left is not None:
            self.left.print_tree_dft()

        if self.right is not None:
            self.right.print_tree_drt()

        return

    def print_tree_in_order(current_node):

        if current_node.right is not None:
            print_tree_in_order(current_node.right)

        if current_node.left is not None:
            print_tree_in_order(current_node.left)
        return

    def print_tree_post_order(current_node):
        # Evalutate the current node
        print(self.value)

        if self.left is not None:
            self.left.print_tree_dft()

        if self.right is not None:
            self.right.print_tree_drt()

        return

root = BSTNode(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(12)
root.insert(11)
root.insert(13)

root.print_tree_drt()