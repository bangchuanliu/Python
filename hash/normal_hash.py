from hash import hash 

items = 1_000_000
nodes = 100
nodes2 = 101
node_count = [0] * nodes

change = 0

for item in range(items):
    h = hash(item)
    node_count[h % nodes]+=1
    if h % nodes != h % nodes2:
        change += 1

print(f"change rate is {change * 100/items}%")
print(f"average number of items in a node is {items/nodes}")
print(f"max number of items in a node is {max(node_count)}")
print(f"min number of items in a node is {min(node_count)}")