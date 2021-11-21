# 한 단어에서 각 알파벳이 처음 등장하는 위치를 찾는 문제
# 알파벳 소문자로만 이루어진 문자가 주어진다.
# 문자에서 각각의 알파벳이 처음 등장하는 위치를, 포함되어 있지 않는 경우에는 -1을 출력하도록 해라.
# 출처: https://www.acmicpc.net/problem/10809

string_ = input()

for i in range(ord('a'), ord('z')+1):
    if chr(i) in string_:
        print(string_.index(chr(i)), end=' ')
    else:
        print('-1', end=' ')