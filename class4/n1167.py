"""
1167 - 트리의 지름 / gold 2 / DFS, 트리 지름
"""
import sys

input = sys.stdin.readline

# 정점 개수 입력 받기
v = int(input())

# 트리 정보 입력 받기
graph = [[] for _ in range(v + 1)]
for _ in range(v):
    info = list(map(int, input().split()))
    for i in range(1, len(info) - 1, 2):
        graph[info[0]].append((info[i], info[i + 1]))

leaf = []
for n in range(1, v + 1):
    if len(graph[n]) == 1:
        leaf.append(n)


def dfs(now_dist, now_node, visited):
    if visited[now_node] == -1:
        visited[now_node] = now_dist
        for next_node, next_dist in graph[now_node]:
            dfs(now_dist + next_dist, next_node, visited)


visited = [-1] * (v + 1)
dfs(0, 1, visited)
node = visited.index(max(visited))

visited = [-1] * (v + 1)
dfs(0, node, visited)
print(max(visited))
