class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    while head:
        print(head.data, end="-->")
        head = head.next


node = Node(1)
node2 = Node(2)
node.next = node2

print_list(node)
