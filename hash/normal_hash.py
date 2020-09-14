from hashlib import md5
from struct import unpack_from
ITEMS = 10000000
NODES = 100

node_count = [0] * NODES

for item in range(ITEMS):
    k = md5(str(item).encode("utf-8")).digest()
    h = unpack_from(">I",k)[0]
    node_count[h % NODES]+=1

average = ITEMS / NODES
max = max(node_count)
min = min(node_count)

print(average)
print(max)
print(min)