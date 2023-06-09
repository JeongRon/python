'''
2443번: 별 찍기 - 6 / bronze 3 / 구현
'''
n = int(input())
start = 0
end = 2 * n - 2
for _ in range(n):
    i = 0
    while True:
        if i < start:
            print(' ', end='')
        elif start <= i <= end:
            print('*', end='')
        else:
            break
        i += 1
    print()
    start += 1
    end -= 1
