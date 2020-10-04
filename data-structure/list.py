from hashlib import md5
from struct import unpack_from


l1 = ["Beijing", "Washington"]
l2 = ["China", "USA"]

for a, b in zip(l1, l2):
    print(f"{a} is the capital of {b}")


dic = {}

dic[1] = 0
print (dic)

print (128 >> 3)
