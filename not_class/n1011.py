'''
1011번 - Fly me to the Alpha Centauri / gold 5 / 규칙
'''
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    long = y - x
    tmp_long = 0
    cnt = 0
    move = 1
    while tmp_long < long:
        cnt += 1
        tmp_long += move
        if cnt % 2 == 0:
            move += 1
    print(cnt)
