# 출처: https://www.acmicpc.net/problem/1193 
# 분수의 순서에서 규칙을 찾는 문제

n = int(input())
count_ = 1
nums_ = (count_*(count_+1))//2

while n>nums_:
    count_ += 1
    nums_ = (count_*(count_+1))//2

# numerator_ = 분자, denominator_ = 분모
numerator_ = n - (nums_ - count_)
denominator_ = (count_ + 1) - numerator_
if count_%2 == 0:
    print(f'{numerator_}/{denominator_}')
else:
    print(f'{denominator_}/{numerator_}')


