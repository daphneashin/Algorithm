# 시험 점수를 성적으로 바꾸는 문제
# 출처: https://www.acmicpc.net/problem/9498

score_ = int(input())

if (90<=score_): print("A")
elif (80<=score_): print("B")
elif (70<=score_): print("C")  
elif (60<=score_): print("D")    
else: print("F")