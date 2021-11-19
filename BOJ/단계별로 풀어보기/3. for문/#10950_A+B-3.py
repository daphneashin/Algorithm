# 주어진 테스트케이스의 개수만큼, 입력 받은 두 정수 A와 B의 합을 구하는 프로그램
# 출처: https://www.acmicpc.net/problem/10950

for i in range(0, int(input()), 1):
    print(sum(map(int, input().split())))