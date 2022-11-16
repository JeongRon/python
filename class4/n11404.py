'''
11404 - 플로이드 / gold 4 / 플로이드-워셜 
'''
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

# graph 초기화
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

# 입력 받은 간선 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

# 점화식 - 플로이드 워셜 알고리즘
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
