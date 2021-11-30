# 출처: https://www.acmicpc.net/problem/2292
# 벌집이 형성되는 규칙에 따라 벌집의 위치를 구하는 문제

n = int(input())
nums_ = 1
count_ = 1

while n>nums_:
    nums_ = nums_ + (6*count_)
    count_ += 1

print(count_)

