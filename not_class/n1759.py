'''
1759번: 암호 만들기 / gold 5 / 브루트포스
'''
import sys

input = sys.stdin.readline


def reset_idx(p):
    if p == -1:
        exit(0)
    call_idx[p] += 1
    if call_idx[p] > call_idx_range[p]:
        reset_idx(p - 1)
    else:
        for i in range(p + 1, l):
            call_idx[i] = call_idx[i - 1] + 1


# 1. 입력 받기
l, c = map(int, input().split())
alpha = list(map(str, input().split()))
alpha.sort()
# 2. 필요한 리스트, 세트 만들기
consonant = {'a', 'e', 'i', 'o', 'u'}
call_idx = [i for i in range(l)]
call_idx_range = [0 for i in range(l)]
call_value = ['' for i in range(l)]
for i in range(l):
    call_idx_range[i] = c - l + i
# 3. 반복문 실행
while 1:
    consonant_cnt = 0
    vowel_cnt = 0
    # 3-1. idx 번호에 있는 값을 value 리스트에 넣기
    for i in range(l):
        call_value[i] = alpha[call_idx[i]]
        if call_value[i] in consonant:
            consonant_cnt += 1
        else:
            vowel_cnt += 1
    # 3-2. value 리스트 자음 모음 구성 체크 -> 맞으면 출력
    if consonant_cnt >= 1 and vowel_cnt >= 2:
        for v in call_value:
            print(v, end='')
        print()
    # 3-3. idx 번호 증가 시키기
    call_idx[l - 1] += 1
    if call_idx[l - 1] > call_idx_range[l - 1]:
        reset_idx(l - 2)
