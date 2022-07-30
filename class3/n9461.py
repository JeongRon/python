"""
9461 - 파도반 수열 (silver 3)
"""
import sys

input = sys.stdin.readline

T = int(input().rstrip())
P = [0, 1, 1]
for _ in range(T):
    N = int(input().rstrip())
    for i in range(len(P), N + 1):
        P.append(P[i - 3] + P[i - 2])
    print(P[N])
