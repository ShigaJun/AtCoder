s = input()
t = input()
for i in range(1, len(s)):
    if ord(s[i]) < 97:
        if s[i - 1] not in t:
            print("No")
            break
else:
    print("Yes")