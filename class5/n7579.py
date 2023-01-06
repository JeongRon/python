'''
7579번 - 앱 / gold 3 / DP(냅색 알고리즘)
'''
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(sum(cost) + 1)] for _ in range(n + 1)]
min_cost = sum(cost)

for row in range(1, n + 1):
    byte = memory[row]
    expense = cost[row]
    for col in range(1, sum(cost) + 1):
        if col < expense:
            dp[row][col] = dp[row - 1][col]
        else:
            dp[row][col] = max(byte + dp[row - 1][col - expense],
                               dp[row - 1][col])
        if dp[row][col] >= m:
            min_cost = min(min_cost, col)

for i in dp:
    print(i)
if m == 0:
    print(0)
else:
    print(min_cost)
