"""
10816 - 숫자 카드 2 (silver 4)
"""

import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

card = map(int, input().split())

M = int(input())

num = map(int, input().split())

C = Counter(card)

for key in num:
    if not C[key]:
        print(0, end=" ")
    else:
        print(C[key], end=" ")

# review
# card리스트에 있는 것들을 하나씩 count 시키게끔 처음에 접근 -> 시간초과
# collection의 Counter 사용 방법 활용
# 딕셔너리? 같이 key: value 로 Counter 되는 방식으로 되어 있음
