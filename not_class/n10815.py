'''
10815 - 숫자 카드 / silver 5 / 이분탐색
'''
import sys

input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
card.sort()
m = int(input())
check = list(map(int, input().split()))
for v in check:
    start = 0
    end = len(card) - 1
    flag = False
    while start <= end:
        mid = (start + end) // 2
        if card[mid] == v:
            flag = True
            break
        elif card[mid] < v:
            start = mid + 1
        elif card[mid] > v:
            end = mid - 1
    if flag:
        print(1, end=' ')
    else:
        print(0, end=' ')
