'''
1439번: 뒤집기 / silver 5 / 그리디
'''
# 1. 입력 받기
s = input()
# 2. 연속된 1, 0 카운트 하기
cnt = [0, 0]
sequence = int(s[0])
for i in range(1, len(s)):
    tmp = int(s[i])
    if tmp == sequence:
        continue
    else:
        cnt[sequence] += 1
        sequence = tmp
cnt[sequence] += 1
# 3. 카운트가 더 작은 수 프린트 하기
print(min(cnt))
