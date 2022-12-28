"""
20040번 - 사이클 게임 / gold 4 / 최소 스패닝 트리
"""
import sys

input = sys.stdin.readline


def find(v):
    if root[v] == v:
        return v
    root[v] = find(root[v])
    return root[v]


def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root < y_root:
        root[y_root] = root[x_root]
    else:
        root[x_root] = root[y_root]


n, m = map(int, input().split())

root = [i for i in range(n)]
flag = False
result = 0

for cnt in range(m):
    a, b = map(int, input().split())
    if flag:
        continue
    if find(a) != find(b):
        union(a, b)
    else:
        result = cnt + 1
        flag = True

print(result)
