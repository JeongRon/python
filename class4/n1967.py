"""
1967 - 트리의 지름 / gold 4 / DFS
"""
import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())
# tree / 각 간선의 대한 정보
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

# 1번 노드에서 가장 긴 거리의 노드 찾기
distance = [-1] * (n + 1)
distance[1] = 0


def dfs(node, all_dist):
    for next_node, dist in tree[node]:
        if distance[next_node] == -1:
            distance[next_node] = all_dist + dist
            dfs(next_node, all_dist + dist)


dfs(1, 0)

# 1번 노드와 가장긴 노드 선택 / 그 노드와 가장 긴 노드 찾기
node = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[node] = 0

dfs(node, 0)

print(max(distance))
