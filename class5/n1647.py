"""
1647번 - 도시 분할 계획 / gold 4 / 최소 스패닝 트리
"""
import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(graph, (c, a, b))


def find(v):
    if root[v] == v:
        return v
    root[v] = find(root[v])
    return root[v]


def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root < y_root:
        root[y_root] = x_root
    else:
        root[x_root] = y_root


root = [i for i in range(n + 1)]
all_cost = []
while graph:
    cost, x, y = heapq.heappop(graph)
    if find(x) != find(y):
        union(x, y)
        all_cost.append(cost)

print(sum(all_cost) - max(all_cost))
