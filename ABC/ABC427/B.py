N = int(input())
A = [1]

for i in range(1, N + 1):
    sumF = 0
    for j in range(i):
        tmp = str(A[j])
        for a in tmp:
            sumF += int(a)
    A.append(sumF)
print(A[N])