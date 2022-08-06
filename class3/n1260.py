"""
1260 - DFS와 BFS (silver 2)
"""
import sys
from collections import deque

input = sys.stdin.readline


def dfs(v):
    visited.append(v)
    for i in lst[v]:
        if i not in visited:
            dfs(i)


def bfs(v):
    visited.append(v)
    que = deque([v])
    while que:
        for i in lst[que.popleft()]:
            if i not in visited:
                visited.append(i)
                que.append(i)


# n: 정점개수 / m: 간선개수 / v:시작정점
n, m, v = map(int, input().split())

visited = []
lst = [[] for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

for i in range(len(lst)):
    lst[i].sort()

dfs(v)
print(" ".join(str(i) for i in visited))
visited.clear()
bfs(v)
print(" ".join(str(i) for i in visited))
