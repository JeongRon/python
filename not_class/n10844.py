'''
10844번: 쉬운 계단 수 / silver 1 / DP
'''
# 자릿수 n 입력
n = int(input())
# dp[x][y] / x는 자릿수, y는 맨 뒷자리 수, 값은 개수
dp = [[0 for _ in range(10)] for _ in range(101)]
# 한 자릿 수
for j in range(1, 10):
    dp[1][j] = 1
# 2~100 자릿수
for i in range(2, 101):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % 1000000000)
