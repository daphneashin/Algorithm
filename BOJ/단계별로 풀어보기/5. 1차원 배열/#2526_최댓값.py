# 최댓값이 어디에 있는지 찾는 문제
# N개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지 구하는 프로그램
# 출처: https://www.acmicpc.net/problem/2562

import sys
nlist_ = [int(sys.stdin.readline()) for i in range(9)]

print(f'{max(nlist_)}\n{nlist_.index(max(nlist_))+1}')
