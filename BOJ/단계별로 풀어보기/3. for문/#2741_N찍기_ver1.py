# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램

import sys

n = int(sys.stdin.readline())
for i in range(1, (n+1)):
    print(i)

# 출처: https://www.acmicpc.net/problem/2741