'''
1912번: 연속합 / silver 2 / DP
'''
# 1. 입력
n = int(input())
arr = list(map(int, input().split()))
# 2. dp / 순서대로 가장 큰 합을 저장하기
dp = [0 for _ in range(n)]
dp[0] = arr[0]
# 3. 0~i 까지에서의 가장 큰 합 찾기
for i in range(1, n):
    # dp[i] 에 현재 확인하는 숫자 arr[i] 합하기
    dp[i] = dp[i-1] + arr[i]
    # dp[i] 녀석이 arr[i]보다 작으면, arr[i]를 dp[i] 값으로 지정
    if arr[i] > dp[i]:
        dp[i] = arr[i]
# 4.출력
print(max(dp))
