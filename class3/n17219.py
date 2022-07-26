"""
17219 - 비밀번호 찾기 (silver 4)
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
memo_list = {}

for _ in range(N):
    item = input().split()
    memo_list[item[0]] = item[1]

for _ in range(M):
    address = input().rstrip()
    print(memo_list[address])
