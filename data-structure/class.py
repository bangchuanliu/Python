class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

def printList(node):
    while node:
        print(node.data, end = "-->")
        node = node.next


node = Node(1)
node2 = Node(2)
node.next = node2

printList(node)