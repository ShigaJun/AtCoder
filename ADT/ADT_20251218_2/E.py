S = input()
# "WA" の1つ前が  'W' だった場合，"WA" が新たに現れることになる．
# 'A' の前に 'W' が何個あるかで最終的な文字列がわかる
# 'W' * 3 + 'A' の場合 -> 'A' + 'C' * 3
ans = []
i = 0
while i < len(S):
    cnt = 0
    if S[i] == 'W':
        cnt += 1
        i += 1
        while i < len(S) and S[i] == 'W':
            cnt += 1
            i += 1
        if i < len(S) and S[i] == 'A':
            ans.append('A' + 'C' * cnt)
            i += 1
        else:
            ans.append('W' * cnt)
    else:
        ans.append(S[i])
        i += 1
print(''.join(ans))