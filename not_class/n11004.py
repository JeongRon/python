'''
11004번: K번째 수 / silver 5 / 정렬
'''
# 1. 입력
n, k = map(int, input().split())
arr = list(map(int, input().split()))
# 2. 오름차순 정렬 + k번째 수 출력
arr.sort()
print(arr[k - 1])
