'''
4354번: 문자열 제곱 / platinum 5 / KMP
'''
# 10번 이하 입력
for _ in range(10):
    # 전체 문자열 s 입력 받기
    s = input()
    # 종료 조건
    if s == '.':
        exit()
    # KMP / pi 리스트 만들기
    pi = [0 for _ in range(len(s))]
    pointer = 0
    for i in range(1, len(s)):
        while pointer > 0 and s[i] != s[pointer]:
            pointer = pi[pointer - 1]
        if s[i] == s[pointer]:
            pointer += 1
            pi[i] = pointer
    # a_len, share 구하기
    a_len = len(s) - pi[-1]
    share = len(s) // (a_len)
    # 출력하기
    if a_len * share == len(s):
        print(share)
    else:
        # len(s) % (a_len) 나머지가 있는 경우 길이가 달라진다.
        print(1)
