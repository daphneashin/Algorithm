# 평균을 조작하는 문제
# 시험 본 과목의 개수가 N개 일 때, 점수 중 최댓값을 고른다.
# 이후, 나머지 점수를 (점수/M)*100으로 고치고 평균을 구한다.
# 출처: https://www.acmicpc.net/problem/1546

n_ = int(input())
scores_ = list(map(int, input().split()))
print((sum(scores_)*100/max(scores_))/n_)