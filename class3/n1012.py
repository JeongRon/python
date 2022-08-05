"""
1012 - 유기농 배추 (silver 2)
"""
import sys

input = sys.stdin.readline


def bfs(array, i, j):
    queue = [[i, j]]
    qx = [0, -1, 1, 0]
    qy = [1, 0, 0, -1]
    while queue:
        a = queue[-1][0]
        b = queue[-1][1]
        array[a][b] = 2
        del queue[-1]
        for k in range(4):
            q = a + qx[k]
            w = b + qy[k]
            if 0 <= q < N and 0 <= w < M and array[q][w] == 1:
                queue.append([q, w])


T = int(input().rstrip())

for _ in range(T):
    M, N, K = map(int, input().split())
    array = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        array[Y][X] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if array[i][j] == 1:
                bfs(array, i, j)
                count += 1

    print(count)
