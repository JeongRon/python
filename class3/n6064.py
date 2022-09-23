"""
6064 - 카잉 달력 (S1)
"""


def find_result(M, N, x, y):
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        else:
            x += M
    return -1


T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(find_result(M, N, x, y))
