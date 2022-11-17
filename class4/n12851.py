"""
12851 - 숨바꼭질 2 / gold 4 / BFS
"""
import sys
from collections import deque

input = sys.stdin.readline


n, k = map(int, input().split())
# 2차원 배열 활용 info[n][0] , info[n][1]
# info[n][0]: 가장 빠른 시간 , info[n][1]: 가장 빠른 시간으로 찾은 방법 개수
info = [[-1, 0] for _ in range(100001)]

que = deque([n])
info[n][0] = 0
info[n][1] = 1

while que:
    flag = que.popleft()

    for point in [flag * 2, flag + 1, flag - 1]:
        if 0 <= point <= 100000:
            # 처음으로 접근 했을 경우
            if info[point][0] == -1:
                info[point][0] = info[flag][0] + 1
                info[point][1] = info[flag][1]
                que.append(point)
            # 처음이 아닌 경우 + 가장 빠른 시간과 같은지
            elif info[point][0] == info[flag][0] + 1:
                info[point][1] += info[flag][1]

print(info[k][0])
print(info[k][1])
