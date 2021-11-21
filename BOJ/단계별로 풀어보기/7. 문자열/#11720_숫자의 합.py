# 정수를 문자열로 입력받는 문제
# N개의 숫자가 공백 없이 쓰여있을때, 이 숫자를 모두 합해서 출력하는 프로그램
# 첫째 줄에는 숫자의 개수 N, 둘째 줄에는 숫자 n개가 공백없이 주어진다.
# 출처: https://www.acmicpc.net/problem/11720

n = int(input())
num_ = input()

print(sum(map(int, num_)))