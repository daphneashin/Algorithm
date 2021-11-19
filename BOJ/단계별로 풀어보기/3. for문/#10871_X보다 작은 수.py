# for와 if를 같이 쓰는 문제
# 출처: https://www.acmicpc.net/problem/10871

n, x = map(int, input().split())
score = []

for i in list(map(str, input().split())):
    if int(i)<x:
        score.append(i)

print(' '.join(score))