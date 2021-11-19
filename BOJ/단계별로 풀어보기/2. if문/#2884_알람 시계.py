# 시간 뺄셈 문제
# 출처: https://www.acmicpc.net/problem/2884

h,m = map(int, input().split())

m = m-45
if(m<0):
    m += 60 
    if h==0:
        h = 23
    else:
        h -= 1

print(h, m)