'''
2752번: 세수 정렬 / bronze 4 / 구현
'''
num = list(map(int, input().split()))
num.sort()
for v in num:
    print(v, end=' ')
