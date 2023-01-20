'''
14728번 - 벼락치기 / gold 5 / DP-배낭
'''
import sys

input = sys.stdin.readline

n, t = map(int, input().split())
dp = [[0 for _ in range(t + 1)] for _ in range(n + 1)]
exam = [(0, 0)]
for _ in range(n):
    k, s = map(int, input().split())
    exam.append((k, s))

for i in range(1, n + 1):
    time, score = exam[i]
    for j in range(1, t + 1):
        if j < time:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], score + dp[i - 1][j - time])

print(dp[n][t])
