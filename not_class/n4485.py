'''
4485번 - 녹색 옷 입은 애가 젤다지? / gold 4 / 다익스트라
'''
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra(n, graph, distance):
    que = [(graph[0][0], 0, 0)]
    while que:
        cost, x, y = heapq.heappop(que)
        if distance[x][y] <= cost:
            continue
        distance[x][y] = cost
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                heapq.heappush(que, (cost + graph[nx][ny], nx, ny))
    return distance[n - 1][n - 1]


cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    distance = [[INF for _ in range(n)] for _ in range(n)]
    res = dijkstra(n, graph, distance)
    print(f"Problem {cnt}: {res}")
    cnt += 1
