"""
25372 - 성택이의 은밀한 비밀번호 / bronze 5
"""
n = int(input())
for _ in range(n):
    if 6 <= len(input()) <= 9:
        print("yes")
    else:
        print("no")
