'''
2776번: 암기왕 / silver 4 / set
'''
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = set(map(int, input().split()))
    m = int(input())
    note = list(map(int, input().split()))
    for v in note:
        if v in arr:
            print(1)
        else:
            print(0)
