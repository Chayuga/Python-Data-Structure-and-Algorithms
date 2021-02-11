"""
Add following methods to BinarySearchTreeNode class created in main video tutorial

1. find_min(): finds minimum element in entire binary tree
2. find_max(): finds maximum element in entire binary tree
3. calculate_sum(): calcualtes sum of all elements
4. post_order_traversal(): performs post order traversal of a binary tree
5. pre_order_traversal(): perofrms pre order traversal of a binary tree
"""


# SOLUTION ONE:

class BinarySearchTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # node already exist

        if data < self.data:  # add to the left tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if val == self.data:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):  # finds minimum element in entire binary tree
        elements = []

        # left traversal
        if self.left:
            elements += self.left.in_order_traversal()

        # Base root traversal
        elements.append(self.data)

        # Right traversal
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    # performs post order traversal of a binary tree
    def post_order_traversal(self):
        elements = []

        # Left tree traversal
        if self.left:
            elements += self.left.post_order_traversal()

        # Right tree traversal
        if self.right:
            elements += self.right.post_order_traversal()

        # Base root traversal
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):  # perofrms pre order traversal of a binary tree
        elements = []

        # Base root traversal
        elements.append(self.data)

        # Left tree traversal
        if self.left:
            elements += self.left.post_order_traversal()

        # Right tree traversal
        if self.right:
            elements += self.right.post_order_traversal()

        return elements

    # Find the minimum value, in Binary minimum val is on the left node of tree
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    # Find the minimum value, in Binary minimum value is on the right node of tree
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # Get the sum of the values
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0

        return self.data + left_sum + right_sum


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__name__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]

    numbers = [15, 12, 7, 14, 27, 20, 23, 88]

    numbers_tree = build_tree(numbers)
    print("Input numbers:", numbers)
    print("Min:", numbers_tree.find_min())
    print("Max:", numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())
