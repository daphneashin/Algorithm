# 0 0이 들어올 때까지 A+B를 출력하는 문제
# 출처: https://www.acmicpc.net/problem/10952

import sys

while(1):
    a, b = map(int, sys.stdin.readline().split())
    if ((a==0)and(b==0)):
        break
    else:
        print(a+b)
