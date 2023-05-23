'''
2530번: 인공지능 시계 / bronze 4 / 구현
'''
hour, min, sec = map(int, input().split())
cook_sec = int(input())

sec += cook_sec
if sec >= 60:
    cook_min = sec // 60
    sec = sec % 60
    min += cook_min
    if min >= 60:
        cook_hour = min // 60
        min = min % 60
        hour += cook_hour
        if hour >= 24:
            hour = hour % 24
print(hour, min, sec)
