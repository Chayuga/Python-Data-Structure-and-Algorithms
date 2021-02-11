"""How to Traverse a Linked List"""

# creating another class representing each node of the linked list


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkdList(object):
    # Initialise the linked list, store information where the linked list starts
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head

        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # Traversing a linked list (Traversing is another word of iterating) so we create __iter__ to add
    # the same behavior
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
