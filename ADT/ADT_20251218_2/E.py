S = list(input())
#後ろから見ていけば簡単！
for i in range(len(S) - 1, -1, -1):
    if i - 1 >= 0 and S[i - 1] + S[i] == "WA":
        S[i - 1] = 'A'
        S[i] = 'C'
print(''.join(S))