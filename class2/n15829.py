"""
15829 - Hashing (브론즈 2)
"""

L = int(input())
alpha = list(input())

M = 1234567891
result = 0
for i in range(L):
    alpha[i] = ord(alpha[i]) - 96
    result += alpha[i] * 31**i

print(result % 1234567891)
