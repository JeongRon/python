"""
1916 - 최소비용 구하기 / gold 5 / 최단경로(다익스트라+힙)
"""
import sys
import heapq

INF = 1e9

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        stack_dist, node = heapq.heappop(q)
        if distance[node] < stack_dist:
            continue
        for next_node, dist in graph[node]:
            new_stack_dist = dist + stack_dist
            if distance[next_node] > new_stack_dist:
                distance[next_node] = new_stack_dist
                heapq.heappush(q, (new_stack_dist, next_node))


dijkstra(start)

print(distance[end])
