"""
7568 - 덩치 (silver 5)
"""
import sys

N = int(sys.stdin.readline())

big_list = []
for _ in range(N):
    big = tuple(map(int, sys.stdin.readline().split()))
    big_list.append(big)

rank_list = []
for i in range(N):
    rank = 1
    for j in range(N):
        if big_list[i][0] < big_list[j][0] and big_list[i][1] < big_list[j][1]:
            rank += 1
    if i == N - 1:
        print(rank, end="")
    else:
        print(rank, end=" ")

# review
# 참고 : https://claude-u.tistory.com/122
# 완전 탐색 개념
