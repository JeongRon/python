"""
문자열 재정렬

알파벳 대문자 / 숫자로 구성된 문자열 입력 주어지면,
알파벳 오름차순으로 정렬 + 그 뒤에는 모든 숫자를 더한 값 출력
EX) K1KA5CB7 => ACKK13
"""
data = input()
alpha_list = []
sum_num = 0

for i in data:
    if i.isalpha():
        alpha_list.append(i)
    else:
        sum_num += int(i)

alpha_list.sort()
if sum_num != 0:
    alpha_list.append(str(sum_num))

print("".join(alpha_list))
