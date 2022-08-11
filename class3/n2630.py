"""
2630 - 색종이 만들기 (silver2)
"""
import sys

input = sys.stdin.readline

white = 0
blue = 0


def div_table(x, y, n):
    global white, blue

    right_table = table[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if right_table != table[i][j]:
                for a in range(2):
                    for b in range(2):
                        div_table(x + a * n // 2, y + b * n // 2, n // 2)
                return
    if right_table == 0:
        white += 1
    else:
        blue += 1


N = int(input().rstrip())
table = [list(map(int, input().split())) for _ in range(N)]

div_table(0, 0, N)

print(white)
print(blue)
