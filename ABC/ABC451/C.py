import heapq

Q = int(input())
q = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(q, query[1])
    else:
        while len(q) > 0 and q[0] <= query[1]:
            heapq.heappop(q)
    print(len(q))