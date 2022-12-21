'''
4172번 - sqrt log sin / silver 3 / DP
'''
import math

dp = [1 for _ in range(1000000 + 1)]

for i in range(1, 1000000 + 1):
    dp[i] = (dp[math.floor(i - math.sqrt(i))] + dp[math.floor(math.log(i))] +
             dp[math.floor(i * math.sin(i) * math.sin(i))]) % 1000000

while True:
    n = int(input())
    if n == -1:
        break
    print(dp[n])
