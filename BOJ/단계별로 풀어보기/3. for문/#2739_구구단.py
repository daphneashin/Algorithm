# 임의로 입력받은 N을 출력형식에 맞춰 N*1 부터 N*9까지 출력한다.

a = int(input())

for i in range(1, 10, 1):
    print(f'{a} * {i} = {a*i}')
    #print(str(a)+" * "+str(i)+" = "+str(a*i))

# 출처: https://www.acmicpc.net/problem/2739