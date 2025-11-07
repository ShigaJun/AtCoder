Q = int(input())
A = []
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        A.append(q[1])
    else:
        print(A[-q[1]])