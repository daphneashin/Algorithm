# 두 수를 비교한 결과를 출력하는 문제
# 출처: https://www.acmicpc.net/problem/1330

a,b = map(int, input().split())

if a==b:
    print("==")
elif a<b:
    print("<")
else:
    print(">")