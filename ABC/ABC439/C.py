N = int(input())

l = [0] * N
for x in range(1, 3164):
    for y in range(x+1, 3164):
        n = x ** 2 + y ** 2
        if n <= N:
            l[n-1] += 1
         
cnt = 0
ans = []
for i in range(N):
    if l[i] == 1:
        cnt += 1 
        ans.append(i+1)
print(cnt)
print(*ans)