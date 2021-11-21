# 각 문자를 반복하여 출력하는 문제
# 출처: https://www.acmicpc.net/problem/2675

t_ = int(input())
for i in range(0, t_):
    num_, str_ = input().split()
    pr_ = [j*int(num_) for j in str_]
    print(''.join(pr_))
