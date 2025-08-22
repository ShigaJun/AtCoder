Q = int(input())
# query は2次元リスト 例1：[[1, 6], [1, 7], [2], [1, 1], [2]]
# リスト内包表記
query = [list(map(int, input().split())) for _ in range(Q)]
# print(query) # コメントを外すと query の中身を確認できる
b = [] # 空の袋

for i in range(Q):
    # query のタイプを見る
    if query[i][0] == 1: # query タイプが 1 のとき
        b.append(query[i][1]) # 整数 x が書かれたボールを 1 つ袋の中に入れる
    else: # query タイプが 2 のとき
        print(min(b)) # 袋に入っているボールのうち書かれている整数が最小のものを 1 つ出力する
        b.remove(min(b)) # その整数を袋から取り出す
    # print(b) # コメントを外すと b の中身を確認できる