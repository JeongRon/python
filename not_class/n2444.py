'''
2444번: 별 찍기 - 7 / bronze 3 / 구현
'''
n = int(input())
start, end = n - 1, n - 1
for i in range(2 * n - 1):
    for j in range(end + 1):
        if j >= start:
            print('*', end='')
        else:
            print(' ', end='')
    print()
    if i <= n - 2:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1
