'''
2941번: 크로아티아 알파벳 / sliver 5 / 문자열
'''


def cnt_alpha(i):
    if i + 1 < len(alpha):
        if alpha[i] == 'c' and (alpha[i + 1] == '=' or alpha[i + 1] == '-'):
            i += 2
        elif alpha[i] == 'd' and alpha[i + 1] == '-':
            i += 2
        elif alpha[i] == 'd' and i + 2 < len(alpha) and alpha[
                i + 1] == 'z' and alpha[i + 2] == '=':
            i += 3
        elif (alpha[i] == 'l' or alpha[i] == 'n') and alpha[i + 1] == 'j':
            i += 2
        elif (alpha[i] == 's' or alpha[i] == 'z') and alpha[i + 1] == '=':
            i += 2
        else:
            i += 1
    else:
        i += 1
    return i


alpha = input()
cnt = 0
i = 0
while i < len(alpha):
    i = cnt_alpha(i)
    cnt += 1
print(cnt)
