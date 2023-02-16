'''
1213번: 팰린드롬 만들기 / silver 3 / 문자열
'''

arr = input()
arr_cnt = [0 for _ in range(26)]
for s in arr:
    arr_cnt[ord(s) - 65] += 1

odd = 0
odd_s = ''
all_s = ''
for i in range(26):
    if arr_cnt[i] % 2 == 1:
        odd += 1
        odd_s += chr(i + 65)
    all_s += chr(i + 65) * (arr_cnt[i] // 2)

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(all_s + odd_s + all_s[::-1])
