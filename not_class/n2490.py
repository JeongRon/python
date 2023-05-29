'''
2490번: 윷놀이 / bronze 3 / 구현
'''
for _ in range(3):
    arr = list(map(int, input().split()))
    num = sum(arr)
    if num == 0:
        print('D')
    elif num == 1:
        print('C')
    elif num == 2:
        print('B')
    elif num == 3:
        print('A')
    elif num == 4:
        print('E')
