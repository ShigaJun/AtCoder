S = input()
# "WA" の1つ前が  'W' だった場合，"WA" が新たに現れることになる．
# 'A' の前に 'W' が何個あるかで最終的な文字列がわかる
# 'W' * 3 + 'A' の場合 -> 'A' + 'C' * 3
cnt = 0
for i in range(len(S)):
    print(i)
    if S[i] == 'W':
        cnt += 1
        while i + 1 < len(S) and S[i + 1] == 'W':
            cnt += 1
            i += 1
            print(i)
        if i + 1 < len(S) and S[i + 1] == 'A':
            T = 'A' + 'C' * cnt
            print(T)