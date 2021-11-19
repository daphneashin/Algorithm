# n이 주어졌을 때, 1부터  n까지 합을 구하는 프로그램 - using for문
# 출처: https://www.acmicpc.net/problem/8393

n = int(input())
sum = 0

for i in range(1, (n+1), 1):
    sum += i

print(sum)