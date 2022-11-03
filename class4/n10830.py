"""
10830 - 행렬 제곱 / gold 4 / 행렬 - 분할 정복을 이용한 거듭제곱 
"""
import sys

input = sys.stdin.readline

# 행렬 곱셈
def mul(m1, m2):
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp = 0
            for k in range(N):
                temp += m1[i][k] * m2[k][j]
            res[i][j] = temp % 1000
    return res


# a^b
def power(a, b):
    if b == 1:
        for i in range(N):
            for j in range(N):
                a[i][j] %= 1000
        return a
    else:
        a_half = power(a, b // 2)
        # b가 짝수 : A^(k//2) * A(k//2)
        if b % 2 == 0:
            return mul(a_half, a_half)
        # b가 홀수 : A^(k//2) A^(k//2) A
        else:
            return mul(mul(a_half, a_half), a)


# N: N*N행렬 / B: 행렬 제곱 / A: 행렬 리스트
N, B = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

result = power(A, B)

for i in range(N):
    for j in range(N):
        print(result[i][j], end=" ")
    print()
