"""
2869 - 달팽이는 올라가고 싶다 (silver 5)
"""
import sys

up, down, height = map(int, sys.stdin.readline().split())
day = (height - down) / (up - down)
if day == int(day):
    print(int(day))
else:
    print(int(day) + 1)


# 내 첫 코드
# while True:
#     day += 1
#     height -= up
#     if height <= 0:
#         break
#     height += down

# review
# 시간 제한 맞추기 - 반복문 x , 일 수 한번에 계산 가능 식
# 참고 (https://stultus.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-2869-%EB%8B%AC%ED%8C%BD%EC%9D%B4%EB%8A%94-%EC%98%AC%EB%9D%BC%EA%B0%80%EA%B3%A0-%EC%8B%B6%EB%8B%A4)
#   while 1:
#       day += 1
#       if up * day - down * (day - 1) >= height:
#           break
# !! 시간 초과 발생 !!
# => 일수를 최소화 시키기
# if 문 보면, day >= (height - down) / (up - down) 으로 바꾸기
# day = (height - down) / (up - down)
