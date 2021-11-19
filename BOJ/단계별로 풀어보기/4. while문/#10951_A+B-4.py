# 입력이 끝날 때까지 A+B를 출력하는 문제, EOF에 대해 알아보도록 한다.
# 출처: https://www.acmicpc.net/problem/10951

while True:
    try:
        print(sum(map(int, input().split())))
    except:
        break