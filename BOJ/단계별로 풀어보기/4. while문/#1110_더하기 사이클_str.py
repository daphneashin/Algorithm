# 원래 수로 돌아올 때까지 연산을 반복하는 문제
# 출처: https://www.acmicpc.net/problem/1110

num_ = str(input())

# 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리를 만든다.
if int(num_) < 10:
    num_ = '0'+num_

new_ = num_
count_ = 1
while True:
    sum_ = str(sum(map(int, new_)))
    new_ = new_[-1]+sum_[-1]

    if (num_==new_):
        break
    else:
        count_ +=1

print(count_)