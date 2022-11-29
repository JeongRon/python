'''
1238 - 파티 / gold 3 / 최단 경로
'''
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (n + 1)
distance[0] = 0


def dikstra(start):
    # 거리, 현재 노드
    q = [(0, start)]
    distance[start] = 0
    while q:
        stack_dist, now_node = heapq.heappop(q)
        for next_node, dist in graph[now_node]:
            cost = stack_dist + dist
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))


def shortest_path(start, end):
    visited = [INF] * (n + 1)
    visited[start] = 0
    q = [(0, start)]
    while q:
        stack_dist, now_node = heapq.heappop(q)
        for next_node, dist in graph[now_node]:
            cost = stack_dist + dist
            if visited[next_node] > cost:
                visited[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return visited[end]


# x 시작 -> distance 리스트에 각 노드들의 거리 측정 (파티 끝나고 가는 경우)
dikstra(x)

# 각 노드들 시작 -> x까지의 거리 distance 리스트에 더하기 (파티 장소에 가는 경우)
for i in range(1, n + 1):
    distance[i] += shortest_path(i, x)

print(max(distance))
