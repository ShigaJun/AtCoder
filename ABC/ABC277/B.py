N = int(input())
S = []
P = ['H', 'D', 'C', 'S']
C = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

for _ in range(N):
    s = input()
    if s[0] not in P or s[1] not in C or s in S:
        print("No")
        exit() 
    S.append(s)

print("Yes")