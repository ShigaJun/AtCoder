N, M = map(int, input().split())
X = list(map(int, input().split()))
# 家が位置している座標が L 個ある（同じ座標に複数の家が位置することもあるから，L = N とは限らない）とし，
# その座標同士の距離を格納しておく配列 diff を用意する．
# なお，diff の要素数は L - 1 である．
# M 個の基地局を置くから，L 個の座標を M 個の集合に分ければ良い．
# つまり，電波の届かない範囲を diff の中から M - 1 箇所選べば良い．
# 家同士の距離が遠いとその分電波強度を強くしなければならないので，
# diff の配列から値の大きい順に選んでいけば良い．
X = sorted(list(set(X)))
L = len(X)
diff = [X[i + 1] - X[i] for i in range(L - 1)]
diff = sorted(diff)
for _ in range(min(M - 1, L - 1)):
    diff.pop()
print(sum(diff))