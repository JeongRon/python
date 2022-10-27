"""
1753 - 최단경로 / gold 4 / 최단경로(다익스트라+힙)
"""
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())

graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)
start = int(input().rstrip())

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        stack_dist, node = heapq.heappop(q)
        if distance[node] < stack_dist:
            continue
        for next_node, dist in graph[node]:
            cost = stack_dist + dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))


dijkstra(start)

for dist in distance[1:]:
    if dist == INF:
        print("INF")
    else:
        print(dist)
