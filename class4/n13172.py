"""
13172 - Σ / gold 4 / 분할 정복을 이용한 거듭제곱
(기댓값) = (s × n^(1,000,000,005)) % 1,000,000,007
"""
import sys

input = sys.stdin.readline
M = 1000000007


def expected_value(n, s):
    return s * n_power(n, M - 2) % M


def n_power(n, power):
    if power == 1:
        return n
    if power % 2 == 0:
        div = n_power(n, power // 2)
        return div * div % M
    else:
        return n * n_power(n, power - 1) % M


m = int(input())

res = 0
for _ in range(m):
    n, s = map(int, input().split())
    res += expected_value(n, s)
    res %= M

print(res)
