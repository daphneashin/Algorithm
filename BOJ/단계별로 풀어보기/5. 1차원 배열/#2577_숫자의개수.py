# 각 숫자가 몇 번 나왔는지 저장하기 위해 일차원 배열을 만드는 문제
# 출처: https://www.acmicpc.net/problem/2577

input_ = [int(input()) for x in range(3)]
mul_ = str(input_[0]*input_[1]*input_[2])

for i in range(10):
    print(mul_.count(str(i)))
