"""
15650 - N과 M (2) / S(3)
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

sequence = []


def dfs(start):
    if len(sequence) == M:
        for i in sequence:
            print(i, end=" ")
        print()
        return
    else:
        for i in range(start, N + 1):
            if i not in sequence:
                sequence.append(i)
                dfs(i + 1)
                sequence.pop()


dfs(1)
