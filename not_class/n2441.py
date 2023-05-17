'''
2441번: 별 찍기 - 4 / bronze 3 / 구현
'''

n = int(input())

for i in range(n):
    star = i
    for j in range(n):
        if j >= star:
            print('*', end='')
        else:
            print(' ', end='')
    print()
