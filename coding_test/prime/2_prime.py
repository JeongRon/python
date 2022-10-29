"""
<< 약수의 성질 >>
- 모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이룬다.
    - 2 X 8 = 8 X 2 (대칭)
- 따라서 특정한 자연수의 모든 약수를 찾을 때 가운데 약수(제곱근)까지만 확인하면 된다.

<< 소수 판별 - 개선된 알고리즘 >>
- 2부터 X의 제곱근까지 연산 수행 / 시간 복잡도 O(N½)
"""
import math

# 소수 판별 함수 (2이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 x의 제곱근 까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


print(is_prime_number(4))
print(is_prime_number(7))
