# 출처: https://www.acmicpc.net/problem/1712
# A는 고정비용, B는 단가, C는 판매가격
# A, B, C가 주어졌을 때, 최초로 손익분기점을 넘길 때의 판매량을 출력한다. 손익분기점이 존재하지 않으면 -1을 출력한다.

import sys
a, b, c = map(int, sys.stdin.readline().split())

if b>=c:
    print(-1)
else:
    print((a//(c-b))+1)