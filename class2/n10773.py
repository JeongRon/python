"""
10773 - 제로 (silver 4)
"""
import sys

input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    cash = int(input())
    if cash != 0:
        lst.append(cash)
    else:
        lst.pop()

# print("---------")
print(sum(lst))
