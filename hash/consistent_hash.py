from bisect import bisect_left
from hash import hash

items = 1_000_000
nodes = 100
new_nodes = 101
ring = list()
new_ring = list()
node_count = {}

for i in range(nodes):
    h = hash(i)
    ring.append(h)
    node_count[h] = 0
ring.sort()

for i in range(new_nodes):
    h = hash(i)
    new_ring.append(h)
new_ring.sort()

change = 0

for i in range(items):
    h = hash(i)
    index = bisect_left(ring, h)    
    node_hash = ring[bisect_left(ring, h) % nodes]
    # compute the number of items in each node 
    node_count[node_hash] += 1

    new_node_hash = new_ring[bisect_left(new_ring, h) % new_nodes]
    if node_hash != new_node_hash:
        change += 1

print(f"change rate is {change/items}")
print(f"average number of items in a node is {items/nodes}")
print(f"max number of items in a node is {max(node_count.values())}")
print(f"min number of items in a node is {min(node_count.values())}")
