t = int(input())
for i in range(t):
    n = int(input())
    s = list(input())
    s = [int(x) for x in s]
    kiken = []
    for j in range(len(s)):
        if s[j] == 1:
            kiken.append(j + 1)
    print(kiken)