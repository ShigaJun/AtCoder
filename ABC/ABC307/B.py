N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        newS = S[i] + S[j]
        if newS == newS[::-1]:
            print("Yes")
            exit()
print("No")