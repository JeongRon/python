"""
18111 - 마인크래프트 (silver 2)
"""
import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
H_list = []
for _ in range(N):
    H_list += map(int, input().split())

time, height = float("inf"), 0

for H in range(257):
    p = 0
    q = 0
    for i in H_list:
        if H > i:
            p += H - i
        else:
            q += i - H

    inven = B + q - p
    if inven < 0:
        continue
    t = q * 2 + p
    if t <= time:
        time = t
        height = H

print(time, height)
