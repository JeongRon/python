'''
1476번: 날짜 계산 / silver 5 / 브루트포스
'''
# 1. 입력 받기
e, s, m = map(int, input().split())
# 2. x, y, z, year 선언 및 초기화
x, y, z = 1, 1, 1
year = 1
# 3. x, y, z == e, s, m 일때까지 반복
while True:
    if x == e and y == s and z == m:
        break
    x += 1
    y += 1
    z += 1
    year += 1
    if x == 16:
        x = 1
    if y == 29:
        y = 1
    if z == 20:
        z = 1

print(year)

