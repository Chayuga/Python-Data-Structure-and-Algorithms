"""There are different ways of inseting node to a LinkedList 
1. At the Beginning
2. At the End
3. Between Nodes"""

# Inserting at the Beginning
# This is the most straight forward inserton, create new node and point the head of the list to it


class LinkedList(object):
    def __init__(self, node):
        node = self.node

    def add_first(self, node):
        node.next = self.head
        self.head = node

        """llist = LinkedList()
print(llist)


llist.add_first("b")
print(llist)

llist.add_first("a")
print(llist)"""

    # Inserting at the End
    # Inserting a new node at the end of the list forces you to traverse the whole linked list first and
    # to add the new node when you reach the end.

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
