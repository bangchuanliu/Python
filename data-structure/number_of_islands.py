def dfs (nums, x, y):
    m = len(nums)
    n = len(nums[0])
    if (x < 0 or x >= m or y < 0 or y >= n or nums[x][y] != 1):
        return
    nums[x][y] = 0

    dfs (nums, x + 1, y)
    dfs (nums, x - 1, y)
    dfs (nums, x, y + 1)
    dfs (nums, x, y - 1)


def bfs (nums, x, y):
  q = []
  q.append((x,y))

  while (len(q) > 0):
      size = len(q)
      for i in range(size):
          (x, y) = q.pop(0)
            


nums = [[1,0,0],[0,0,0],[0,1,1]]
count = 0

for i in range(len(nums)):
    for j in range(len(nums[0])):
        if (nums[i][j] == 1):
            count += 1
            bfs(nums, i, j)

print(count)