"""
1259 - 팰린드롬수 (브론즈 1)
"""
while True:
    case = list(input())
    if case[0] == "0":
        break
    elif case == case[-1::-1]:
        print("yes")
    else:
        print("no")

# 숫자를 팰린드롬
# 문자열로 취급해서 코드 작성
# 슬라이스 이용해서 인덱스 비교
