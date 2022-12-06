'''
1918 - 후위 표기식 / gold 2 / 스택, 자료구조
'''

infix = input()

op_stack = []
postfix = ''

for v in infix:
    if v.isalpha():
        postfix += v
    else:
        if v == '(':
            op_stack.append(v)
        elif v == '*' or v == '/':
            while op_stack and (op_stack[-1] == '*' or op_stack[-1] == '/'):
                postfix += op_stack.pop()
            op_stack.append(v)
        elif v == '+' or v == '-':
            while op_stack and op_stack[-1] != '(':
                postfix += op_stack.pop()
            op_stack.append(v)
        elif v == ')':
            while op_stack[-1] != '(':
                postfix += op_stack.pop()
            op_stack.pop()

while op_stack:
    postfix += op_stack.pop()

print(postfix)
