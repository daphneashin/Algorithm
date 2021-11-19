# 별을 찍는 문제

t_ = int(input())
for i in range(1, t_+1, 1):
    print(' '*(t_-i)+'*'*i)
    # print(str('*'*i).rjust(t_)) → 오른쪽 정렬
# 출처: https://www.acmicpc.net/problem/2439