import sys
'''
# 빠른 표준 입력 방법

# 공백으로 숫자 여려개 받기
a, b = map(int, sys.stdin.readline().split())
# 2차원 list 받기
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 문자열 입력 받기
s = sys.stdin.readline().rstrip()  # 끝에 엔터가 사용되기 때문에 rstrip 필요
'''


n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)