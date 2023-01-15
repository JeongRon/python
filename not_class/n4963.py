'''
4963번 - 섬의 개수 / silver 2 / DFS
'''
import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

# 상하좌우, 위아래대각선
dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]


def dfs(graph, row, col):
    graph[row][col] = 2
    for i in range(8):
        nx = row + dx[i]
        ny = col + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if graph[nx][ny] == 1:
                dfs(graph, nx, ny)


while True:
    # 1. 입력 및 리스트 받기
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    cnt = 0
    # 2. dfs 알고리즘
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                cnt += 1
                dfs(graph, i, j)
    print(cnt)
