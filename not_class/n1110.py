'''
1110번: 더하기 사이클 / bronze 1 / 구현
'''
N = int(input())
num = N
cnt = 0
while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c
    cnt += 1
    if N == num:
        break
print(cnt)
