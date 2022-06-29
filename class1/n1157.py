"""
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
"""
# 단어 입력 + 모두 대문자로
word = input().upper()

# 딕셔너리 초기화 'A' : 0
alpha = {key: 0 for key in word}

# 알파벳 카운트 -> 딕셔너리에 넣기 'A': 3
for key in word:
    alpha[key] += 1

# 가장 많이 나온 알파벳 key, value 찾기
max_value = 0
for key, value in alpha.items():
    if value > max_value:
        max_value = value
        max_key = key

# 가장 많이 나온 알파벳 중복 확인
max_cnt = 0
for value in alpha.values():
    if value == max_value:
        max_cnt += 1

if max_cnt == 1:
    print(max_key)
else:
    print("?")
