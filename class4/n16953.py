"""
16953 - A → B / silver 2 / BFS
"""
import sys
from collections import deque

input = sys.stdin.readline

initial, result = map(int, input().split())

que = deque()
visited = set()
que.append((initial, 1))

flag = 0
while que:
    value, count = que.popleft()
    if value == result:
        flag = 1
        break
    res1 = value * 2
    res2 = value * 10 + 1
    if res1 <= result and res1 not in visited:
        que.append((res1, count + 1))
        visited.add(res1)
    if res2 <= result and res2 not in visited:
        que.append((res2, count + 1))
        visited.add(res2)

if flag == 1:
    print(count)
else:
    print(-1)
