'''
2342번 - Dance Dance Revolution / gold 3 / DP (3차원 배열 점화식)
'''
import sys

input = sys.stdin.readline
INF = int(1e9)


def move(a, b):
    if a == b:
        return 1
    elif a == 0:
        return 2
    elif abs(a - b) % 2 == 1:
        return 3
    else:
        return 4


# 1. 입력받기 및 3차원 리스트 만들기
dance = [0] + list(map(int, input().split()))
dp = [[[INF for _ in range(5)] for _ in range(5)]
      for _ in range(len(dance) - 1)]
dp[0][0][0] = 0

# 2. dp 알고리즘 실행
for i in range(1, len(dance)):
    step = dance[i]
    if step == 0:
        break
    for left in range(5):
        for right in range(5):
            if dp[i - 1][left][right] == INF:
                continue
            if step != right:
                dp[i][step][right] = min(
                    dp[i][step][right],
                    dp[i - 1][left][right] + move(left, step))
            if step != left:
                dp[i][left][step] = min(
                    dp[i][left][step],
                    dp[i - 1][left][right] + move(right, step))

# 3. 결과값 도출
res = INF
for i in range(5):
    for j in range(5):
        if res > dp[-1][i][j]:
            res = dp[-1][i][j]

print(0 if res == INF else res)
