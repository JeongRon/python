'''
14502 - 연구소 / gold 4 / BFS
'''
import sys
import itertools
import copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# 0:빈칸, 1:벽, 2:바이러스
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 값이 0(빈칸)인 위치 zero_index 리스트에 담기
zero_index = []
virus_index = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_index.append((i, j))
        if graph[i][j] == 2:
            virus_index.append((i, j))

zero_cases = list(itertools.combinations(zero_index, 3))


def case_bfs(change, arr):
    for a, b in change:
        arr[a][b] = 1
    que = deque(virus_index)
    while que:
        x, y = que.popleft()
        for i in range(4):
            vx = dx[i] + x
            vy = dy[i] + y
            if 0 <= vx < n and 0 <= vy < m:
                if arr[vx][vy] == 0:
                    arr[vx][vy] = 1
                    que.append((vx, vy))

    count = 0
    for p in range(n):
        for q in range(m):
            if arr[p][q] == 0:
                count += 1
    return count


max_res = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for case in zero_cases:
    case_res = case_bfs(case, copy.deepcopy(graph))
    if case_res > max_res:
        max_res = case_res

print(max_res)
