"""
9251 - LCS / gold 5 / DP
"""
first = list(input())
second = list(input())
array = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

for i in range(1, len(first) + 1):
    for j in range(1, len(second) + 1):
        if first[i - 1] == second[j - 1]:
            array[i][j] = array[i - 1][j - 1] + 1
        else:
            array[i][j] = max(array[i - 1][j], array[i][j - 1])

print(array[-1][-1])
