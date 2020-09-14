# use content manager to read/write file
# with open("1.txt", 'r') as f: - right
# f = open("1.txt", 'r') - wrong

with open("1.txt",'r') as f:
    for line in f.readlines():
        print (line.strip('\n'))


with open("2.txt", 'w') as f:
    for i in range(1, 5):
        f.write(f'{str(i)}-->')

