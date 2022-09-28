"""
7576 - 토마토 (G5)
"""
import sys
from collections import deque

input = sys.stdin.readline

box = []
que = deque()
y, x = map(int, input().split())
for i in range(x):
    box.append(list(map(int, input().split())))
    for j in range(y):
        if box[i][j] == 1:
            que.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while que:
    a, b = que.popleft()
    for i in range(4):
        move_x = a + dx[i]
        move_y = b + dy[i]
        if 0 <= move_x < x and 0 <= move_y < y:
            if box[move_x][move_y] == 0:
                box[move_x][move_y] = box[a][b] + 1
                que.append((move_x, move_y))

day = 0
for i in range(x):
    for j in range(y):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        else:
            day = max(day, box[i][j])
print(day - 1)
