'''
2525번: 오븐 시계 / bronze 3 / 구현
'''

hour, min = map(int, input().split())
cook = int(input())

min += cook
if min // 60 != 0:
    tmp = min // 60
    min = min % 60
    hour += tmp
    while hour >= 24:
        hour -= 24
print(hour, min)
