S = list(input())
T = list(input())

U = []
X = []

for i in range(len(S)):
    if S[i] != T[i]:
        U.append([i, T[i]])

U = sorted(U, key=lambda x: x[1])

for j in range(len(U)):
    S[U[j][0]] = U[j][1]
    X.append(''.join(S))
    
print(len(X))
for x in X:
    print(x)