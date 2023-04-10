'''
11057번: 오르막 수 / silver 1 / DP
'''
# 1. 입력 받기
n = int(input())
# 2. DP, sum_list 초기화
dp = [0 for i in range(1001)]
dp[1] = 10
sum_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 3. sum_list 활용하여  DP 채우기
for i in range(2, n + 1):
    dp[i] = sum(sum_list)
    print(sum_list)
    for j in range(10, 0, -1):
        sum_list[j - 1] = sum(sum_list[:j])

print(dp[n] % 10007)
