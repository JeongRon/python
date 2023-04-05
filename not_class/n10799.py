'''
10799번: 쇠막대기 / silver 2 / 스택
'''
# 1. 레이저 괄호 입력받기
laser = input()
slice_cnt = 0
stack = []

# 2. 잘려진 조각 개수 세기
for i in range(len(laser)):
    if laser[i] == '(':
        stack.append(laser[i])
    elif laser[i] == ')':
        if laser[i - 1] == '(':
            stack.pop()
            slice_cnt += len(stack)
        elif laser[i - 1] == ')':
            stack.pop()
            slice_cnt += 1

print(slice_cnt)
