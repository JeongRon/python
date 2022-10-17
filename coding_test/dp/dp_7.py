"""
병사 배치하기
LIS(가장 긴 증가하는 부분 수열)
"""
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

# DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 출력
print(n - max(dp))
