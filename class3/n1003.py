"""
1003 - 피보나치 함수 (silver 3)
"""
import sys

input = sys.stdin.readline

zero = 0
one = 0


def fib(n):
    global zero
    global one
    if n == 0:
        zero += 1
    elif n == 1:
        one += 1
    else:
        return fib(n - 1), fib(n - 2)


T = int(input())

for _ in range(T):
    fib(int(input()))
    print(zero, one)
    zero, one = 0, 0
