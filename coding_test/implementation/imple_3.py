"""
왕실의 나이트
8 X 8 체스 좌표 평면상 나이트가 이동 할 수 있는 경우의 수
"""
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord("a")) + 1

step_list = [(-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, -2), (1, 2), (2, -1), (2, 1)]

result = 0
for step in step_list:
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)
