t = input()
u = input()

for i in range(len(t) - len(u) + 1):
    if t[i] == u[0] or t[i] == '?':
        for j in range(1, len(u)):
            if t[i + j] != u[j] and t[i + j] != '?':
                break
        else:
            print("Yes")
            break
else:
    print("No")