'''
4673번: 셀프 넘버 / silver 5 / 브루트포스
'''

# d(v) / 생성 숫자 만드는 함수
def d(v):
    tmp = v
    if 1 <= v <= 9:
        tmp += v
    else:
        while v // 10 != 0:
            tmp += v % 10
            v = v // 10
        tmp += v % 10
    return tmp

# 1. self / 1~10000 까지의 수가 들어 있는 세트 만들기
self = {i for i in range(1, 10001)}
# 2. 모든 숫자 1~10000로 인해 생성된 숫자 구하고, self 세트에서 제외 시키기   
for i in range(1, 10001):
    num = d(i)
    self.discard(num)
# 3. self 세트를 리스트로 바꾸고, 정렬되게 설정
self = list(self)
self.sort()
# 4. 출력
for i in self:
    print(i)
