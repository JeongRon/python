'''
1010 - 다리 놓기 / silver 5 / 수학, 조합
'''
import sys
import math

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    res = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(res)
