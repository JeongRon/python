'''
11048번: 이동하기 / silver 2 / DP
'''
import sys

input = sys.stdin.readline

# 미로 크기 n,m / 미로 리스트 graph 입력 받기
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# candy DP 리스트 / 각 좌표 마다, 가장 사탕을 많이 받을 수 있는 개수 넣을 예정
candy = [[0 for _ in range(m)] for _ in range(n)]
for x in range(n):
    for y in range(m):
        if x == 0:
            if y == 0:
                candy[x][y] = graph[x][y]
            else:
                candy[x][y] = graph[x][y] + candy[x][y - 1]
        elif 1 <= x <= n - 1:
            if y == 0:
                candy[x][y] = graph[x][y] + candy[x - 1][y]
            else:
                candy[x][y] = max(graph[x][y] + candy[x - 1][y],
                                  graph[x][y] + candy[x - 1][y - 1],
                                  graph[x][y] + candy[x][y - 1])
print(candy[-1][-1])
