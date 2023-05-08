'''
1302번: 베스트셀러 / silver 4 / 문자열, 정렬
'''
import sys

input = sys.stdin.readline

# 입력받기
N = int(input())
seller = []
for _ in range(N):
    book = input().rstrip()
    seller.append(book)

# 문자열 사전순으로 정렬하기
seller.sort()
# 베스트셀러 책 구하기
best_seller = [0, 'book_name']
tmp = [1, seller[0]]
for i in range(1, len(seller)):
    if tmp[1] == seller[i]:
        tmp[0] += 1
    else:
        if best_seller[0] < tmp[0]:
            best_seller[0] = tmp[0]
            best_seller[1] = tmp[1]
        tmp[0], tmp[1] = 1, seller[i]
if best_seller[0] < tmp[0]:
    best_seller[0] = tmp[0]
    best_seller[1] = tmp[1]
# 베스트셀러 책 출력하기
print(best_seller[1])
