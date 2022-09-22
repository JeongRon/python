"""
5525 - IOIOI (S1)
"""

N = int(input())
arr_len = int(input())
arr = input()

result = 0
count = 0
i = 0
while i < arr_len:
    if arr[i : i + 3] == "IOI":
        i += 2
        count += 1
        if N == count:
            result += 1
            count -= 1
    else:
        i += 1
        count = 0

print(result)
