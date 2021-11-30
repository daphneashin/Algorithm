# 출처: https://www.acmicpc.net/problem/2869
# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다.
# 높이가 V미터인 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하시오. 

import math

a, b, v = map(int, input().split())
print(math.ceil((v-a)/(a-b))+1)