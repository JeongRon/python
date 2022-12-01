"""
1865 - 웜홀 / gold 3 / 벨만-포드
"""
import sys

input = sys.stdin.readline
INF = int(1e9)


def bellman_ford():
    visited = [INF] * (n + 1)
    visited[1] = 0
    for node in range(1, n + 1):
        for search_node in range(1, n + 1):
            for next_node, dist in graph[search_node]:
                if visited[next_node] > visited[search_node] + dist:
                    visited[next_node] = visited[search_node] + dist
                    if node == n:
                        return True
    return False


t = int(input())

for _ in range(t):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    for _ in range(w):
        a, b, c = map(int, input().split())
        graph[a].append((b, -c))
    if bellman_ford():
        print("YES")
    else:
        print("NO")
