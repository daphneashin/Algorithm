# 숫자를 뒤집어서 비교하는 문제
# 출처: https://www.acmicpc.net/problem/2908

import sys

a_, b_ = sys.stdin.readline().split()
a_ = a_[::-1]
b_ = b_[::-1]

print(a_ if int(a_)>int(b_) else b_)
