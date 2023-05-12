'''
10039번: 평균 점수 / bronze 4 / 사칙연산
'''

all_score = 0
for _ in range(5):
    score = int(input())
    if score < 40:
        score = 40
    all_score += score
all_score //= 5
print(all_score)
