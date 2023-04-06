'''
11052번: 카드 구매하기 / silver 1 / DP
'''
# 1. 카드 개수 n, 카드팩 card 입력 받기
n = int(input())
card = [0]
card += list(map(int, input().split()))
# 2. dp 리스트 만들기 / 카드 i일때, 최댓값 담기
dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    a = i
    b = 0
    while a != 0:
        case = card[a] + dp[b]
        if case > dp[i]:
            dp[i] = case
        a -= 1
        b += 1
# 3. dp[n] 출력 하기
print(dp[-1])
