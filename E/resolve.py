def resolve():
    '''
    code here
    '''
    H, W, M = [int(item) for item in input().split()]
    targets = [[int(item) -1 for item in input().split()] for _ in range(M)]

    col = [0 for _ in range(H)]
    row = [0 for _ in range(W)]

    bomb_set = set()
    # 配列で要素を作ると要素数が$10^8$超える場合、setで要素の座標を持っておく


    for i,j in targets:
        col[i] += 1
        row[j] += 1
        bomb_set.add((i,j))

    max_col = max(col)
    max_row = max(row)
    max_col_index = []
    max_row_index = []

    for i in range(H):
        if col[i] == max_col:
            max_col_index.append(i)

    for i in range(W):
        if row[i] == max_row:
            max_row_index.append(i)

    res = 0
    for item in max_col_index:
        for jtem in max_row_index:
            if (item,jtem) not in bomb_set:
                # setのin演算子はオーダ1
                res =max_col + max_row
                break
        else:
            res = max(res, max_col + max_row -1 )
    print(res)

if __name__ == "__main__":
    resolve()
