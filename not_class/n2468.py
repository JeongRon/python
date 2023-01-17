'''
2468번 - 안전 영역 / silver 1 / 브루트포스, DFS
'''
import sys
import copy

sys.setrecursionlimit(10**8)
INF = int(1e9)
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def cnt_dfs(cp, x, y):
    cp[x][y] = INF
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < n:
            if cp[nx][ny] != INF:
                cnt_dfs(cp, nx, ny)


# 1. 입력 받기
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

max_cnt = 1
height = 1
# 2. 브루트포스 / height 1~100까지 모든 경우 탐색
while height <= 100:
    # 2-1. height 보다 같거나 낮은 영역 INF(물에 잠김)
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= height:
                graph[i][j] = INF
    # 2-2. graph를 복사 후, dfs 활용하여 cnt 구하기
    cp_graph = copy.deepcopy(graph)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if cp_graph[i][j] != INF:
                cnt_dfs(cp_graph, i, j)
                cnt += 1
    # 2-3. 구한 cnt와 max_cnt 비교
    if max_cnt < cnt:
        max_cnt = cnt

    height += 1

print(max_cnt)
