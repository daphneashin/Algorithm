# 윤년을 판별하는 문제
# 출처: https://www.acmicpc.net/problem/2753

year_ = int(input())

# 4의 배수이지만 100의 배수가 아닌 경우와 400의 배수인 경우 윤년이다.
# 윤년인 경우 1을 출력한다.
if ((year_%4==0 and year_%100 !=0) or (year_%400 ==0)):
    print("1")
else:
    print("0")