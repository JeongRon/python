"""
9019 - DSLR (G4)
"""
import sys
from collections import deque

input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    start, result = map(int, input().split())
    que = deque()
    visited = set()
    que.append((start, ""))

    while que:
        num, command = que.popleft()

        if num == result:
            print(command)
            break

        temp = num * 2 % 10000
        if temp not in visited:
            visited.add(temp)
            que.append((temp, command + "D"))

        temp = num - 1
        if temp == -1:
            temp = 9999
        if temp not in visited:
            visited.add(temp)
            que.append((temp, command + "S"))

        temp = (10 * num + (num // 1000)) % 10000
        if temp not in visited:
            visited.add(temp)
            que.append((temp, command + "L"))

        temp = (num // 10 + (num % 10) * 1000) % 10000
        if temp not in visited:
            visited.add(temp)
            que.append((temp, command + "R"))
