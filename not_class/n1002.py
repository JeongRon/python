'''
1002번 - 터렛 / silver 3 / 수학-기하학
'''
import sys
import math

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c, x, y, z = map(int, input().split())
    dis = math.sqrt((a-x)**2 + (b-y)**2) 
    if dis == 0:
        if c==z:
            print(-1)
        else:
            print(0)
    else:
        if c+z == dis or abs(c-z) == dis:
            print(1)
        elif abs(c-z) < dis < c+z:
            print(2)
        else:
            print(0)
    
