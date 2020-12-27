"""
There are 3 ways to read data from stdin

1. sys.stdin
2. input()
3. fileinput.input()

"""
# run: python sys.py < 3.txt

import sys, fileinput

# sys.stdin

for line in sys.stdin:
    if line.rstrip() == "Exit":
        break
    a, b, c = line.rstrip().split()
    print(int(a) + int(b) + int(c))

# input()

# while True:
#     line = input("Input here: ")
#     if line == "Exit":
#         break
#     print(f"You have typed {line}")


# fileinput.input()

# for fileinput_line in fileinput.input():
#     if 'Exit' == fileinput_line.rstrip():
#         break
#     print(f'You have typed {fileinput_line}')
