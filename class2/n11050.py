"""
11050 - 이항 계수 1 (bronze 1) 
"""
N, K = map(int, input().split())

fac_N = 1
fac_K = 1
fac_NK = 1
for i in range(1, N + 1):
    fac_N *= i
for j in range(1, K + 1):
    fac_K *= j
for k in range(1, N - K + 1):
    fac_NK *= k
result = fac_N // (fac_K * fac_NK)
print(result)

# 식 : N! / k!(n-k)!
