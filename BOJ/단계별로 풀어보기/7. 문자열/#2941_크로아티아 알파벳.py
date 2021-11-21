# 크로아티아 알파벳의 개수를 세는 문제
# 크로아티아 알파벳으로 구성된 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져있는가
# 알파벳 소문자와 '-', '='로만 이루어진 단어만 입력됨
# 출처: https://www.acmicpc.net/problem/2941

croatia_alphabet_ = ['c=', 'c-', 'dz=', 'd-', 'lj','nj','s=','z=']
str_ = input()
count_ = len(str_)

for i in croatia_alphabet_:
    if i in str_:
        count_ += str_.count(i)*(1-len(i))
        str_ = str_.replace(i, " ")

print(count_)