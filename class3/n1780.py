"""
1780 - 종이의 개수 (silver 2)
"""
import sys

input = sys.stdin.readline

minus = 0
zero = 0
plus = 0


def div_arr(x, y, N):
    global minus, zero, plus

    check_arr = arr[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if check_arr != arr[i][j]:
                for p in range(3):
                    for q in range(3):
                        div_arr(x + p * N // 3, y + q * N // 3, N // 3)
                return
    if check_arr == -1:
        minus += 1
    elif check_arr == 0:
        zero += 1
    else:
        plus += 1


N = int(input().rstrip())

arr = [list(map(int, input().split())) for _ in range(N)]

div_arr(0, 0, N)

print(minus)
print(zero)
print(plus)
