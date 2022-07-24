"""
1620 - 나는야 포켓몬 마스터 이다솜 (silver 4)
"""
import sys

input = sys.stdin.readline

poketmon_dict = {}
poketmon_dict_2 = {}
N, M = map(int, input().split())
for i in range(1, N + 1):
    cmd = input()
    poketmon_dict[i] = cmd
    poketmon_dict_2[cmd] = i
for _ in range(M):
    Q = input()
    try:
        Q = int(Q)
        print(poketmon_dict[Q], end="")
    except:
        print(poketmon_dict_2[Q])

# review
# 처음에는 리스트 하나를 만들어서 해당 인덱스<->값 불러오는 형식으로 코드 작성
# 시간 초과 문제 발생 / 맞는 해당 인덱스를 찾을 때 시간 많이 소요
# 그다음, 딕셔너리 사용 생각
# 딕셔너리 key : value 를 활용해서 두개의 딕셔너리 만듬
# 1번 딕셔너리  Num : poketmon
# 2번 딕셔너리  poketmon : Num
