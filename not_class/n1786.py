'''
1786번: 찾기 / platinum 5 / KMP(Knuth-Morris-Pratt)
'''
# T, P 문자열 입력
T = input()
P = input()

# pi 리스트 만들기
pi = [0 for _ in range(len(P))]
pointer = 0
for i in range(1, len(P)):
    while pointer > 0 and P[i] != P[pointer]:
        pointer = pi[pointer - 1]
    if P[i] == P[pointer]:
        pointer += 1
        pi[i] = pointer

# same_cnt, same_index 구하기
same_cnt = 0
same_index = []
pointer = 0
# T 문자열 하나씩 확인하기
for i in range(len(T)):
    # T와 P 문자열 비교 중, 다를 시 처리
    while pointer > 0 and T[i] != P[pointer]:
        pointer = pi[pointer - 1]
    # T와 P 문자열 비교 중, 같을시 처리
    if T[i] == P[pointer]:
        # P 문자열과 같은 문자열 발견
        if pointer == len(P) - 1:
            same_index.append(i - len(P) + 2)
            same_cnt += 1
            pointer = pi[pointer]
        # 아직 P 문자열 아님
        else:
            pointer += 1
# 출력하기
print(same_cnt)
for v in same_index:
    print(v)
