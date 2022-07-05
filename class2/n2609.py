"""
2609 - 최대공약수와 최소공배수 (브론즈 1)
"""

a, b = map(int, input().split())
a_divisor = {i for i in range(1, a + 1) if a % i == 0}
b_divisor = {i for i in range(1, b + 1) if b % i == 0}
max_divisor = max(a_divisor & b_divisor)
multiple = max_divisor * (a // max_divisor) * (b // max_divisor)
print(max_divisor)
print(multiple)

# 1. 최대공약수 - set 이용 / {} + &(교집합)
# 2. 최소공배수
