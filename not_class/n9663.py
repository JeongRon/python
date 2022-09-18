"""
N-Queen (gold 4)
"""
# timeout!!!!! C언어로 대체

import sys

input = sys.stdin.readline


N = int(input())
count = 0
q_list = [0] * N


def is_put_queen(x, y, q_list):
    for i in range(x):
        if q_list[i] == y or abs(i - x) == abs(q_list[i] - y):
            return False
    return True


def n_queen(x):
    global count
    if x == N:
        count += 1
        return
    else:
        for y in range(N):
            q_list[x] = y
            if is_put_queen(x, y, q_list):
                n_queen(x + 1)


n_queen(0)
print(count)
