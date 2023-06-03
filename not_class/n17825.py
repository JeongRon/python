'''
17825번: 주사위 윷놀이 / gold 2 / 백트래킹
'''


# 말 위치에 따라 게임판 경로 전환하는 함수
def check_change_board(i, horse):
    # 5, 10, 15 지점일때, board (0) -> board (1) (2) (3)
    if horse[i][0] == 0:
        if horse[i][1] == 5:
            horse[i][0], horse[i][1] = 1, 0
        elif horse[i][1] == 10:
            horse[i][0], horse[i][1] = 2, 0
        elif horse[i][1] == 15:
            horse[i][0], horse[i][1] = 3, 0
        return
    # 25 중간 지점 거치면, / board (2)(3) 번 -> (1)번으로 change
    elif horse[i][0] == 2 and 3 <= horse[i][1] <= 5:
        horse[i][0], horse[i][1] = 1, horse[i][1] + 1
    elif horse[i][0] == 3 and 4 <= horse[i][1] <= 6:
        horse[i][0], horse[i][1] = 1, horse[i][1]
    # 40 위치에 도달 했을 시 -> board (0)
    elif len(board[horse[i][0]]) - 1 == horse[i][1]:
        horse[i][0] = 0
        horse[i][1] = len(board[horse[i][0]]) - 1


# 말 4개를 10턴 만큼 백트래킹하는 함수
def backtracking(depth, score, horse):
    global all_res
    # 종료 조건
    if depth == 10:
        all_res.append(score)
        return
    move = turn[depth]
    for i in range(4):
        # i번째 말 게임 판에 없고, 나가있으면 다른 말 선택
        if horse[i][1] >= len(board[horse[i][0]]):
            continue
        # i번째 말 움직이기
        pre_horse = [horse[i][0], horse[i][1]]
        horse[i][1] += move
        check_change_board(i, horse)
        # 움직인 말이 다른 말과 충돌나는지 확인
        collision = False
        # 게임 판 안에 있을 시,
        if len(board[horse[i][0]]) > horse[i][1]:
            for j in range(4):
                if i != j and horse[i][0] == horse[j][0] and horse[i][
                        1] == horse[j][1]:
                    collision = True
        # 충돌 발생 시, 제자리 위치로 + 다음 말
        if collision == True:
            horse[i][0], horse[i][1] = pre_horse[0], pre_horse[1]
        # 충돌 발생하지 않으면
        else:
            # 움직인 말이 게임판 안에 있을 시 score 추가,
            if len(board[horse[i][0]]) > horse[i][1]:
                score += board[horse[i][0]][horse[i][1]]
            # 백트래킹
            backtracking(depth + 1, score, horse)
            # 다시 원위치
            if len(board[horse[i][0]]) > horse[i][1]:
                score -= board[horse[i][0]][horse[i][1]]
            horse[i][0], horse[i][1] = pre_horse[0], pre_horse[1]


# 10턴 입력받기
turn = list(map(int, input().split()))
# 게임판 리스트
board = [[] for _ in range(4)]
board[0] = [i * 2 for i in range(21)]
board[1] = [10, 13, 16, 19, 25, 30, 35, 40]
board[2] = [20, 22, 24, 25, 30, 35, 40]
board[3] = [30, 28, 27, 26, 25, 30, 35, 40]
# 말 위치 정보
horse = [[0, 0], [0, 0], [0, 0], [0, 0]]
# 모두 나온 점수 결과
all_res = []
# 백트래킹 실행
backtracking(0, 0, horse)
# 나온 점수 결과 중 최댓값 출력
print(max(all_res))
