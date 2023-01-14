'''
1058번 - 친구 / silver 2 / 브루트포스
'''
import sys

input = sys.stdin.readline

# 1. 입력 및 리스트 생성
n = int(input())

best_friend = [[] for _ in range(n)]
for i in range(n):
    info = list(input().rstrip())
    for j in range(n):
        if info[j] == 'Y':
            best_friend[i].append(j)

# 2. 프루트포스
friend = [set() for _ in range(n)]
for i in range(n):
    for j in best_friend[i]:
        friend[i].add(j)
        for k in best_friend[j]:
            friend[i].add(k)
# 3. 결과 출력
res = 0
for i in range(n):
    if res < len(friend[i]):
        res = len(friend[i])
print(res - 1 if res > 0 else res)
