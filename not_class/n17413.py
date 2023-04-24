'''
17413번: 단어 뒤집기 2 / silver 3 / 구현, 스택, 문자열
'''
# S 문자열 입력받기
S = input()
# stack, reverse_flag 선언 및 초기화
stack = []
reverse_flag = True
# S 문자열 문자 하나씩 확인하기
for v in S:
    # flag=False일때
    if reverse_flag == False:
        print(v, end='')
        if v == '>':
            reverse_flag = True
    # flag=True일때
    else:
        # '<' 또는 ' ' 일때
        if v == '<' or v == ' ':
            # 스택에 담겨있던 값들 출력
            if stack:
                for i in range(len(stack) - 1, -1, -1):
                    print(stack[i], end='')
                stack.clear()
            print(v, end='')
            # '<' 일때 flag=False로 변환
            if v == '<':
                reverse_flag = False
        # stack에 문자 담기
        else:
            stack.append(v)
# 문자열 모두 확인 후, 스택에 담겨있는 값들 출력
if stack:
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i], end='')
