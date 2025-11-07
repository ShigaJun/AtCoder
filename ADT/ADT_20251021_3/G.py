import collections

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    c = collections.Counter(A)
    elements = list(c)
    if len(elements) == 2 and elements[0] / elements[1] == -1 and abs(c[elements[0]] - c[elements[1]]) <= 1:
            print("Yes")
            continue
    
    sorted_A = sorted(A, key=abs)
    
    for i in range(1, N - 1):
        if pow(sorted_A[i], 2) != sorted_A[i - 1] * sorted_A[i + 1]:
            print("No")
            break
    else:
        print("Yes")