"""
1992 - 쿼드트리 (silver 1)
"""
import sys

input = sys.stdin.readline

quad_tree = []

# 1. input
n = int(input().rstrip())
for _ in range(n):
    line = list(map(int, input().rstrip()))
    quad_tree.append(line)

# 2. div quad_tree 분할 정복
def div_quad_tree(x, y, n):
    flag = quad_tree[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if quad_tree[i][j] != flag:
                flag = -1
                break

    if flag == -1:
        print("(", end="")
        div_quad_tree(x, y, n // 2)
        div_quad_tree(x, y + (n // 2), n // 2)
        div_quad_tree(x + (n // 2), y, n // 2)
        div_quad_tree(x + (n // 2), y + (n // 2), n // 2)
        print(")", end="")
    elif flag == 1:
        print(1, end="")
    elif flag == 0:
        print(0, end="")


div_quad_tree(0, 0, n)
