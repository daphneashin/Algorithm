# OX퀴즈의 결과를 일차원 배열로 입력받아 점수를 계산하는 문제
# 출처: https://www.acmicpc.net/problem/8958

for i in range(int(input())):
    ox_ = input()
    total_ = 0
    score_ = 0

    for c in ox_:
        if c == 'O':
            score_ += 1
            total_ += score_
        else:
            score_ = 0
    print(total_)
             

