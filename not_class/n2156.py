'''
2156번: 포도주 시식 / sliver 1 / DP
'''
import sys

input = sys.stdin.readline

# 1. 입력 받기 n, wine
n = int(input())
wine = [0]
for _ in range(n):
    wine.append(int(input()))
# 2. DP 알고리즘
dp = [0 for _ in range(n + 1)]
dp[1] = wine[1]
if n > 1:
    dp[2] = wine[1] + wine[2]
for i in range(3, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i],
                dp[i - 2] + wine[i])
# 3. 출력 
print(dp[n])
