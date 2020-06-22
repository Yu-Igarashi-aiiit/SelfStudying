"""
BFS（幅優先探索）概要

DFSと同様にある状態から始めてたどり着けるすべての状態を探索する

深さ優先探索は深い階層から探索し、幅優先探索は浅い階層から探索する
つまりDFSはスタックにより実装されたが、BFSはキューによる実装を試みる

たとえば0をスタート地点として1,2,3,4の分岐が存在するとき
0 をプッシュ
0をポップ　01 02 03 04　をスタック                         
01 をポップ　011 012 013 014　をスタック
02　をポップ　021 022 023 024 をスタック
...
これを繰り返していって 状態x == 終了条件　のとき同じ状態を通らない組み合わせを生成 
計算量は(n*遷移数)となる

"""


from collections import deque

# (sx, sy) から (gx, gy) への最短距離を求める
# 辿り着けないと INF
def bfs():
    # すべての点を INF で初期化
    d = [[float("inf")] * m for i in range(n)]

    # 移動4方向のベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # スタートとゴールの座標を探す
    for i in range(n):
        for j in range(m):
            if maze[i][j] == "S":
                sx = i
                sy = j
            if maze[i][j] == "G":
                gx = i
                gy = j

    # スタート地点をキューに入れ、その点の距離を0にする
    que = deque([])
    que.append((sx, sy))
    d[sx][sy] = 0

    # キューが空になるまでループ
    while que:
        # キューの先頭を取り出す
        p = que.popleft()
        # 取り出してきた状態がゴールなら探索をやめる
        if p[0] == gx and p[1] == gy:
            break
        # 移動4方向をループ
        for i in range(4):
            # 移動した後の点を (nx, ny) とする
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            # 移動が可能かの判定とすでに訪れたことがあるかの判定
            # d[nx][ny] != INF なら訪れたことがある
            # コード中の#は壁（選択不可能マス）のこと。
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != "#" and d[nx][ny] == float("inf"):
                # 移動できるならキューに入れ、その点の距離を p からの距離 +1 で確定する
                que.append((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1

    return d[gx][gy]


n, m = map(int, input().split())
maze = [list(input()) for i in range(n)]

print(bfs())