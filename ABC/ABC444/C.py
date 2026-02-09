N = int(input())
A = list(map(int, input().split()))

minL = max(A)
listL = []
if A[0] >= minL:
    listL.append(A[0])
for l in  A[1:]:
    tmp = A[0] + l
    if tmp >= minL:
        listL.append(tmp)
listL = sorted(set(listL))
print(listL)