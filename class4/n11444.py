"""
11444 - 피보나치 수 6 / gold 2 / 분할 정복을 이용한 거듭제곱
"""

# 행렬 곱셈 계산 함수
def multiple(mat1, mat2):
    res = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += mat1[i][k] * mat2[k][j] % 1000000007
    return res


def power(a, b):
    if b == 1:
        return a
    else:
        tmp = power(a, b // 2)  # a **(b//2)
        # b가 짝수
        if b % 2 == 0:
            return multiple(tmp, tmp)
        # b가 홀수
        else:
            return multiple(multiple(tmp, tmp), a)


n = int(input())
matrix = [[1, 1], [1, 0]]

result = power(matrix, n)

print(result[0][1] % 1000000007)
