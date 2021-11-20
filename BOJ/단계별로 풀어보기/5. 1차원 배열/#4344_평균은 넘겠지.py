# 과연 그럴까요?
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
# 출처: https://www.acmicpc.net/problem/4344

t_ = int(input())

for c in range(t_):
    nScore_ = list(map(int, input().split()))
    avg_ = sum(nScore_[1:])/nScore_[0]
    above_avg_ = [i for i in nScore_[1:] if i>avg_]

    print(f'{(len(above_avg_)/nScore_[0])*100:.3f}%')
    