'''
1915 - 가장 큰 정사각형 (gold 4)
'''
import sys

input = sys.stdin.readline

x, y = map(int, input().split())

square = []
dp = [[0] * y for _ in range(x)]
result = 0

# 1. square 리스트에 입력 값 넣기
for _ in range(x):
    square.append(list(map(int, list(input().rstrip()))))



# 2. dp 리스트에 square값들 복사
for i in range(x):
    for j in range(y):
        if i == 0 or j == 0:
            dp[i][j] = square[i][j]
        elif square[i][j] == 0:
            pass
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        result = max(result, dp[i][j])
        
print(result * result)
