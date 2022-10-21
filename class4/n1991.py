"""
1991 - 트리 순회 / silver 1 /
"""
import sys

input = sys.stdin.readline

tree = []
N = int(input().rstrip())
for _ in range(N):
    tree.append(list(input().split()))

print(tree)
