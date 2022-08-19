"""
1389 - 케빈 베이컨의 6단계 법칙 (silver 1)
"""
import sys
from collections import deque

input = sys.stdin.readline


def bfs(man):
    que = deque([[man, 0]])
    visited = [man]
    count = [0]

    while que:
        pop_man = que[0][0]
        pop_count = que[0][1]
        que.popleft()
        for j in friend_list[pop_man]:
            if j not in visited:
                visited.append(j)
                que.append([j, pop_count + 1])
                count.append(que[-1][1])
    # print("visited :", visited)
    # print("count :", count, " / sum :", sum(count))
    return sum(count)


n, m = map(int, input().split())
friend_list = [[] for _ in range(n + 1)]

for _ in range(m):
    p, q = map(int, input().split())
    friend_list[p].append(q)
    friend_list[q].append(p)

result_man = 0
result_count = 1e9

for i in range(1, n + 1):
    if result_count > bfs(i):
        result_count = bfs(i)
        result_man = i

print(result_man)
