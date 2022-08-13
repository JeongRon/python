"""
11724 - 연결 요소의 개수 (silver 2)
"""
import sys

input = sys.stdin.readline


def dfs(start):
    visited[start] = True
    for i in connect_list[start]:
        if not visited[i]:
            dfs(i)


# 정점 개수 N, 간선 개수 M
N, M = map(int, input().split())
connect_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    connect_list[u].append(v)
    connect_list[v].append(u)

count = 0
for i in range(1, N + 1):
    if not visited[i]:
        if not connect_list[i]:
            visited[i] = True
        else:
            dfs(i)
        count += 1

print(count)
