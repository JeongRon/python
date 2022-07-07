"""
1181 - 단어 정렬 (silver 5)
"""

import sys

N = int(sys.stdin.readline())
words_list = []

# 리스트에 입력
for i in range(N):
    words_list.append(sys.stdin.readline().strip())

# set로 변환
set_list = set(words_list)
# 다시 리스트로 변환
words_list = list(set_list)
# 정렬 (알파벳 / 길이 순)
words_list.sort()
words_list.sort(key=len)
print("--------------")
for i in words_list:
    print(i)

# review
# 1. 입력 시, sys.stdin.readline() 사용하기 / input()보다 빠름
# 2. list를 set로 변환하면? / 요소 순서 없음, 중복된 값 없어짐
# 3. sort()함수 사용하면? / 알파벳순(오름차순)으로 정렬
# 4. sort(key=len) 사용하면? / 길이에 따라 오름차순 정렬
