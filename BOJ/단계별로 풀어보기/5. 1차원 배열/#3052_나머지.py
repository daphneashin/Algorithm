# 숫자의 개수와 비슷한 문제
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성한다.
# 출처: https://www.acmicpc.net/problem/3052

n_ = [int(input())%42 for x in range(10)]
print(len(set(n_)))