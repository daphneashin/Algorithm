# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램
# 출처: https://www.acmicpc.net/problem/2742

print('\n'.join(map(str,range(int(input()), 0, -1))))

