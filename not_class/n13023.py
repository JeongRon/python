'''
13023번: ABCDE / gold 5 / 백트래킹
'''
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)


# 백트래킹을 이용한 친구 관계 확인
def check_friend(s):
    # 조건에 맞는 친구 관계 있을 시 / 종료조건
    if len(visited) == 5:
        print(1)
        exit()
    for next in relation[s]:
        if next not in visited:
            visited.add(next)
            check_friend(next)
            visited.remove(next)


# 입력받기
N, M = map(int, input().split())
relation = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)
# 0~N-1 친구까지 확인하기
start = 0
end = N - 1
while start <= end:
    visited = set()
    check_friend(start)
    start += 1
print(0)
