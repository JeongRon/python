'''
1057번: 토너먼트 / silver 4 / 브루트포스 
'''


# A, B 친구가 같은 라운드에서 경기하는지 확인하는 함수
def check_round(div, N, A, B):
    A -= 1
    B -= 1
    if A // div == B // div:
        return True
    return False

    return False


# 참가자 수 N, 친구 둘 A, B 입력받기
N, A, B = map(int, input().split())
round = 1
div = 2
while True:
    if check_round(div, N, A, B) == True:
        break
    div *= 2
    round += 1
# round 출력
print(round)
