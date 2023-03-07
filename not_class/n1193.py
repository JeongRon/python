'''
1193번: 분수찾기 / silver 5 / 구현
'''
# 1. 입력
x = int(input())
# 2. row_value 리스트 만들기 / 인덱스번호: row번  값: X번째
row_value = [0, 1]
num = 1
increase = 1
while True:
    if num >= 10000000:
        break
    num += increase
    row_value.append(num)
    increase += 1
# 3. x가 몇 번째 row 인지 확인 / x_row
for i in range(1, len(row_value)):
    if x < row_value[i]:
        x_row = i - 1
        break
# 4. x_row 홀수-짝수 판별해서 cnt, a, b 얻기
# cnt : (x_row)열은 cnt번째 부터 시작
# a, b : 분자, 분모
if x_row % 2 == 0:
    a, b = 1, x_row
    plus_a, plus_b = 1, -1
else:
    a, b = x_row, 1
    plus_a, plus_b = -1, 1
cnt = row_value[x_row]
# 5. cnt번째 값을 계속 하나씩 더하면서, 분수도 증감 연산 => x번째 값 도착하면 결과값 도출
while True:
    if cnt == x:
        print(f"{a}/{b}")
        break
    a += plus_a
    b += plus_b
    cnt += 1
