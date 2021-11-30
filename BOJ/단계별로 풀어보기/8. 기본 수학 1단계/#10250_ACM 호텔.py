# 출처: https://www.acmicpc.net/problem/10250
# 호텔 방 번호의 규칙을 찾아 출력하는 문제

for i in range(int(input())):
    h, w, n = map(int, input().split())
    room_num_ = 0

    if n%h == 0:
        room_num_ = (h*100) + (n//h)
    else:
        room_num_ = (n%h)*100 + (n//h)+1

    print(room_num_)