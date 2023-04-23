'''
10867번: 중복 빼고 정렬하기 / silver 5 / 정렬
'''
n = int(input())
arr = list(set(map(int, input().split())))
arr.sort()
for i in arr:
    print(i, end=' ')
