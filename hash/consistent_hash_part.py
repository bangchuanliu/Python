from bisect import bisect_left
from hash import hash

items = 1_000_000
nodes = 100
new_nodes = 101
log_nodes = 7
max_power = 32
partition = max_power - log_nodes

node_count = [0] * nodes
ring = []
partition_node = {}
new_partition_node = {}

for part in range(2 ** log_nodes):    
    ring.append(part)
    partition_node[part] = part % nodes

for part in range(2 ** log_nodes):    
    new_partition_node[part] = part % new_nodes

change = 0
for i in range(items):
    h = hash(i) >> partition
    part = bisect_left(ring, h)
    node_count[partition_node[part]] += 1

    if partition_node[part] != new_partition_node[part]:
        change += 1


print(f"change rate is {change/items}")
print(f"average number of items in a node is {items/nodes}")
print(f"max number of items in a node is {max(node_count)}")
print(f"min number of items in a node is {min(node_count)}")
node_count.sort()
print(f"median number of items in a node is {node_count[len(node_count)//2]}")
