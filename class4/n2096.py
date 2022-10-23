"""
2096 - 내려가기 / gold 5 / DP
"""
n = int(input())

dp_min = [0, 0, 0]
dp_max = [0, 0, 0]
temp_min = [0, 0, 0]
temp_max = [0, 0, 0]

for i in range(n):
    first, second, third = map(int, input().split())

    dp_min[0] = first + min(temp_min[0], temp_min[1])
    dp_min[1] = second + min(temp_min[0], temp_min[1], temp_min[2])
    dp_min[2] = third + min(temp_min[1], temp_min[2])

    dp_max[0] = first + max(temp_max[0], temp_max[1])
    dp_max[1] = second + max(temp_max[0], temp_max[1], temp_max[2])
    dp_max[2] = third + max(temp_max[1], temp_max[2])

    temp_min[0], temp_min[1], temp_min[2] = dp_min[0], dp_min[1], dp_min[2]
    temp_max[0], temp_max[1], temp_max[2] = dp_max[0], dp_max[1], dp_max[2]


print(max(dp_max), min(dp_min))
