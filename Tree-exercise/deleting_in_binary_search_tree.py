class BinarySearchTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return

        if data < self.data:
            # add to the left tree node
            if self.left:
                self.left.add_child(data)

            else:
                self.left = BinarySearchTreeNode(data)

        else:  # Else if data is greater than self.data
            # add to the right tree node
            if self.right:
                self.right.add_child(data)

            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        # if val equal to self.data, return true
        if self.data == val:
            return True

        # if val is less than self.data, search on the left tree node.
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        # otherwise if val is greater than self.data, search on the right tree node.
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    """In Order Traversal"""

    def in_order_traversal(self):
        elements = []

        # traverse left tree first
        if self.left:
            elements += self.left.in_order_traversal()

        # Base node traversal
        elements.append(self.data)

        # traverse right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    """Finding Max Val"""

    def find_max(self):
        # find max is found in right tree node.
        if self.right is None:
            return self.data
        return self.right.find_max()

    """Finding Min Val"""

    def find_min(self):
        # find min is found in left tree node.
        if self.left is None:
            return self.data
        return self.left.find_min()

    """Deleting val from a Tree Node"""

    def delete(self, val):
        if val < self.data:  # search in self.left
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data:  # search in self.right
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right

            if self.right is None:
                return self.left

        # Using minimum value from right to replace self.data
            """min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)"""

        # Using maximum value from the left to replace self.data
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self


def build_tree(elements):
    print("Building tree with these elements: ", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(18)
    print("After delete 18 ", numbers_tree.in_order_traversal())
