'''
2644번 - 촌수계산 / silver 2 / BFS
'''
import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, end, arr, visited):
    find_flag = False
    que = deque()
    que.append((start, 0))
    visited[start] = True
    while que:
        node, res = que.popleft()
        if node == end:
            find_flag = True
            print(res)
        for next_node in arr[node]:
            if not visited[next_node]:
                que.append((next_node, res + 1))
                visited[next_node] = True
    if not find_flag:
        print(-1)


n = int(input())
a, b = map(int, input().split())
arr = [[] for _ in range(n + 1)]
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
visited = [False] * (n + 1)
bfs(a, b, arr, visited)
