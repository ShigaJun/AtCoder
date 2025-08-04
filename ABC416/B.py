s = input()
t = list(s)

if s[0] != '#':
    t[0] = 'o'
for i in range(1, len(s)):
    if s[i - 1] == '#':
        if s[i] != '#':
            t[i] = 'o'    
print("".join(t))