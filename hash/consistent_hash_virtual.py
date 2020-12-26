from bisect import bisect_left
from hash import hash

items = 1_000_000
nodes = 100
v_nodes = 100
new_nodes = 101
ring = list()
new_ring = list()
node_count = [0] * nodes
hash_node = {}

for i in range(nodes):
    for j in range(v_nodes):
        h = hash(str(i) + str(j))
        ring.append(h)
        hash_node[h] = i
ring.sort()

for i in range(new_nodes): 
    for j in range(v_nodes):
        h = hash(str(i) + str(j))
        new_ring.append(h)
new_ring.sort()

change = 0

for i in range(items):
    h = hash(i)
    index = bisect_left(ring, h)    
    node_hash = ring[bisect_left(ring, h) % (nodes * v_nodes)]
    # compute the number of items in each node 
    node_count[hash_node[node_hash]] += 1

    new_node_hash = new_ring[bisect_left(new_ring, h) % (new_nodes * v_nodes)]
    if node_hash != new_node_hash:
        change += 1

print(f"change rate is {change/items}")
print(f"average number of items in a node is {items/nodes}")
print(f"max number of items in a node is {max(node_count)}")
print(f"min number of items in a node is {min(node_count)}")
node_count.sort()
print(f"median number of items in a node is {node_count[len(node_count)//2]}")
