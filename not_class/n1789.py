'''
1789번: 수들의 합 / silver 5 / 그리디
'''
# 1. 입력 받기
s = int(input())
# 2.변수 선언 및 초기화
res = 0
num = 1
cnt = 0
# 3. cnt 구하기
while res <= s:
    res += num
    num += 1
    cnt += 1
print(cnt - 1)
