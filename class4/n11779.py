"""
11779 - 최소비용 구하기 2 / gold 3 / 다익스트라+힙
"""
import heapq

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

distance = [INF] * (n + 1)
distance_path = [[] for _ in range(n + 1)]


def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, [0, start, [start]])
    while q:
        stack_dist, node, path = heapq.heappop(q)
        if stack_dist > distance[node]:
            continue
        for next_node, dist in graph[node]:
            cost = stack_dist + dist
            if distance[next_node] > cost:
                distance[next_node] = cost
                distance_path[next_node] = path + [next_node]
                heapq.heappush(q, [cost, next_node, path + [next_node]])


dijkstra(start)

print(distance[end])
print(len(distance_path[end]))
for i in distance_path[end]:
    print(i, end=" ")
