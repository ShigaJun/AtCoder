S = input()
T = input()

N = [n for n in range(ord('a'), ord('z') + 1)]

for i in range(1, len(S)):
    if N[ord(T[i]) - ord('a')] - N[ord(S[i]) - ord('a')] != N[ord(T[i - 1]) - ord('a')] - N[ord(S[i - 1]) - ord('a')]:
        print("No")
        exit()
print("Yes")