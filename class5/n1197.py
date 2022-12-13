'''
1197번 - 최소 스패닝 트리 / gold 4 / 최소 신장 트리, heapq
'''
import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
graph = []
for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(graph, (c, a, b))


def find(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, x, y):
    x_parent = find(parent, x)
    y_parent = find(parent, y)

    if x_parent > y_parent:
        parent[x_parent] = y_parent
    else:
        parent[y_parent] = x_parent


result = 0
while graph:
    dist, x, y = heapq.heappop(graph)
    if find(parent, x) != find(parent, y):
        union(parent, x, y)
        result += dist

print(result)
