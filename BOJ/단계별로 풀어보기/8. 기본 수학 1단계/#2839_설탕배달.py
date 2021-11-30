# 출처: https://www.acmicpc.net/problem/2839
# 상근이가 설탕을 N킬로그램 배달해야 할 때, 몇 개의 봉지를 가져가면 되는지 그 수를 구하는 프로그램
# 상근이가 배달하는 봉지의 최소 개수, 설탕의 무개를 정확하게 N킬로그램을 만들 수 없다면 -1을 출력

n = int(input())
five_cnt_ = n//5

while five_cnt_>-1:
    reWeight_ = n - (five_cnt_)*5
    weight_ = five_cnt_*5 + reWeight_

    if (reWeight_%3 == 0) and (weight_==n):
       print(five_cnt_+reWeight_//3)
       break
    elif (reWeight_%3 != 0):
        five_cnt_ -= 1

if five_cnt_ == -1:   
    print(-1)
 