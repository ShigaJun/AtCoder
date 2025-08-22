Q = int(input())
# リスト内包表記
query = [list(map(int, input().split())) for _ in range(Q)]
# print(query)
b = []

for i in range(Q):
    # queryのタイプを見る
    if query[i][0] == 1:
        b.append(query[i][1])
    else:
        print(min(b))
        b.remove(min(b))
    # print(b)