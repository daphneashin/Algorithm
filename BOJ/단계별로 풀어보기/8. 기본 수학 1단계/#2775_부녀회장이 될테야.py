# 출처: https://www.acmicpc.net/problem/2775
# 층과 거주자 수의 규칙을 찾는 문제
# 계약 조항: a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다.

#2차 배열을 만들자.
for t in range(int(input())):
    k = int(input())
    n = int(input())

    apt_ = [[i for i in range(1, n+1)]]
    for floor_ in range(0, k):
        temp_ = []
        for room_ in range(0, n):
            temp_.append(sum(apt_[floor_][0:room_+1]))
        apt_.append(temp_)
    print(apt_[k][n-1])