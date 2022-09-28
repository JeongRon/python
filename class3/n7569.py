"""
7569 - 토마토 (G5)
"""

from collections import deque
import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())
box = []
que = deque()

for h in range(H):
    temp = []
    for n in range(N):
        temp.append(list(map(int, input().split())))
        for m in range(M):
            if temp[n][m] == 1:
                que.append((m, n, h))
    box.append(temp)

dm = [-1, 1, 0, 0, 0, 0]
dn = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

while que:
    m, n, h = que.popleft()

    for i in range(6):
        c = m + dm[i]
        b = n + dn[i]
        a = h + dh[i]
        if 0 <= c < M and 0 <= b < N and 0 <= a < H:
            if box[a][b][c] == 0:
                que.append((c, b, a))
                box[a][b][c] = box[h][n][m] + 1

day = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                day = -1
                print(day)
                exit(0)
            else:
                day = max(box[h][n][m], day)
print(day - 1)
