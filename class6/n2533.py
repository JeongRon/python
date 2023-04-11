'''
2533번: 사회망 서비스(SNS) / gold 3 / dp, tree, dfs
'''
import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def dfs(start):
    visited[start] = 1
    for i in sns[start]:
        if visited[i] == 0:
            dfs(i)
            dp[start][1] += min(dp[i][0], dp[i][1])
            dp[start][0] += dp[i][1]
    dp[start][1] += 1


# 1. n, sns 친구 관계리스트 입력 받기
n = int(input())
sns = [[] for i in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    sns[u].append(v)
    sns[v].append(u)
# 2. dp, visited 리스트 만들기
dp = [[0, 0] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

# 3. dfs 실행
dfs(1)
# 4. 1번이 어뎁터가 아닐시, 맞을시의 결과 중 제일 작은 것 출력
print(min(dp[1][0], dp[1][1]))
