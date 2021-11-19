# 빈 칸에 들어갈 수는?
# 출처: https://www.acmicpc.net/problem/2588

# 아래 함수들의 출력 결과는 동일
# mul_() → 수학적으로 접근한 방법
# mul_str1(), mul_str2() → 두번 째로 입력 받은 값을 역순으로 출력하여, 해당 값을 출력
def mul_():
    a = int(input())
    b = int(input())
    print(a*(b%10), a*((b%100)//10), a*((b%1000)//100), a*b)
    
def mul_str1():
    a = int(input())
    b = input()

    for i in reversed(b):
        print(a*int(i))
        
    print(a*int(b))

def mul_str2():
    a = int(input())
    b = input()

    for i in b[::-1]:
        print(a*int(i))
        
    print(a*int(b))