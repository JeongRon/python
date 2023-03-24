'''
2217번: 로프 / silver 4 / 그리디, 정렬
'''
import sys

input = sys.stdin.readline

# 1. 입력 받기
n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))
# 2. 로프 리스트 오름차순 하기
rope.sort(reverse=True)
# 3. 최대 중량 구하기
res_weight = 0
for i in range(len(rope)):
    rope_cnt = i + 1
    if res_weight < rope[i] * rope_cnt:
        res_weight = rope[i] * rope_cnt
print(res_weight)
