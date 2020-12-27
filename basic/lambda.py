# filter, map, reduce

arr = [1, 2, 3]

result = map(lambda x: x + 1, arr)
print(list(result))

result2 = filter(lambda x: x % 2 == 0, arr)
print(list(result2))
