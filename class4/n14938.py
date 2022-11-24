'''
14938 - 서강그라운드 / gold 4 / 최단 경로
'''
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# n:지역 개수, m:수색 범위, r:길의 개수
n, m, r = map(int, input().split())

item_box = list(map(int, input().split()))
item_box.insert(0, 0)

graph = [[] for i in range(n + 1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


# 거리 / 아이템 수 / 해당 노드
def dijkstra(start):
    q = []
    visited = [INF] * (n + 1)
    visited[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        now_dist, now_node = heapq.heappop(q)
        for next_node, next_dist in graph[now_node]:
            if now_dist + next_dist < visited[next_node]:
                next_dist += now_dist
                visited[next_node] = next_dist
                heapq.heappush(q, (next_dist, next_node))

    res = 0
    for i in range(1, n + 1):
        if visited[i] <= m:
            res += item_box[i]
    return res


max_result = 0
for i in range(1, n + 1):
    result = dijkstra(i)
    if max_result < result:
        max_result = result

print(max_result)
