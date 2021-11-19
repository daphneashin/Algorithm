#빠르게 입력받고 출력하는 문제
# 출처: https://www.acmicpc.net/problem/15552

import sys

t_ = int(sys.stdin.readline())
for i in range(0, t_, 1):
    a_, b_ = map(int, sys.stdin.readline().split())
    print(a_+b_)