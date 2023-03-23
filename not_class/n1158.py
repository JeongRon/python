'''
1158번: 요세푸스 문제 / silver 4 / 큐
'''
# 1. n, k 입력 받기
n, k = map(int, input().split())
# 2. 리스트 만들기
arr = [i for i in range(1, n + 1)]
res = []
search_index = 0
# 3. 요세푸스 순열 구하기
for _ in range(n):
    search_index += k - 1
    search_index = search_index % len(arr)
    res.append(arr.pop(search_index))
# 4. 출력하기
print('<', end='')
for i in range(len(res) - 1):
    print(res[i], end=', ')
print(res[-1], end='')
print('>')
