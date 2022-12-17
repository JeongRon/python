'''
9252번 - LCS 2 / gold 4 / DP
'''

first = list(input().rstrip())
second = list(input().rstrip())

arr = [[''] * (len(second) + 1) for _ in range(len(first) + 1)]

for i in range(1, len(first) + 1):
    for j in range(1, len(second) + 1):
        if first[i - 1] == second[j - 1]:
            arr[i][j] = arr[i - 1][j - 1] + first[i - 1]
        else:
            if len(arr[i - 1][j]) >= len(arr[i][j - 1]):
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = arr[i][j - 1]

print(len(arr[-1][-1]))
print(arr[-1][-1])
