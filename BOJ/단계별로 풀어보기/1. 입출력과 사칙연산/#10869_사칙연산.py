# 모든 연산 문제
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력
# 출처: https://www.acmicpc.net/problem/10869

a, b = map(int, input().split())
print(a+b, a-b, a*b, a//b, a%b)

