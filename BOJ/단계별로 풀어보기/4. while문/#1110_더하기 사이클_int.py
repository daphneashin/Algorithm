# 원래 수로 돌아올 때까지 연산을 반복하는 문제
# 출처: https://www.acmicpc.net/problem/1110

num_ = int(input())
new_ = num_
count_ = 1

# 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리를 만든다.
while True:
    sum_ = (new_//10)+(new_%10)
    new_ = (new_%10)*10+(sum_%10)

    if (num_==new_):
        break
    else:
        count_ +=1

print(count_)