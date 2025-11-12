S = list(input())
T = list(input())

X = []
Y = []
Z = []

for i in range(len(S)):
    if ord(S[i]) > ord(T[i]):
        Y.append([i, T[i]])
    elif ord(S[i]) < ord(T[i]):
        Z.append([i, T[i]])

Y = sorted(Y)
Z = sorted(Z, reverse=True)

for j in range(len(Y)):
    S[Y[j][0]] = Y[j][1]
    X.append(''.join(S))
for k in range(len(Z)):
    S[Z[k][0]] = Z[k][1]
    X.append(''.join(S))
    
print(len(X))
for x in X:
    print(x)