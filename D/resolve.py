def resolve():
    '''
    code here
    '''
    from collections import deque

    H, W = [int(item) for item in input().split()]
    Ch, Cw = [int(item)-1 for item in input().split()]
    Dh, Dw = [int(item)-1 for item in input().split()]
    grid = [input() for _ in range(H)]
    max_num = 10**6
    fp = [[max_num] * W for _ in range(H)]

    que = deque([[Ch, Cw, 0]])
    fp[Ch][Cw] = 0

    walk = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    warp = [(i, j) for i in range(-2, 3) for j in range(-2, 3) if (i, j) not in [(0, 0)] + walk]

    while que:
        y, x, w_num = que.popleft()

        for dy, dx in walk:
            ny = y + dy
            nx = x + dx

            if 0 <= ny <= H-1 and 0 <= nx <= W-1 and grid[ny][nx] == '.' and fp[ny][nx] > w_num:
                que.appendleft([ny, nx, w_num])
                fp[ny][nx] = w_num

        for dy, dx in warp:
            ny = y + dy
            nx = x + dx
            nw = w_num +1

            if 0 <= ny <= H-1 and 0 <= nx <= W-1 and grid[ny][nx] == '.' and fp[ny][nx] > nw:
                que.append([ny, nx, nw])
                fp[ny][nx] = nw

    if fp[Dh][Dw] != max_num:
        print(fp[Dh][Dw])
    else:
        print(-1)

if __name__ == "__main__":
    resolve()
