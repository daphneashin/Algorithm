# 함수 d를 정의하여 문제를 해결
# 출처: https://www.acmicpc.net/problem/4673

def d(n):
    sum_ = n
    for i in str(n):
        sum_ += int(i)
    
    return(sum_)

def main():
    not_self_=[]
    for i in range(1, 10001):
        not_self_.append(d(i))
    
    for i in range(1, 10001):
        if i not in not_self_:
            print(i)
main()
