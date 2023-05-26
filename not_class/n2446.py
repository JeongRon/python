'''
2446번: 별 찍기 - 9 / bronze 3 / 구현
'''
n = int(input())

start, end = 0, 2 * n - 2
for row in range(2 * n - 1):
    for col in range(end + 1):
        if col >= start:
            print('*', end='')
        else:
            print(' ', end='')
    print()
    if row < n - 1:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
