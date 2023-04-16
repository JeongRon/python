'''
1946번: 신입 사원 / silver 1 / 그리디, 정렬
'''
import sys

input = sys.stdin.readline

T = int(input())
# 테스트 케이스 T 횟수 만큼 반복
for _ in range(T):
    # 지원자 수 N 입력 받기
    N = int(input())
    # 지원자 [서류, 면접] 등수 applicant 리스트에 담기
    applicant = []
    for _ in range(N):
        x, y = map(int, input().split())
        applicant.append([x, y])
    # 지원자 서류 등수로 오름차순 정렬
    applicant.sort(key=lambda x: x[0])
    # 선발되지 않는 사람 cnt
    score = applicant[0][1]
    cnt = 0
    for i in range(1, N):
        if score < applicant[i][1]:
            cnt += 1
        else:
            score = applicant[i][1]
    # 선발인원 출력하기
    print(N - cnt)
