"""
1018 - 체스판 다시 칠하기 (silver 4)
"""
import sys

input = sys.stdin.readline

M, N = map(int, input().split())

board = []
# board 판 채우기
for _ in range(M):
    board.append(tuple(input().strip()))

# board 판 출력
# print("board")
# index = 0
# while 1:
#     if index > M - 1:
#         break
#     print(board[index])
#     index += 1
# print("-----")

count_list = []
for x in range(M - 7):
    for y in range(N - 7):
        count1 = 0
        count2 = 0
        for i in range(x, x + 8):
            for j in range(y, y + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] == "W":
                        count1 += 1
                    if board[i][j] == "B":
                        count2 += 1
                else:
                    if board[i][j] == "B":
                        count1 += 1
                    if board[i][j] == "W":
                        count2 += 1
        count_list.append(min(count1, count2))

print(min(count_list))
