"""
2407 - 조합 (S4)
"""
from math import factorial
import sys

input = sys.stdin.readline

n, r = map(int, input().split())

print(factorial(n) // (factorial(n - r) * factorial(r)))
