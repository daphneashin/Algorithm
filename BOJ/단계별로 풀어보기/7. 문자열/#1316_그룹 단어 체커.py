# 출처: https://www.acmicpc.net/problem/1316

n_ = int(input())
count_ = 0
for i in range(n_):
    str_ = input()
    set_chr_ = set(str_)

    not_ = 0
    for c in set_chr_:
        if (c*str_.count(c) != 1) and (c*str_.count(c) not in str_):
            not_ = 1
            break
    
    if not_ == 0:
        count_ += 1

print(count_)
            