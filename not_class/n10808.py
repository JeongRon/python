'''
10808번: 알파벳 개수 / bronze 4 / 구현
'''
alpha = [0 for _ in range(26)]
S = input()

for i in S:
    alpha[ord(i) - 97] += 1

for v in alpha:
    print(v, end=' ')
