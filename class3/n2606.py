"""
2606 - 바이러스 (silver 3)
"""
import sys

input = sys.stdin.readline


def bfs(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.add(i)
                queue.append(i)


N = int(input().rstrip())
M = int(input().rstrip())
dic = {}

for i in range(1, N + 1):
    dic[i] = set()
# print(dic)
for j in range(M):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)
# print(dic)

visited = set()
bfs(1, dic)
print(len(visited) - 1)
