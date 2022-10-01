"""
9086 - 문자열 (B5)
"""
n = int(input())
for _ in range(n):
    letter = input()
    print(letter[0], end="")
    print(letter[-1])
