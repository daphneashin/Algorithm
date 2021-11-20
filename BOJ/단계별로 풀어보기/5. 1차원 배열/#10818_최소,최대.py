# 최솟값과 최댓값을 찾는 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 출처: https://www.acmicpc.net/problem/10818

import sys

n_ = int(input())
nlist_ = list(map(int, sys.stdin.readline().split()))
print(min(nlist_), max(nlist_))