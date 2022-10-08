"""
16236 - 아기 상어 (G3)
"""
import sys
from collections import deque

input = sys.stdin.readline

board = []
fish = 0
eat = 0
time = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input().rstrip())
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(N):
        if 1 <= board[i][j] <= 6:
            fish += 1
        elif board[i][j] == 9:
            shark_x, shark_y, shark_size = i, j, 2
            board[shark_x][shark_y] = 0


def bfs(shark_x, shark_y, shark_size):
    que = deque()
    min_path = []
    flag = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    que.append((shark_x, shark_y, 0))
    visited[shark_x][shark_y] = True
    while que:
        x, y, distance = que.popleft()
        for i in range(4):
            mx = dx[i] + x
            my = dy[i] + y
            if 0 <= mx < N and 0 <= my < N and not visited[mx][my]:
                if board[mx][my] <= shark_size:
                    visited[mx][my] = True
                    if 0 < board[mx][my] < shark_size:
                        if flag == 0:
                            min_distance = distance + 1
                            min_path.append((distance + 1, mx, my))
                        elif flag == 1 and min_distance >= distance + 1:
                            min_path.append((distance + 1, mx, my))
                    if flag == 0:
                        que.append((mx, my, distance + 1))
    if min_path:
        min_path.sort()
        return min_path[0]
    else:
        return False


while fish:
    bfs_info = bfs(shark_x, shark_y, shark_size)
    if not bfs_info:
        break
    else:
        shark_x, shark_y = bfs_info[1], bfs_info[2]
        time += bfs_info[0]
        eat += 1
        fish -= 1
        if eat == shark_size:
            shark_size += 1
            eat = 0
    board[shark_x][shark_y] = 0

print(time)
