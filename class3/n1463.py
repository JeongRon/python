"""
1463 - 1로 만들기 (silver 3)
"""
import sys

input = sys.stdin.readline

N = int(input().rstrip())
DP = [0] * (N + 1)

for i in range(2, N + 1):
    DP[i] = DP[i - 1] + 1
    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i // 3] + 1)
    if i % 2 == 0:
        DP[i] = min(DP[i], DP[i // 2] + 1)
print(DP[N])
