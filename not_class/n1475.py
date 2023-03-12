'''
1475번: 방 번호 / silver 5 / 구현
'''
# 1. n 입력
n = input()
# 2. num_cnt / 각 숫자 개수 넣을 딕셔너리 선언 및 초기화
num_cnt = dict()
for i in range(9):
    num_cnt[i] = 0
# 3. 입력 받은 숫자 개수 세기
for num in n:
    key = int(num)
    if key == 9:
        num_cnt[6] += 1
    else:
        num_cnt[key] += 1
# 4. result / 숫자 개수 보고 필요한 세트의 개수 출력
result = 0
for key in range(9):
    if key == 6:
        cnt = num_cnt[key] // 2 + num_cnt[key] % 2
    else:
        cnt = num_cnt[key]
    if result < cnt:
        result = cnt
print(result)
