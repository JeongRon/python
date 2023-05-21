'''
10797번: 10부제 / bronze 4 / 구현
'''
n = int(input())
car = list(map(int, input().split()))
cnt = 0
for v in car:
    if v == n:
        cnt += 1
print(cnt)
