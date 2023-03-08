'''
1427번: 소트인사이드 / silver 5 / 문자열, 정렬
'''
# 1. 입력 받기
n = input()
# 2. 입력 받은 숫자 arr 리스트에 담기
arr = []
for i in n:
    arr.append(int(i))
# 3. arr 리스트 내림차순으로 정렬하기
arr.sort(reverse=True)
# 4. arr 리스트 출력
for v in arr:
    print(v, end='')
