"""
1929 - 소수 구하기 (silver 3)
"""
import sys
import math

input = sys.stdin.readline

M, N = map(int, input().split())

for num in range(M, N + 1):
    is_prime = True
    if num == 1:
        is_prime = False
    else:
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        print(num)

# review - 1회_시간초과 / 2,3회_틀림
# 소수 구하기 시, 제곱근 활용하기!
# 처음 제곱근을 활용 안해서 시간초과가 났음
# 제곱근을 활용해서 for 반복문을 도는 것을 매우 낮추는 개념
# 2, 3일때의 경우를 생각 못해서 2,3회 틀린듯
