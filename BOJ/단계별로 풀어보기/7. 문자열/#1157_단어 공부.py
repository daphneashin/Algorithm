# 주어진 단어에서 가장 많이 사용된 알파벳을 출력하는 문제
# 출처: https://www.acmicpc.net/problem/1157

str_ = input().upper()
chr_ = set(str_)

count_, max_c = 0, 0
for c in chr_:
    if str_.count(c) > count_:
        count_ = str_.count(c)
        max_c = c
    elif str_.count(c) == count_:
        max_c = '?'
    else:
        pass

print(max_c)

