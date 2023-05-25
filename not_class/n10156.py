'''
10156번: 과자 / bronze 4 / 구현
'''
k, n, m = map(int, input().split())
buy = k * n
if buy > m:
    print(buy - m)
else:
    print(0)
