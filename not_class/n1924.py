'''
1924번: 2007년 / bronze 1 / 구현
'''
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

x, y = map(int, input().split())

day = 0
for i in range(1, x):
    day += month[i]
day += y
day %= 7
print(week[day])
