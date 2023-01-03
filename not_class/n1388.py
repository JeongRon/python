'''
1388번 - 바닥 장식 / silver 4 / DFS
'''


def dfs(x, y, floor, cnt):
    visited[x][y] = cnt
    if floor == '-':
        if y + 1 < m and house[x][y + 1] == '-':
            dfs(x, y + 1, floor, cnt)
    elif floor == '|':
        if x + 1 < n and house[x + 1][y] == '|':
            dfs(x + 1, y, floor, cnt)


n, m = map(int, input().split())
house = []
for _ in range(n):
    house.append(list(input()))

visited = [[0 for _ in range(m)] for _ in range(n)]

cnt = 1
for i in range(n):
    for j in range(m):
        if visited[i][j] != 0:
            continue
        else:
            dfs(i, j, house[i][j], cnt)
            cnt += 1

print(cnt - 1)
