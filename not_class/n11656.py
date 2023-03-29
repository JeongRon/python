'''
11656번: 접미사 배열 / silver 4 / 문자열-정렬
'''
# 1. 입력 받기
s = input()
# 2. 접미사 배열 arr 리스트 만들기
arr = []
for i in range(len(s)):
    arr.append(s[i:])
# 3. 사전순으로 정렬하기 (오름차순)
arr.sort()
# 4. 출력하기
for i in arr:
    print(i)
