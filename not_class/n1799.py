'''
1799번: 비숍 / gold 1 / 백트래킹
'''
import sys

input = sys.stdin.readline


# 해당 (x, y) 비숍이 그 전에 두었던 비숍과 충돌이 나는지 확인하는 함수
def collision(x, y, bishop):
    for a, b in bishop:
        if abs(a - x) == abs(b - y):
            return True
    return False


# 백트래킹 함수
def backtracking(x, y, board, bishop):
    if x == n - 1 and y == n:
        global result
        result.append(len(bishop))
        return
    if y == n:
        backtracking(x + 1, 0, board, bishop)
        return
    if board[x][y] == 1 and not collision(x, y, bishop):
        board[x][y] = 2
        bishop.append((x, y))
        backtracking(x, y + 1, board, bishop)
        board[x][y] = 1
        bishop.pop()
        backtracking(x, y + 1, board, bishop)
    else:
        backtracking(x, y + 1, board, bishop)


# 입력받기
n = int(input())
black = [[0 for _ in range(n)] for _ in range(n)]
white = [[0 for _ in range(n)] for _ in range(n)]
# 체스판을 black, white 두 개의 판으로 분류
for i in range(n):
    graph = list(map(int, input().split()))
    for j in range(n):
        if graph[j] == 1:
            if (i + j) % 2 == 0:
                black[i][j] = 1
            else:
                white[i][j] = 1

# black 체스판 백트래킹
bishop = []
result = []
backtracking(0, 0, black, bishop)
black_max = max(result)
# white 체스판 백트래킹
bishop = []
result = []
backtracking(0, 0, white, bishop)
white_max = max(result)
# black, white 백트래킹 최댓값 더해서 출력
print(black_max + white_max)
