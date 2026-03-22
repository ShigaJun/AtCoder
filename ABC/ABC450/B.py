N = int(input())
C = []
for _ in range(N-1):
    C.append(list(map(int, input().split())))
    
for a in range(1, N):
    for c in range(a+1, N+1):
        for b in range(a+1, c):
            if C[a-1][c-a-1] > C[a-1][b-a-1] + C[b-1][c-b-1]:
                print("Yes")
                exit()
else:
    print("No")