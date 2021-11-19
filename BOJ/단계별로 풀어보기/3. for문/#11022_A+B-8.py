# 주어진 테스트케이스의 개수만큼, 입력 받은 두 정수 A와 B의 합을 구하는 프로그램
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다.  
# 출처: https://www.acmicpc.net/problem/11022

t_ = int(input())
for i in range(1, t_+1, 1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a} + {b} = {a+b}")