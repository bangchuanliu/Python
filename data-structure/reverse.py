class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(node):
    pre = None
    cur = node

    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    
    return pre


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3

newNode = reverse(n1)

while newNode:
    print(newNode.data, end="-->")
    newNode = newNode.next