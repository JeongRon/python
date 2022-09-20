"""
2178 - 미로 탐색 (silver 1)
"""

from collections import deque


def bfs_maze(x, y):
    que = deque()
    que.append((x, y))
    while que:
        del_x, del_y = que.popleft()
        for i in range(4):
            move_x = del_x + dx[i]
            move_y = del_y + dy[i]
            if move_x < 0 or move_y < 0 or move_x >= row or move_y >= col:
                continue
            elif maze[move_x][move_y] == 0:
                continue
            elif maze[move_x][move_y] == 1:
                maze[move_x][move_y] = maze[del_x][del_y] + 1
                que.append((move_x, move_y))
    return maze[row - 1][col - 1]


maze = []
# 1. 입력 받기
row, col = map(int, input().split())
for i in range(row):
    maze.append(list(map(int, input())))

# 2. 왼쪽-오른쪽-위-아래 살펴보기
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 3. bfs (deque 사용)
print(bfs_maze(0, 0))
