"""
재귀 1 - 팩토리얼
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
"""


def factorial(N):
    """팩토리얼"""
    result = 1
    if N > 0:
        result = N * factorial(N - 1)
    return result


N = int(input())
print(factorial(N))
