'''
3085번: 사탕 게임 / silver 2 / 브루트포스
'''
import sys

input = sys.stdin.readline


def simulation():
    stack_len_row = []
    # 가로
    for i in range(N):
        stack_value = board[i][0]
        len = 1
        for j in range(1, N):
            if board[i][j] == stack_value:
                len += 1
            else:
                stack_len_row.append(len)
                len = 1
                stack_value = board[i][j]
        stack_len_row.append(len)
    # 세로
    stack_len_col = []
    for i in range(N):
        stack_value = board[0][i]
        len = 1
        for j in range(1, N):
            if board[j][i] == stack_value:
                len += 1
            else:
                stack_len_col.append(len)
                len = 1
                stack_value = board[j][i]
        stack_len_col.append(len)

    return max(max(stack_len_row), max(stack_len_col))


# 입력받기
N = int(input())
board = []
for _ in range(N):
    board.append(list(input().rstrip()))

# board에서 하나씩 브루트포스 탐색
max_candy = 0
dx = [0, 1]
dy = [1, 0]
for x in range(N):
    for y in range(N):
        for i in range(2):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < N:
                if board[x][y] != board[nx][ny]:
                    # change and simulation
                    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                    candy = simulation()
                    if max_candy < candy:
                        max_candy = candy
                    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
print(max_candy)
