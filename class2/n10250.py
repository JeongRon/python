"""
10250 - ACM 호텔
"""

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        building = H * 100
        unit = N // H
    else:
        building = N % H * 100
        unit = N // H + 1
    print(building + unit)


# 101 201 301 .. H01 / 102 202 302 .. H02 / .. H + W

# 10(N) // 6(H) = 1 + (1)
# 10(N) % 6(H) = 4
# = 402

# 72 // 30 = 2(몫) + (1)
# 72 % 30 = 12(나머지)
# = 1203

# 예외 처리
# 맨 위층일때는 원하는 값이 나오지 않음
