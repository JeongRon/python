'''
16139번: 인간-컴퓨터 상호작용 / silver 1 / 누적합
'''
import sys

input = sys.stdin.readline

s = input().rstrip()
q = int(input())
# 누적합 담을 arr 만들기
arr = [[0 for _ in range(26)] for _ in range(len(s))]
arr[0][ord(s[0]) - 97] = 1
for i in range(1, len(s)):
    for j in range(26):
        arr[i][j] += arr[i - 1][j]
    arr[i][ord(s[i]) - 97] += 1
# 누적합 이용하여 결과값 출력
for _ in range(q):
    alpha, start, end = input().split()
    start, end = int(start), int(end)
    if start == 0:
        print(arr[end][ord(alpha) - 97])
    else:
        print(arr[end][ord(alpha) - 97] - arr[start - 1][ord(alpha) - 97])
