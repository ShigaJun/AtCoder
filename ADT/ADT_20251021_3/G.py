import collections

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    c = collections.Counter(A)
    if len(list(c)) == 2:
        if list(c)[0] / list(c)[1] == -1 and abs(c[list(c)[0]] - c[list(c)[1]]) <= 1:
            print("Yes")
            continue
    
    sorted_A = sorted(A, key=abs)
    
    for i in range(1, N - 1):
        if pow(sorted_A[i], 2) != sorted_A[i - 1] * sorted_A[i + 1]:
            print("No")
            break
    else:
        print("Yes")