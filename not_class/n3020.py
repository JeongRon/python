'''
3020번: 개똥벌레 / gold 5 / 누적합
'''
import sys

input = sys.stdin.readline

# 1. 입력 받기
n, h = map(int, input().split())
down = [0 for _ in range(h + 1)]
up = [0 for _ in range(h + 1)]

for i in range(n):
    v = int(input())
    if i % 2 == 0:
        down[v] += 1
    else:
        up[v] += 1

# 2. 누적합
for i in range(h - 1, 0, -1):
    down[i] += down[i + 1]
    up[i] += up[i + 1]

# 3. 최소 값 도출
min_res = int(1e9)
min_cnt = 0
for i in range(1, h + 1):
    tmp_res = down[i] + up[h - i + 1]
    if min_res > tmp_res:
        min_res = tmp_res
        min_cnt = 1
    elif min_res == tmp_res:
        min_cnt += 1

print(min_res, min_cnt)
