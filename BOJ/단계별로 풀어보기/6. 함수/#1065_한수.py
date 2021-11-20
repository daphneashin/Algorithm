# X가 한수인지 판별하는 함수를 정의하여 문제를 해결
# 1~99는 모두 한수이고, 100의 자리 숫자와 10의자리 숫자의 차이, 10의 자리 숫자와 1의자리 숫자의 차이가 같으면 한수
# 1~99가 한수인 이유는 각 자리의 숫자들이 등차수열로 이루어져있는지, 각 자리의 숫자가 균등한 차이를 보이는지 알 수 없기 때문
# 출처: https://www.acmicpc.net/problem/1065

n_ = int(input())
count_ = 0

for i in range(1, n_+1):
    if i<100:
        count_ +=1
    elif len(str(i))==3:
        num_ = list(map(int, str(i)))
        if ((num_[2]-num_[1])==(num_[1]-num_[0])):
            count_+=1
        else:
            pass
    else:
        num_ = list(map(int, str(i)))
        if ((num_[3]-num_[2])==(num_[2]-num_[1])==(num_[1]-num_[0])):
            count_+=1

print(count_)