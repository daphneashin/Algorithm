# 규칙에 따라 문자에 대응하는 수를 출력하는 문제
# 출처: https://www.acmicpc.net/problem/5622

str_ = input()

dial_ = {}
chr_ = 'A'
for i in range(3, 11):
    num_ = 3
    if (chr_ == 'P') or (chr_ == 'W'):
        num_ = 4
    
    for n in range(num_):
        dial_[chr_] = i
        chr_ = chr(ord(chr_)+1)

result_ = 0
for se_ in str_:
    result_ += dial_[se_]

print(result_)
