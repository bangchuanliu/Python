def dfs(grid, x, y):
    m = len(grid)
    n = len(grid[0])
    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
        return
    grid[x][y] = 0

    dfs(grid, x + 1, y)
    dfs(grid, x - 1, y)
    dfs(grid, x, y + 1)
    dfs(grid, x, y - 1)


def bfs(grid, x, y):
    q = [(x, y)]
    grid[x][y] = 0
    r = [0, 1, 0, -1]
    c = [1, 0, -1, 0]
    m = len(grid)
    n = len(grid[0])

    while len(q) > 0:
        (x, y) = q.pop(0)
        for i, j in zip(r, c):
            a = x + i
            b = y + j
            if a < 0 or a >= m or b < 0 or b >= n or grid[a][b] == 0:
                continue
            grid[a][b] = 0
            q.append((a, b))


nums = [[1, 0, 0], [0, 0, 0], [0, 1, 1]]
count = 0
m = len(nums)
n = len(nums[0])

for i in range(m):
    for j in range(n):
        if nums[i][j] == 1:
            count += 1
            bfs(nums, i, j)

print(count)
