q = int(input())
l = []
for i in range(q):
    query = input().split()
    if query[0] == '1':
        l.append(int(query[1]))
    else:
        ans = l.pop(l.index(min(l)))
        print(ans)