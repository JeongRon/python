"""
1697 - 숨바꼭질 (silver 1)
"""
import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    que = deque([a])
    count = [0] * (100000 + 1)

    while que:
        x = que.popleft()

        if x == b:
            print(count[x])
            break

        for i in (x - 1, x + 1, 2 * x):
            if 0 <= i <= 100000 and count[i] == 0:
                que.append(i)
                count[i] = count[x] + 1


# 위치 a, b
a, b = map(int, input().split())

bfs()
