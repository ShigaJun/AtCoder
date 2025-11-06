S = input()
T = input()

for i in range(1, len(S)):
    if (ord(T[i]) - ord(S[i])) % 26 != (ord(T[i - 1]) - ord(S[i -1])) % 26:
        print("No")
        exit()
print("Yes")