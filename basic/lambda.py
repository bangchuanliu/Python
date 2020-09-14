list = [1, 2, 3]


def mapTo(f, list):
    for i in range(len(list)):
        list[i] = f(list[i])
    return list


list2 = mapTo(lambda x: x + 1, list)

print(list2)
