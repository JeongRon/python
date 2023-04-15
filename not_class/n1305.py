'''
1305번: 광고 / platinum 4 / KMP
'''
# 광고판의 길이 L, 광고판 문자열 board 입력 받기
L = int(input())
board = input()
# pi 리스트 만들기
pi = [0 for _ in range(L)]
j = 0
for i in range(1, L):
    while j > 0 and board[i] != board[j]:
        j = pi[j - 1]
    if board[i] == board[j]:
        j += 1
        pi[i] = j
print(pi)
# 실제 광고 최소 길이 출력하기
print(L - pi[-1])
