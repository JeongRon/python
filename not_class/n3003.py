'''
3003 - 킹, 퀸, 룩, 비숍, 나이트, 폰 (bronze 5)
'''
chess = [1, 1, 2, 2, 2, 8]

find = list(map(int, input().split()))

for i in range(6):
    print(chess[i] - find[i], end=' ')