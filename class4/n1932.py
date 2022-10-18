"""
1932 - 정수 삼각형 / silver 1 / DP
"""
import sys

input = sys.stdin.readline

# 1. Input
n = int(input().rstrip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 2. DP
for i in range(1, n):
    for j in range(i + 1):
        # 맨 왼쪽
        if j == 0:
            arr[i][j] = arr[i][j] + arr[i - 1][0]
        # 맨 오른쪽
        elif j == i:
            arr[i][j] = arr[i][j] + arr[i - 1][i - 1]
        # 가운데
        else:
            arr[i][j] = arr[i][j] + max(arr[i - 1][j - 1], arr[i - 1][j])

# 3. Print
print(max(arr[n - 1]))
