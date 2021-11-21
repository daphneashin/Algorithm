# 아스키 코드에 대해 알아보는 문제
# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력
# 출처: https://www.acmicpc.net/problem/11654

n_ = input()
print(ord(n_))      # 문자 → 아스키 코드: ord() 이 반대는 chr()