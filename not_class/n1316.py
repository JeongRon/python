'''
1316번 - 그룹 단어 체커 / silver 5 / dict, string
'''
import sys

input = sys.stdin.readline


def is_group_word(word):
    i = 0
    group = dict()
    while i < len(word):
        now = word[i]
        if group.get(now):
            return 0
        group[now] = 1
        i += 1
        if i == len(word):
            break
        while now == word[i]:
            i += 1
            if i == len(word):
                break
    return 1


cnt = 0
for _ in range(int(input())):
    word = input()
    if is_group_word(word):
        cnt += 1
print(cnt)
