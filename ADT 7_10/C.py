s = input()
t = input()
for i in range(len(s)):
    if i >= len(t) or s[i] != t[i]:
        print("No")
        break
else:
    print("Yes")