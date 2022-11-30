"""
14652 - 나는 행복합니다~ / bronze 5
"""

row, col, num = map(int, input().split())

m = num // col
n = num - (col * m)
print(m, n)
