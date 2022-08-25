"""
3733 - Shares  (bronze 5)
"""

while True:
    try:
        n, s = map(int, input().split())
        print(s // (n + 1))
    except EOFError:
        break
