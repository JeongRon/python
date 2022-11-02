"""
1504 - 특정한 최단 경로 / gold 4 / 다익스트라+힙
"""
import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        stack_dist, node = heapq.heappop(q)

        if stack_dist > distance[node]:
            continue

        for next_node, next_dist in graph[node]:
            cost = stack_dist + next_dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return distance


dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)
# 1 -> v1 -> v2 -> n
result_1 = dist_1[v1] + dist_v1[v2] + dist_v2[n]
# 1 -> v2 -> v1 -> n
result_2 = dist_1[v2] + dist_v2[v1] + dist_v1[n]
min_result = min(result_1, result_2)

if min_result >= INF:
    print(-1)
else:
    print(min_result)
